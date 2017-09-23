# -*- coding: utf-8 -*-
{
    'name': 'Event Location',
    'version': '1.0',
    'category': 'Marketing',
    'summary': 'Event Location',
    'description': """
Apply the following customizations to accounting module:
=======================================================

* Create a new menu in event module of name locations
    """,
    'depends': ['base_setup','web','event'],
    'data': [
        'views/web_map_templates.xml',
        'views/res_config_views.xml',
        'views/event_location_view.xml',
    ],
    'qweb': [
        'static/src/xml/web_map.xml',
    ],
    'installable': True,
}