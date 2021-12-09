# -*- coding: utf-8 -*-

from collections import namedtuple
from odoo import models, fields, api
import re
import logging

from odoo import http

_logger = logging.getLogger(__name__)


class player(models.Model):#******************************************************************************************

     _name = 'moixoloadventure.player'
     _description = 'Player '

     foto = fields.Image(max_weigth=200, max_heigth=200)
     
     name = fields.Char()
     surename1 = fields.Char()
     surename2 = fields.Char()
     edad = fields.Integer(compute="_get_calculEdad")
     birthday = fields.Date()     
     dni = fields.Char()

     username = fields.Char()
     levelUser = fields.Integer()
     description = fields.Text()
     descriptionuser = fields.Text()
     nextlevel = fields.Integer()
     capacitisquadroncity = fields.Integer()
     

     cantCities = fields.Integer()
    

     cities = fields.One2many("moixoloadventure.city", "player")
     squadron = fields.One2many("moixoloadventure.squadron", "city")
     
     #def _calculMaxCities(self):
      #    cantCities = 0
       #   for cities in city.name:
        #       cantCities = cantCities + 1

     @api.depends('birthday')
     def _get_calculEdad(self):
          for t in self:
               if (t.birthday):
                    dataactual = fields.Date.from_string(fields.Date.today())
                    datanaixement = fields.Date.from_string(t.birthday)

                    t.edad = ((dataactual - datanaixement).days)/365
               else:
                    t.edad = 0


     @api.constrains('dni')     
     def _check_dni(self):
          regex = re.compile('[0-9]{8}[a-z]\\Z' ,re.I)
          for s in self:
               if regex.match(s.dni):
                   _logger.info('el dn es valid')
               else:
                    raise ValidationError('dni no valid')


class city(models.Model):#******************************************************************************************
     _name = 'moixoloadventure.city'
     _description = 'city '
     foto = fields.Image(max_weigth=200, max_heigth=200)
     name = fields.Char()
     description = fields.Text()
     level = fields.Integer()
     poweratac=fields.Integer()
     powerresistance=fields.Integer(compute="_get_powresis")
     

     player = fields.Many2one("moixoloadventure.player")
     squadron = fields.One2many("moixoloadventure.squadron", "city")

     @api.depends('poweratac', 'powerresistance')
     def _get_powresis(self):
          #sumapoweratac = 0
          sumapowerresistance = 0
          for p in self:
               if(p.powerresistance ):
                    #sumapoweratac = sumapoweratac + p.poweratac
                    sumapowerresistance = sumapowerresistance + p.powerresistance
                    p.powerresistance = sumapowerresistance
                    #p.poweratac = sumapoweratac
               else:
                    p.powerresistance = 0
                    #p.poweratac = 0
            
          


class squadron(models.Model):#*********************************************************************************
     _name = 'moixoloadventure.squadron'
     _description = 'squadron '
     foto = fields.Image(max_weigth=100, max_heigth=100)
     name = fields.Char()
     description = fields.Text()
     datacreation = fields.Datetime(default=lambda self:fields.Datetime.now())
     numberbatlesassisted=fields.Integer()

     powerresistance=fields.Integer(compute='_get_nivelbase')
     poweratac=fields.Integer(compute='_get_nivelbase')
        
     nivel = fields.Integer(compute="_get_nivelbase")

     # agafem el id de on ve | variable que ho te
     fighters = fields.One2many("moixoloadventure.cantsquadronfigther", "squadron" )
     batle = fields.Many2many("moixoloadventure.batle")
     city = fields.Many2one("moixoloadventure.city")
    
    #funcions escuadron
     def _get_nivelbase(self):
          for squadron in self:
               resistance=0
               powerattac=0
               nivell = 0
               for figther in squadron.fighters:
                    resistance = resistance + figther.figther.powerresistance * figther.cant
                    powerattac = resistance + figther.figther.poweratac * figther.cant
                    nivell = nivell + figther.figther.nivel
               squadron.powerresistance = resistance
               squadron.poweratac = powerattac
               squadron.nivel = nivell
     


     
class cantsquadronfigther(models.Model):#******************************************************************************************
     _name = 'moixoloadventure.cantsquadronfigther'
     _description = 'Cant figthers for squadron '
     
     cant = fields.Integer()     
     positionFormation = fields.Selection([('1', '1'), ('2','2'), ('3', '3')])

     figther = fields.Many2one("moixoloadventure.fighter", ondelete='set null')
     squadron = fields.Many2one("moixoloadventure.squadron")

     nivellfigther = fields.Integer(related="figther.nivel")
     

class fighter(models.Model):#******************************************************************************************
     _name = 'moixoloadventure.fighter'
     _description = 'fighter'
     foto = fields.Image(max_weigth=200, max_heigth=200)
     name = fields.Char()
     description = fields.Text()
     
   
     powerresistance=fields.Integer()
     poweratac=fields.Integer()

     nivel = fields.Integer(compute="_get_level")
    
     @api.depends("powerresistance", "poweratac") #forçar el canvi de estes variables
     def _get_level(self):
          for f in self:
               f.nivel =  f.powerresistance + f.poweratac



class batle(models.Model):#******************************************************************************************
     _name = 'moixoloadventure.batle'
     _description = 'Batle'
     name = fields.Text()
     time = fields.Datetime()
     timeFinish = fields.Datetime()
     duration = fields.Integer()
     winer = fields.Boolean()
     louser = fields.Boolean()

     squadron = fields.Many2many("moixoloadventure.squadron")

class calendar(models.Model):
     _name = 'moixoloadventure.calendar'
     _description ='calenad ot batles'
     name = fields.Text()
     duration = fields.Integer()
     initialDate = fields.Datetime()
     finalDate = fields.Datetime()     

     batle = fields.Many2one("moixoloadventure.batle")

#************************  VISTES HEADER **********************************************************************
#class banner_city_controller(http.Controller):
#    @http.route('model', auth='user', type='json')
#    def banner(self):
#        return {
#        return {
#            'html': """
#                <div>
#                <div>
#                <div class="negocity_button" style="position: static; color:#fff;"><a>Generate Cities</a></div>
#                </div> """
#        }

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
