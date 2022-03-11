# -*- coding: utf-8 -*-

from odoo import models, fields, api


class persona(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Persones que tindràn cançons'

    cansons = fields.Many2many(comodel_name='cansons.canso', relation='personacanso')
    

class canso(models.Model):
    _name = 'cansons.canso'

    name = fields.Char()
    artista = fields.Char()
    popularitat = fields.Integer()

    clients = fields.Many2many(comodel_name='res.partner')
   

class wizard(models.TransientModel):
    _name = "cansons.proces_wizar" #ha de correspondre en el action
        
    cansonsw = fields.Many2one(comodel_name='cansons.canso')
    personaw = fields.Many2one(comodel_name='res.partner')

    def guardarcanso(self):        
                 
        self.personaw.write({'cansons': [(4,self.cansonsw.id,0)]})
                                        
         
      
        

