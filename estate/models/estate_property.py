# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "estate property"
    # _order = "sequence"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    def _get_default_date(self):
        return fields.Date.context_today(self) + relativedelta(months=3)
    date_availability = fields.Date(copy=False, default=_get_default_date)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
            help="garden_orientation")
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('received', 'Offer Received'),
        ('accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
        ], string='Status', default='new', copy=False, required=True)
    property_type_id = fields.Many2one("estate_property_type", string="Property Type")
    buyer_partner_id = fields.Many2one('res.partner', 'Buyer', copy=False)
    seller_user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate_property_tags", string="Tags")
    offer_ids = fields.One2many("estate_property_offer", "property_id", string="Offers")
