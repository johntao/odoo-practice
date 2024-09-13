# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate_property_tags"
    _description = "estate property type"
    # _order = "sequence"

    name = fields.Char(required=True)
    description = fields.Text()