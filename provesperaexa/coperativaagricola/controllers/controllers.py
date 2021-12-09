# -*- coding: utf-8 -*-
# from odoo import http


# class Coperativaagricola(http.Controller):
#     @http.route('/coperativaagricola/coperativaagricola/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coperativaagricola/coperativaagricola/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coperativaagricola.listing', {
#             'root': '/coperativaagricola/coperativaagricola',
#             'objects': http.request.env['coperativaagricola.coperativaagricola'].search([]),
#         })

#     @http.route('/coperativaagricola/coperativaagricola/objects/<model("coperativaagricola.coperativaagricola"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coperativaagricola.object', {
#             'object': obj
#         })
