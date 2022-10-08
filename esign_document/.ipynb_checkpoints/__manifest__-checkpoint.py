# -*- coding: utf-8 -*-

{
    'name': 'Chepss Esign',
    'sumary': """Chepss esign module""",
    'description':"""
        Chepss esign to manage documents:
        - Esign
        - Documents
    """,
    'author': 'CHEPSS',
    'website': 'https://www.chepss.cl',
    'category': 'Sign',
    'version': '0.1',
    'depends': ['hr'],
    'license': 'LGPL-3',
    'data':[
        'security/esign_security.xml',
        'security/ir.model.access.csv',
        'views/esign_menuitems.xml',
        'views/document_view.xml',       
    ],
    'demo':[
        
    ],
}