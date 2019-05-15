# -*- coding: utf-8 -*-
from odoo import http

# class Addons/library(http.Controller):
#     @http.route('/addons/library/addons/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/library/addons/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/library.listing', {
#             'root': '/addons/library/addons/library',
#             'objects': http.request.env['addons/library.addons/library'].search([]),
#         })

#     @http.route('/addons/library/addons/library/objects/<model("addons/library.addons/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/library.object', {
#             'object': obj
#         })