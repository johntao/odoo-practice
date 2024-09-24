# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate_property_type"
    _description = "estate property type"
    # _order = "sequence"

    name = fields.Char(required=True)
    description = fields.Text()
    _sql_constraints = [
        (
            "name_uniq",
            "unique(name)",
            "An estate property type with the same name already exists.",
        )
    ]
