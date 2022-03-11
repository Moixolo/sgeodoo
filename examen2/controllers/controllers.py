# -*- coding: utf-8 -*-
# from odoo import http


# class Examen2(http.Controller):
#     @http.route('/examen2/examen2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen2/examen2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen2.listing', {
#             'root': '/examen2/examen2',
#             'objects': http.request.env['examen2.examen2'].search([]),
#         })

#     @http.route('/examen2/examen2/objects/<model("examen2.examen2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen2.object', {
#             'object': obj
#         })
