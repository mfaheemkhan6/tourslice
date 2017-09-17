# -*- coding: utf-8 -*-
{
    'name': 'Accounting Customization',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'CAccounting Customization',
    'description': """
Apply the following customizations to accounting module:
=======================================================

* Custom modifications invoices pivot table
    """,
    'depends': ['account_accountant'],
    'data': [
        'views/account_invoice_report_inherit_view.xml',
    ]
}
