# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate_property_offer"
    _description = "estate property offer"
    # _order = "sequence"

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
        ], copy=False)
    buyer_partner_id = fields.Many2one('res.partner', 'Buyer', required=True)
    property_id = fields.Many2one('estate_property', required=True)