# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare
# from odoo.tools import date_utils


class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer"
    _description = "estate property offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        copy=False,
    )
    buyer_partner_id = fields.Many2one("res.partner", "Buyer", required=True)
    property_id = fields.Many2one("estate_property", required=True)
    property_type_id = fields.Many2one("estate_property_type", related="property_id.property_type_id", store=True)

    validity = fields.Integer(default=7)

    @api.depends("validity")
    def _compute_deadline(self):
        for item in self:
            if item.create_date:
                item.date_deadline = item.create_date + relativedelta(
                    days=item.validity
                )

    def _inverse_deadline(self):
        for offer in self:
            if not offer.date_deadline:
                continue
            if offer.create_date:
                offer.validity = (
                    offer.date_deadline - fields.Date.to_date(offer.create_date)
                ).days

    date_deadline = fields.Date(
        compute="_compute_deadline", inverse="_inverse_deadline"
    )

    def action_accept(self):
        self.ensure_one()
        prop = self.property_id
        if prop.state == "accepted":
            raise UserError("Only one offer can be accepted at a time")
        prop.state = "accepted"
        self._check_offer_price_rule([self.price])
        prop.selling_price = self.price
        prop.buyer_partner_id = self.buyer_partner_id
        self.status = "accepted"
        return True

    def action_refuse(self):
        prop = self.property_id
        if self.status == "accepted":
            prop.state = "received"
        # prop.selling_price = None
        prop.buyer_partner_id = None
        self.status = "refused"
        return True

    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The price of an offer must be positive."),
    ]

    @api.constrains("price", "property_id")
    def _check_offer_price(self):
        accepted_price = self.filtered(lambda x: x.status == "accepted").mapped("price")
        self._check_offer_price_rule(accepted_price)

    def _check_offer_price_rule(self, accepted_price):
        prop = self.property_id
        expected_price_min = prop.expected_price * 0.9
        accepted_price_max = max(accepted_price, default=0)
        if accepted_price_max == 0:
            return
        invalid_expected_price = (
            float_compare(accepted_price_max, expected_price_min, None, 2) == -1
        )
        if invalid_expected_price:
            raise ValidationError(
                r"Selling price cannot be lower than 90% of the expected price."
            )
