# -*- coding: utf-8 -*-
from odoo import http


class banner_city_controller(http.Controller):
    @http.route('/gestioclinica/personal_banner', auth='user', type='json')
    def banner(self):
        return {
            'html': """
                <div  class="personal_banner" 
                style="height: 150px; background-size:100%; background-image: url(/negocity/static/src/img/negocity_city.jpg)">
                <div class="btn_new_personal" style="position: static; color:#fff; text-align:center; padding-top:35px;">
                    <a style=" background-color:white; color: grey; padding:5px; border: 2px solid grey; border-radius:5px; " class="btn_new_patient" type="action" data-reload-on-close="true" 
                    role="button" data-method="crearpatientwizar" data-model="res.partner">Nuevo paciente</a>                
                </div>
                </div> """
        }


# class gestio_clinica_dental(http.Controller):
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
