# -*- coding: utf-8 -*-

from datetime import time
from email.policy import default
from pickle import TRUE
from re import match
from readline import read_init_file
from trace import Trace
from unicodedata import name
from xmlrpc.client import DateTime
from odoo import models, fields, api
from pyrsistent import field

# *************************************************************************************   
# PEOPLE DATES
# *************************************************************************************  

class patient(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    #_name = 'gestio_clinica_dental.patient'
    _description = 'All information from patient'

    #personal dates
    #photo = fields.Image()
    #name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    ispatient = fields.Boolean(default=TRUE)
    vat = fields.Char()
    dateborn = fields.Date()
    years = fields.Integer(compute="_get_calculEdad")
    direction = fields.Char()

    
    
    

    #medical dates
    medicalid = fields.Integer()
    patientshortdescription = fields.Text()
    #salutformulary = fields.Many2many(comodel_name='gestio_clinica_dental.salutformulary', relation='formclinic')#restric to one
    #anamnesispat = fields.Many2many(comodel_name="gestio_clinica_dental.anamnesis",relation='anampatient')#restric to one
    medicalstory = fields.One2many(comodel_name='gestio_clinica_dental.medicalhistory',  inverse_name='patientmed')#restric to one
    #doctorpac = fields.Many2many(comodel_name='res.partner', relation='doctorpatientassigned')
    alergies = fields.Boolean()
    pregnant = fields.Boolean()

    #economicdates
    #patientbud = fields.Many2one(comodel_name='gestio_clinica_dental.budget')
    #paysstatus = fields.Selection([("1","No pay"), ("2","Parcial pay"), ("3","Finalized")])
    #patientpay = fields.Many2one(comodel_name='gestio_clinica_dental.pays')

    #schedule dates
    #quotes = fields.Many2one(comodel_name='gestio_clinica_dental.quotes', relation='quotesagendfrompatient')
    status = fields.Selection([("1","Advised"), ("2","Inside cabinet"), ("3","Finalized"), ("4","Other")])

    #others
    #patientproces  = fields.One2many(comodel_name='gestio_clinica_dental_proces.wizard',  inverse_name='procespatient')#un pacient pot tindre molts processos
    afterimg = fields.Image()
    beforeimg = fields.Image()

    @api.model
    def crearpatientwizar(self):
       return self.env.ref("gestio_clinica_dental.action_proces_wizard_window").read()[0]

       # no se perquè però no funciona    
       # return {
       #     'name': 'nuevopaciente',
       #     'type': 'ir.actions.act_window',
       #     'res_model': "res.partner",
       #     'view_mode': 'form',
       #     'target': 'new',
       #}

class doctor(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    #_name = 'gestio_clinica_dental.doctor'
    #_description = 'doctor description'
    #personal dates
    #photo = fields.Image()
    #name = fields.Char()
    #surname1 = fields.Char()
    #surname2 = fields.Char()
    #phonenumber = fields.Char()
    #direction = fields.Text()
    isdoctor = fields.Boolean(default=TRUE)
    
    
    #profesional dates
    collegiatenumber = fields.Char()
    specialitydoc = fields.Selection([('1','General'),('2','Surgery'),('3','Orthodontics'),('4','Endodontics'),('5','Stetic'),('6','Prosthodontist'),('7','Pediatric')])
    #forenkeys
    #items dates
    datepatientassigned = fields.Date() 
    patientsintervened = fields.Many2many(comodel_name='gestio_clinica_dental.processline', relation='professionalline')
    #doctorsch = fields.Many2many(comodel_name='gestio_clinica_dental.principalschedule', relation='doctorschedule')
    #doctortex = fields.One2many(comodel_name='gestio_clinica_dental.textmedicalhistory', inverse_name='textmedicalhistorydoc')

class medicalassistant(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    #_name = 'gestio_clinica_dental.medicalassistant'
    #_description = 'Medical assistant description'

    #personal dates
    #name = fields.Char()
    #surname1 = fields.Char()
    #surname2 = fields.Char()
    #phonenumber = fields.Char()
    #direction = fields.Text()
    #photo = fields.Image()
    ismedicalassistant = fields.Boolean()

    #profesional dates
    collegiatenumber = fields.Char()
    #items dates
    #assistantbud= fields.Many2many(comodel_name='gestio_clinica_dental.budget', relation='assistatintervention')#assistant

class treatment(models.Model):
    _name = 'gestio_clinica_dental.treatment'
    _description = 'treatment description'
    
    #basic dates
    name = fields.Char()
    description = fields.Text()
    #specificdates
    specialitytre = fields.Selection([('1','General'),('2','Surgery'),('3','Orthodontics'),('4','Endodontics'),('5','Stetic'),('6','Prosthodontist'),('7','Pediatric')])
    category = fields.Selection([('1','Primary'),('2','Secondary')])
    duration = fields.Integer()#minutes
    price = fields.Float()

    processlinetreatment = fields.Many2many(comodel_name='gestio_clinica_dental.processline', relation='treatmentline')

class quotes(models.Model):
    _name = 'gestio_clinica_dental.quotes'
    _description = 'quotes and specification intervention '
    #basic dates
    idquotes = fields.Integer()
    #datetime = fields.Datetime()
    shortdescription =fields.Char()

class medicalhistory (models.Model): 
    _name =   'gestio_clinica_dental.medicalhistory'
    _description = 'Notes for interventions in the pacient'    
    
    patientmed= fields.Char()
    dateread = DateTime()
    entry = fields.One2many(comodel_name="gestio_clinica_dental.medicalhistoryentries", inverse_name='medicalhistory')
  
class medicalhistoryentries (models.Model): 
    _name =   'gestio_clinica_dental.medicalhistoryentries'
    _description = 'Notes for interventions in the pacient'

    
    dateentry = DateTime()
    title = fields.Char()
    description = fields.Text()

    medicalhistory = fields.Many2one(comodel_name="gestio_clinica_dental.medicalhistory")

class processline(models.Model):
    _name =   'gestio_clinica_dental.processline'
    _description = 'interventions for pacient'

    idprocess = fields.Integer()
    daterealized =fields.Date()

    medical = fields.Many2many(comodel_name='gestio_clinica_dental.res.parner', relation='professionalline')
    treatment = fields.Many2many(comodel_name='gestio_clinica_dental.treatment', relation='treatmentline')

#**********************************************************************************************************
#************     WIZARDS      ****************************************************************************
#**********************************************************************************************************

class proces_wizar(models.TransientModel): #crear un proces de tractaments que tindrà un pacient(diagnostic)
    _name = "gestio_clinica_dental.proces_wizar" #ha de correspondre en el action
    name = fields.Char()
    #dades del personals----------------------------------------
    ispatient = fields.Boolean(default=TRUE)
    vat = fields.Char()
    dateborn = fields.Date()
    surname1 = fields.Char()
    surname2 = fields.Char()
    

    description = fields.Char()
    direction = fields.Char()
    city = fields.Char()
    contry_id = fields.Char()
    postal_code = fields.Integer()
    num_House = fields.Integer()

    telf = fields.Integer()
    email = fields.Char()
    
    #dades del mediques-----------------------------------------
    medicalid = fields.Integer()
    patientshortdescription = fields.Text()
    alergies = fields.Boolean()
    pregnant = fields.Boolean()
    
    #dades economiques  ----------------------------------------
    dir_factur_equal = fields.Boolean()
    direction_factur = fields.Char()
    formpay = fields.Selection([('card',"Card"),('money',"Money"),('others', "Others")])
    #dades del resum--------------------------------------------
   
    name_r = fields.Char(related='name')
    vat_r = fields.Char(related='vat')
    dateborn_r = fields.Date(related='dateborn')
    surname1_r = fields.Char(related='surname1')
    surname2_r = fields.Char(related='surname2') 
    telf_r = fields.Integer(related='telf')
    email_r = fields.Char(related='email')
    alergies_r = fields.Boolean(related='alergies')
    preganant_r = fields.Boolean(related='pregnant')



    state = fields.Selection([
        ('dades_personals', "Personal dates"),
        ('dades_mediques', "Medical dates"),  
        ('dades_facturacio', "Factur dates"),      
        ('dades_resum', "Resum dates")                                                                
        ], default='dades_personals')

   
    def action_personal(self):
        #açò és on anirà
        self.state = 'dades_mediques'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }       

                        
    def action_mediques(self):              
        self.state = 'dades_facturacio'                      
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def dades_facturacio(self):              
        self.state = 'dades_resum'                      
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
    def dades_resum(self):
       
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
                                   
    def action_validar_crear_patient(self): 
        
        patient = self.env['res.partner'].create({
        
        'name': self.name,
        'ispatient': self.ispatient,
        'vat' : self.vat,
        'dateborn' : self.dateborn,
        'medicalid' : self.medicalid,
        'patientshortdescription' : self.patientshortdescription
        })      
        
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'res_id': patient.id,
            'view_mode': 'form',
            
            'target': 'current',

            'views':[(self.env.ref('gestio_clinica_dental.patient_res_partner_form').id, "form")]
        }


    