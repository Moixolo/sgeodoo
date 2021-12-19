# -*- coding: utf-8 -*-
# from odoo import http


# class GestioClinicaDental(http.Controller):
#     @http.route('/gestio_clinica_dental/gestio_clinica_dental/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestio_clinica_dental/gestio_clinica_dental/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestio_clinica_dental.listing', {
#             'root': '/gestio_clinica_dental/gestio_clinica_dental',
#             'objects': http.request.env['gestio_clinica_dental.gestio_clinica_dental'].search([]),
#         })

#     @http.route('/gestio_clinica_dental/gestio_clinica_dental/objects/<model("gestio_clinica_dental.gestio_clinica_dental"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestio_clinica_dental.object', {
#             'object': obj
#         })
