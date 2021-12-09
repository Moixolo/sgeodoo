#-*- coding: utf-8 -*-

from odoo import models, fields, api


class coperativaagricola2(models.Model):
     _name = 'coperativaagricola2.coperativaagricola2'
     _description = 'coperativaagricola2.coperativaagricola2'

     name = fields.Char()
     description = fields.Char()
     capacityalmacen = fields.Integer()
     capacidadcamiones = fields.Integer()

     camionespropios = fields.One2many("coperativaagricola2.camio", "coperativa")


class camio(models.Model):
     _name = 'coperativaagricola2.camio'
     _description = 'coperativaagricola2.camio'

     name = fields.Char()
     description = fields.Char()

     cantitatcarrega = fields.Integer()
     duraciocarrega=fields.Integer()
     
     coperativa = fields.Many2one("coperativaagricola2.coperativaagricola2")
     caixonscamio = fields.Many2many("coperativaagricola2.caixo")

    


class caixo(models.Model):
    _name = 'coperativaagricola2.caixo'
    _description = 'coperativaagricola2.caixo'

    name = fields.Char()
    description = fields.Char()
    arrobacapacitat = fields.Integer()
    espaiqueocupa = fields.Integer()

    
   

    camiocaixo = fields.Many2many("coperativaagricola2.camio")
    varietatfruta = fields.Many2many("coperativaagricola2.varietatfruta")
    
    



class varietatfruta(models.Model):
     _name = 'coperativaagricola2.varietatfruta'
     _description = 'coperativaagricola2.varietattaronja'

     name = fields.Char()
     description = fields.Char()
     tempsmaduraciodesdecollita=fields.Datetime(default=fields.Datetime.today)
     arrobaqueacupa = fields.Integer()
     categoriafruta = fields.Selection([('1','Primera'),('2','Segon'),('3','Tercera')])
     

     caixotransport = fields.Many2many("coperativaagricola2.caixo")

     caixonsnecessaris = fields.Integer(compute="_get_caixonsnecessaris")

     @api.depends('caixonsnecessaris')
     def _get_caixonsnecessaris(self):
          
          for c in self:
               c.caixonsnecessaris =  c.caixotransport.arrobacapacitat / c.arrobaqueacupa   

     @api.constrains('arrobaqueacupa')
     def comprobar(self):
          for c in self:
               if c.arrobaqueacupa == 1:
                    c.arrobaqueacupa=10

     def sumaruno(self):
          var = 0
          for i in self:
               var = i.arrobaqueacupa + 1
          i.arrobaqueacupa = var 

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
