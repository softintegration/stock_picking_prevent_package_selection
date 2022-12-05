# -*- coding: utf-8 -*- 


{
    'name': 'Prevent selection of packages in transfers',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Stock',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'views/stock_move_views.xml',
        'views/stock_picking_views.xml'
    ],
    'license': 'LGPL-3',
}
