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
    # def __init__(self, dt1=None, dt2=None,
    #              years=0, months=0, days=0, leapdays=0, weeks=0,
    #              hours=0, minutes=0, seconds=0, microseconds=0,
    #              year=None, month=None, day=None, weekday=None,
    #              yearday=None, nlyearday=None,
    #              hour=None, minute=None, second=None, microsecond=None):
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
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('received', 'Offer Received'),
        ('accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
        ], string='Status', default='new', copy=False, required=True)
    garden_orientation = fields.Selection(string='Type',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
            help="garden_orientation")
    # number_of_months = fields.Integer(required=True)
    # active = fields.Boolean(default=True)
    # sequence = fields.Integer(default=10)
# Field	Type
    # _sql_constraints = [
    #     ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    # ]