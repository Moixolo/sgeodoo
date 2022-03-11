# -*- coding: utf-8 -*-
# from odoo import http


# class Cansons(http.Controller):
#     @http.route('/cansons/cansons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cansons/cansons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cansons.listing', {
#             'root': '/cansons/cansons',
#             'objects': http.request.env['cansons.cansons'].search([]),
#         })

#     @http.route('/cansons/cansons/objects/<model("cansons.cansons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cansons.object', {
#             'object': obj
#         })
