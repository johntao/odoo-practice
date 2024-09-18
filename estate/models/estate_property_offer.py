# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
# from odoo.tools import date_utils

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
    
    validity = fields.Integer(default=7)
    @api.depends('validity')
    def _compute_deadline(self):
        for item in self:
            if item.create_date:
                item.date_deadline = item.create_date + relativedelta(days=item.validity)
    def _inverse_deadline(self):
        for item in self:
            if item.create_date:
                item.validity = (item.date_deadline -  fields.Date.to_date(item.create_date)).days
    date_deadline = fields.Date(compute='_compute_deadline', inverse="_inverse_deadline")