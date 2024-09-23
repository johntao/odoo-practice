# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import UserError
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
    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area = 10 if self.garden else None
        self.garden_orientation = 'north' if self.garden else None
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
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    total_area = fields.Integer(compute='_compute_total_area')
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.mapped('offer_ids.price'), default=0)
    best_price = fields.Float(compute='_compute_best_price')
    
    def action_sold(self):
        if self.state == 'canceled':
            raise UserError('Canceled property cannot be sold.')
        self.state = 'sold'
        return True
    def action_cancel(self):
        if self.state == 'sold':
            raise UserError('Sold property cannot be canceled.')
        self.state = 'canceled'
        return True