# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
from dbus import ValidationException
from odoo import models, fields, api


class persona(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'
     _description = 'All information from person'

     name = fields.Char()
     cognom = fields.Char()
     description = fields.Text()

     emails= fields.One2many(comodel_name='examen2.email', inverse_name="persona")
     direccio = fields.Many2many(comodel_name='examen2.direccion')

    
     def crearpersonawizar(self):
       return self.env.ref("examen2.actionwizard_window").read()[0]

class email(models.Model):
     _name = 'examen2.email'
     _description = 'informació dels correus'

     email = fields.Char()
     persona = fields.Many2one(comodel_name='examen2.persona')

class direccion(models.Model):
     _name = 'examen2.direccion'
     _description = 'informació de les direccion'

     carrer = fields.Char()
     numero = fields.Integer()
     provincia = fields.Selection([('1','Valencia'),('2','Alacant'),('3','Castello')])
     
     persona = fields.Many2many(comodel_name='examen2.persona', relation='direcciopersona')

class wizard(models.TransientModel):
     _name = "examen2.wizard"
     
     name = fields.Char()

class cronmoixo(models.Model):
     _name = "examen2.cronmoixo"

     nombre = fields.Char()
     data = fields.Integer()

     def mostrarmissatge(self):
          raise ValidationErr('MIAAAAAU')


class finestra(models.Model):
     _name = "examen2.finestra"
     _description = "es el primer cron que faig"

     def finestradvertencia(self):
          raise ValidationError("Your record is too small:")

