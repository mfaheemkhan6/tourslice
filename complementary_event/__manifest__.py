# -*- coding: utf-8 -*-
{
    'name': 'Complementary Event',
    'version': '1.0',
    'category': 'Marketing',
    'summary': 'Complementary Event',
    'description': """
Apply the following customizations to accounting module:
=======================================================

* Create a new menu in event module
* Add filter on product category
    """,
    'depends': ['base','event','product'],
    'data': [
        'views/complementary_event_view.xml',
    ]
}
