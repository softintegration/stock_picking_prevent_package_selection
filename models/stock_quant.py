# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.osv import expression


class QuantPackage(models.Model):
    _inherit = "stock.quant.package"

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('picking_id', False):
            prevent_package_selection = self.env['stock.picking'].browse(
                self.env.context.get('picking_id')).picking_type_id.prevent_package_selection
            if prevent_package_selection:
                domain = [('id', '=', -1)]
                args = expression.AND([domain, args])
        return super(QuantPackage, self)._name_search(name, args=args, operator=operator, limit=limit,
                                                      name_get_uid=name_get_uid)
