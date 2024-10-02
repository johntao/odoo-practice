# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertySeller(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many(
        "estate.property",
        "seller_user_id",
        string="Estate Props",
        domain=['|', ("state", "=", "new"), ("state", "=", "received")],
    )
