# -*- coding: utf-8 -*-
# from odoo import http


# class Coperativaagricola2(http.Controller):
#     @http.route('/coperativaagricola2/coperativaagricola2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coperativaagricola2/coperativaagricola2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coperativaagricola2.listing', {
#             'root': '/coperativaagricola2/coperativaagricola2',
#             'objects': http.request.env['coperativaagricola2.coperativaagricola2'].search([]),
#         })

#     @http.route('/coperativaagricola2/coperativaagricola2/objects/<model("coperativaagricola2.coperativaagricola2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coperativaagricola2.object', {
#             'object': obj
#         })
