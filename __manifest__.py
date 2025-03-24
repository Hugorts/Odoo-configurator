{
    'name': 'Configurator',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module for configuring roles, translations, and other data in Odoo',
    'description': """
        This module provides tools for managing roles, translations, chart of accounts, and other configurations.
    """,
    'author': 'MK_LAB',
    'depends': ['base'],
    'data': [
        'views/configurator_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}