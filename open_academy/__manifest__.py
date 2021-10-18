# -*- coding: utf-8 -*-
{
    'name': """Open Academy""",

    'summary': """Módulo #1 para la clase de Industria del Software - UNAH""",

    'description': """Mini proyecto correspondiente al III periodo 2021""",

    'author': "Kemuel-López -20141004944",
    'website': "https://github.com/Kemuel-Lopez/Industria",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tool',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner.xml',
        'views/openacademy.xml',
        'reportes/reports.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
