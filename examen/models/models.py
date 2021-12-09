# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class furgoneta(models.Model):
    _name = 'examen.furgoneta'
    _description = 'usada per a fer els repartos '

    name = fields.Char()
    foto = fields.Image(max_weight=200, max_height=200)
    capacitat = fields.Float()
    matricula = fields.Char() #conte que una maticula te lletres i números
    

    viatgequefa = fields.One2many("examen.viatge", "furgonetaasociada")



class paquet(models.Model):
    _name = 'examen.paquet'
    _description = 'El que es transporta'

    name = fields.Char()
    foto = fields.Image(max_weight=200, max_height=200)
    volum = fields.Float()
    identificador = fields.Integer() 

    viageotorgat = fields.Many2one("examen.viatge")

  

class viatge(models.Model):
    _name = 'examen.viatge'
    _description = 'El que es fa transporta'

    ident = fields.Integer()
    conductor = fields.Char()

    furgonetaasociada = fields.Many2one("examen.furgoneta")
    paquetsqueporta = fields.One2many("examen.paquet", "viageotorgat")
    volumgastats = fields.Float(compute="_get_volumpaquet")


    def _get_volumpaquet(self):
        
        for c in self:
            total = 0
            for b in c.paquetsqueporta:
                 total = total + b.volum

        c.volumgastats = total




    @api.constrains('volumgastats', 'furgonetaasociada')
    def _check_something(self):
        for v in self:
            if v.furgonetaasociada.capacitat < v.volumgastats:
                raise ValidationError("sobrepassa el volum del vehicle:")





#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
