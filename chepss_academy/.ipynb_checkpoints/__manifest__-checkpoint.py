# -*- coding: utf-8 -*-

{
    'name': 'Chepss Academy',
    'sumary': """Chepss Academy module""",
    'description':"""
        Chepss Academy to manage training:
        - Training
        - Session
        - Attendees
    """,
    'author': 'CHEPSS',
    'website': 'https://www.chepss.cl',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale'],
    'license': 'LGPL-3',
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_view.xml',
        'views/session_view.xml',
    ],
    'demo':[
        'demo/academy_demo.xml',
    ],
}