# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
import logging
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class player(models.Model):

     _name = 'moixoloadventure.player'
     _description = 'Player '
     name = fields.Char()
     dni = fields.Char()
     description = fields.Text()
     edad = fields.Integer()
     foto = fields.Image(max_with=200, max_heigth=200)

     cities = fields.One2many("moixoloadventure.city", "player")

     #funcions del player
     @api.constrains('dni')     
     def _check_dni(self):
          regex = re.compile('[0-9]{8}[a-z]\\Z' ,re.I)
          for s in self:
               if regex.match(s.dni):
                   _logger.info('el dn es valid')
               else:
                    raise ValidationError('dni no valid')


class city(models.Model):
     _name = 'moixoloadventure.city'
     _description = 'city '
     foto = fields.Image(max_with=200, max_heigth=200)
     name = fields.Char()
     description = fields.Text()
     nivel = fields.Integer()
     poweratac=fields.Integer()
     powerresistance=fields.Integer()
     

     player = fields.Many2one("moixoloadventure.player")
     


class squadron(models.Model):
     _name = 'moixoloadventure.squadron'
     _description = 'squadron '
     foto = fields.Image(max_with=200, max_heigth=200)
     name = fields.Char()
     description = fields.Text()
     datacreation = fields.Datetime(default=lambda self:fields.Datetime.now())
     numberbatlesassisted=fields.Integer()
     cantfigters = fields.Integer()

     
     powerresistance=fields.Integer(compute='_get_nivelbase')
     poweratac=fields.Integer(compute='_get_nivelbase')
     nivel = fields.Integer()

     # agafem el id de on ve | variable que ho te
     fighters = fields.One2many("moixoloadventure.cantsquadronfigther", "squadron" )
     batle = fields.Many2many("moixoloadventure.batle")
     city = fields.Many2one("moixoloadventure.city")
    
    #funcions escuadron
     def _get_nivelbase(self):
          for squadron in self:
               resistance=0
               powerattac=0
               for figther in squadron.fighters:
                    resistance = resistance + figther.fighter.powerresistance * figther.cant
                    powerattac = resistance + figther.figther.poweratac * figther.cant
               squadron.powerresistance = resistance
               squadron.poweratac = powerattac
     



class cantsquadronfigther(models.Model):
     _name = 'moixoloadventure.cantsquadronfigther'
     _description = 'Cant figthers for squadron '
     nivel = fields.Integer()
     cant = fields.Integer()

     fighter = fields.Many2one("moixoloadventure.fighter")
     squadron = fields.Many2one("moixoloadventure.squadron")

     

class fighter(models.Model):

     _name = 'moixoloadventure.fighter'
     _description = 'fighter'
     foto = fields.Image(max_with=200, max_heigth=200)
     name = fields.Char()
     description = fields.Text()
     
     powerresistance=fields.Integer()
     poweratac=fields.Integer()


class batle(models.Model):
     _name = 'moixoloadventure.batle'
     _description = 'Batle'
     name = fields.Text()
     time = fields.Datetime()
     duration = fields.Integer()
     winer = fields.Text()
     louser = fields.Text()

     squadron = fields.Many2many("moixoloadventure.squadron")

     
#    
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
