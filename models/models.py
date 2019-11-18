# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Asset(models.Model):
	_name = 'account.asset.depreciation.line'
	_inherit = 'account.asset.depreciation.line'
	_description = 'Description'

	amount_degresive = fields.Float(string='Amount Degresive', digits=0,)
	depreciated_value_degresive = fields.Float(string='Depreciated Value Degresive', digits=0,)
	remaining_value_degresive = fields.Float(string='Remaining Value Degresive',)