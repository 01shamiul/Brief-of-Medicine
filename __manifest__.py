# -*- coding: utf-8 -*-
{
    'name': 'Health Care Virtual Assistant',
    'summary': """Something about the App.""",
    'description': """
Health Care Virtual Assistant
=============================
Something about the App.
    """,
    'version': '13.0.1.0',
    'author': 'Company Name',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'web',
    ],
    'data': [
        ## Data
        'data/ir_sequence.xml',

        ## Security
        'security/ir.model.access.csv',

        ## Report
        'reports/report_paper_format.xml',
        'reports/my_model_name_report.xml',
        
        ## Wizard
        'wizards/my_model_name_wizard.xml',
        
        ## View & Wizard
        'views/web_assets.xml',
        'views/my_model_name_view.xml',
        'views/menus.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'qweb': [],
    'demo': [],
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'icon': '/health_care_va/static/description/icon.png',
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Sajal Das <https://github.com/sajaldas19>',
    ],
}
