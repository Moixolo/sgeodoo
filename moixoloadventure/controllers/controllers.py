# -*- coding: utf-8 -*-
# from odoo import http


# class Moixoloadventure(http.Controller):
#     @http.route('/moixoloadventure/moixoloadventure/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moixoloadventure/moixoloadventure/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moixoloadventure.listing', {
#             'root': '/moixoloadventure/moixoloadventure',
#             'objects': http.request.env['moixoloadventure.moixoloadventure'].search([]),
#         })

#     @http.route('/moixoloadventure/moixoloadventure/objects/<model("moixoloadventure.moixoloadventure"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moixoloadventure.object', {
#             'object': obj
#         })
