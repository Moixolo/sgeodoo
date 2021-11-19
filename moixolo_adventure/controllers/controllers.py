# -*- coding: utf-8 -*-
# from odoo import http


# class MoixoloAdventure(http.Controller):
#     @http.route('/moixolo_adventure/moixolo_adventure/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moixolo_adventure/moixolo_adventure/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moixolo_adventure.listing', {
#             'root': '/moixolo_adventure/moixolo_adventure',
#             'objects': http.request.env['moixolo_adventure.moixolo_adventure'].search([]),
#         })

#     @http.route('/moixolo_adventure/moixolo_adventure/objects/<model("moixolo_adventure.moixolo_adventure"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moixolo_adventure.object', {
#             'object': obj
#         })
