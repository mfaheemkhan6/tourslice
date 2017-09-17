# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    # gross_margin = fields.Float(string='Gross Margin')
    #
    # # def _select(self):
    # #     return super(AccountInvoiceReport, self)._select() + ", sub.product_id.lst_price as gross_margin"
    #
    # def _sub_select(self):
    #     return super(AccountInvoiceReport, self)._sub_select() + ", ail.product_id.lst_price as gross_margin"
    #
    # def _group_by(self):
    #     return super(AccountInvoiceReport, self)._group_by() + ", ali.product_id.lst_price"
