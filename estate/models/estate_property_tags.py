# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyTags(models.Model):
    _name = "estate_property_tags"
    _description = "estate property type"
    _order = "name"

    name = fields.Char(required=True)
    description = fields.Text()
    color = fields.Integer()
    _sql_constraints = [
        (
            "name_uniq",
            "unique(name)",
            "An estate property tag with the same name already exists.",
        )
    ]
