# -*- coding: utf-8 -*-
{
    'name': "knowledge_base",

    'summary': "Module de gestion des connaissances de l'entreprise ST DIGITAL",

    'description': """
Long description of module's purpose
    """,

    'author': "Kader MOHAMAD Eddy",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Apps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/knowledge_base_security.xml',
        'security/ir.model.access.csv',
        'views/knowledge_article_views.xml',
        'views/knowledge_category_views.xml',
        'views/knowledge_tag_views.xml',
        'views/knowledge_version_views.xml',
        'data/knowledge_article_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

