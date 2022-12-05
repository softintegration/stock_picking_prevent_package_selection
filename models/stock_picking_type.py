# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"


    prevent_package_selection = fields.Boolean(string='Prevent package selection',default=False)
