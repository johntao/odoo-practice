# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Estate xxx',
    'version': '1.0',
    'author': "Author Name",
    'summary': 'Real Estate Management',
    'category': 'Administration',
    'description': 'description',
    'depends': [
        'base',
        'base_setup'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}