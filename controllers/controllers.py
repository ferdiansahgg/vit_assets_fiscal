# -*- coding: utf-8 -*-
from odoo import http

# class VitAssetsFiscal(http.Controller):
#     @http.route('/vit_assets_fiscal/vit_assets_fiscal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_assets_fiscal/vit_assets_fiscal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_assets_fiscal.listing', {
#             'root': '/vit_assets_fiscal/vit_assets_fiscal',
#             'objects': http.request.env['vit_assets_fiscal.vit_assets_fiscal'].search([]),
#         })

#     @http.route('/vit_assets_fiscal/vit_assets_fiscal/objects/<model("vit_assets_fiscal.vit_assets_fiscal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_assets_fiscal.object', {
#             'object': obj
#         })