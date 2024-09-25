# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = "estate_property_type"
    _description = "estate property type"
    _order = "name"
    sequence = fields.Integer(
        "Sequence", default=1, help="Used to order property types. Lower is better."
    )
    name = fields.Char(required=True)
    description = fields.Text()
    _sql_constraints = [
        (
            "name_uniq",
            "unique(name)",
            "An estate property type with the same name already exists.",
        )
    ]
    offer_ids = fields.One2many("estate_property_offer", "property_type_id")
    prop_ids = fields.One2many("estate_property", "property_type_id")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    offer_count = fields.Integer(compute="_compute_offer_count")


# class TestModelLine(models.Model):
#     _name = "test_model_line"
#     _description = "Test Model Line"

#     model_id = fields.Many2one("estate_property")
#     name = fields.Char()
#     expected_price = fields.Float()
#     state = fields.Selection()
