# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class AssetDepreciationLine(models.Model):
	_name = 'account.asset.depreciation.line'
	_inherit = 'account.asset.depreciation.line'

	amount_degresive = fields.Float(string='Amount Degresive', digits=0,)
	depreciated_value_degresive = fields.Float(string='Depreciated Value Degresive', digits=0,)
	remaining_value_degresive = fields.Float(string='Remaining Value Degresive',)

class AssetsAsset(models.Model):
	_name = 'account.asset.asset'
	_inherit = 'account.asset.asset'

	def compute_depreciation_board(self):
		_logger.info('test_fungsi_inherit')
		res = super(AssetsAsset,self).compute_depreciation_board()
		return res

