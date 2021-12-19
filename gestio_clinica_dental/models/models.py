# -*- coding: utf-8 -*-

from datetime import time
from re import match
from odoo import models, fields, api

# *************************************************************************************   
# PEOPLE DATES
# *************************************************************************************  

class Pacient(models.Model):
    _name = 'gestio_clinica_dental.Pacient'
    _description = 'All information from pacient'

    #personal dates
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()
    years = fields.Integer()
    photo = fields.Image()

    #medical dates
    medicalid = fields.Integer()
    pacientshortdescription = fields.Text()
    salutformulary = fields.Many2many(comodel_name='gestio_clinica_dental.Salutformulary', relation='formclinic')#restric to one
    #anamnesis = fields.Many2many()#restric to one
    medicalstory = fields.Many2many(comodel_name='gestio_clinica_dental.Medicalhistory', relation='medicalhistoryonepatient')#restric to one
    doctorpac = fields.Many2many(comodel_name='gestio_clinica_dental.Doctor', relation='doctorpatientassigned')

    #economicdates
    budgetpac = fields.Many2one(comodel_name='gestio_clinica_dental.Pacient')
    paysstatus = fields.Selection([("1","No pay", ("2","Parcial pay"), ("3","Finalized"))])

    #schedule dates
    quotes = fields.Many2one(comodel_name='gestio_clinica_dental.Quotes', relation='quotesagendfrompatient')
    status = fields.Selection([("1","Advised", ("2","Inside cabinet"), ("3","Finalized"), ("4","Other"))])

    #others
    afterimg = fields.Image()
    beforeimg = fields.Image()


class Doctor (models.Model):
    _name = 'gestio_clinica_dental.Doctor'
    _description = 'Doctor description'
    #personal dates
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    phonenumber = fields.Char()
    direction = fields.Text()

    #profesional dates
    collegiatenumber = fields.Char()
    specialitydoc = fields.Selection([('1','General'),('2','Surgery'),('3','Orthodontics'),('4','Endodontics'),('5','Stetic'),('6','Prosthodontist'),('7','Pediatric')])
    
    #items dates
    pacientsintervened = fields.Many2many(comodel_name='gestio_clinica_dental.Patient', relation='doctorpatientassigned')
    quotesdoc = fields.Many2many(comodel_name='gestio_clinica_dental.Quotes', relation='doctorfrompatient')
    doctorscheduledoc = fields.Many2many(comodel_name='gestio_clinica_dental.Doctor', relation='doctorschedule')
    


class Medicalassistant (models.Model):
    _name = 'gestio_clinica_dental.Medicalassistant'
    _description = 'Medical assistant description'

    #personal dates
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    phonenumber = fields.Char()
    direction = fields.Text()

    #profesional dates
    collegiatenumber = fields.Char()

    assistantbud= fields.Many2many(comodel_name='gestio_clinica_dental.Budget', relation='assistatintervention')#assistant



# *************************************************************************************   
# MEDICAL DOCUMENTATION DATES
# *************************************************************************************   
 
class Salutformulary(models.Model):
    _name = 'gestio_clinica_dental.Salutformulary'
    _description = 'The pacient write this obligatorily'

    idform = fields.Integer()
    alergiesbool = fields.Boolean()                 #obligatory
    alergies = fields.Char()                        #obligatory 
    diseasesbool = fields.Boolean()                 #obligatory
    diseases = fields.Char()                        #obligatory
    afterdentalproblemsbool = fields.Boolean()
    afterdentalproblems = fields.Char()

    pacientssal = fields.Many2many(comodel_name='gestio_clinica_dental.Patient', relation='formclinic')#restric to one

class Consent(models.Model):
    _name = 'gestio_clinica_dental.Consent'
    _description = 'The pacient write this obligatorily and is unic for treatment'

    idform = fields.Integer()
    title = fields.Char()                 #obligatory
    text = fields.Text()                  #obligatory 
    youconsent = fields.Boolean()         #obligatory

    treatmentcon = fields.Many2many(comodel_name='gestio_clinica_dental.Treatment', relation='consentsd')     #restric to one
    


class Medicalhistory (models.Model):
    _name = 'gestio_clinica_dental.Medicalstory'
    _description = 'Important regist medical'

    pacientmed =fields.Many2many(comodel_name='gestio_clinica_dental.Patient', relation='medicalhistoryonepatient')#restric to one
    textmed = fields.One2many(comodel_name='gestio_clinica_dental.Textmedicalhistory', inverse_name='textwritemed')


class Textmedicalhistory (models.Model):
    _name = 'gestio_clinica_dental.Textmedicalhistory'
    _description = 'Text inside in the medical history and write from the doctor'

    insertiondate = fields.Date()
    shortdecriptionmedicalh = fields.Char()
    longdescriptionmedicalh = fields.Text()
    textwritemed = fields.Many2one(comodel_name='gestio_clinica_dental.Medicalhistory')


# *************************************************************************************   
# SCHEDULE DATES
# ************************************************************************************* 

class Principalschedule (models.Model):
    _name = 'gestio_clinica_dental.Principalschedule'
    _description = 'Organization pacients '

    hours = fields.Datetime()

    quotes = fields.Many2many(comodel_name='gestio_clinica_dental.Doctor', relation='doctorfrompatient')#quotes
    doctorsinside = fields.Many2many(comodel_name='gestio_clinica_dental.Doctor', relation='doctorschedule')#doctor

class Quotes (models.Model):
    _name = 'gestio_clinica_dental.Quotes'
    _description = 'Quotes and specification intervention '

    time = fields.time()
    doctor = fields.Many2many(comodel_name='gestio_clinica_dental.Doctor', relation='doctorfrompatient')#doctor
    patient = fields.Many2one(comodel_name='gestio_clinica_dental.Patient', relation='quotesagendfrompatient')#patient 
    


# *************************************************************************************   
# MEDICAL DATES
# *************************************************************************************

class Treatment (models.Model):
    _name = 'gestio_clinica_dental.Treatment'
    _description = 'Treatment description'

    name = fields.Char()
    description = fields.Text()

    specialitytre = fields.Selection([('1','General'),('2','Surgery'),('3','Orthodontics'),('4','Endodontics'),('5','Stetic'),('6','Prosthodontist'),('7','Pediatric')])
    category = fields.Selection([('1','Primary'),('2','Secondary')])

    duration = fields.time()
    price = fields.Float()

    tratmenttra = fields.Many2many(comodel_name='gestio_clinica_dental.Treatment', relation='Treatment2category')
    budgettre = fields.Many2many(comodel_name='gestio_clinica_dental.Budgettre', relation='TreatmentBudget')
    Laboratorytra = fields.Many2many(comodel_name='gestio_clinica_dental.Laboratory', relation='Tratment <-> laboratory')




# *************************************************************************************   
# FINANCES DATES
# ************************************************************************************* 
class Budget (models.Model):
    _name = 'gestio_clinica_dental.Budget'
    _description = 'Intervention type'

    idbudget = fields.Integer()
    anotations = fields.Text()
    logoimg = fields.Image()

    pacientbud = fields.One2many(comodel_name='gestio_clinica_dental.Pacient', inverse_name='budgetpac')#pacient
    
    assistantmake = fields.Many2many(comodel_name='gestio_clinica_dental.Medicalassistant', relation='assistatintervention')#assistant
    makedate = fields.Datetime()
   
    treatmentquo = fields.Many2many(comodel_name='gestio_clinica_dental.Treatment', relation='TreatmentBudget')
    duration    = fields.time()

    pricetotal = fields.Float()#computed
    methotpay = fields.Selection([('1','full pay'), ('2','financed'), ('3','Make & pay'), ('4','Other')])
    discountmanual = fields.Float()
    totalprice = fields.Float()#2compute total and discount methot pay



# *************************************************************************************   
# OTHERS DATES
# ************************************************************************************* 


class Laboratory (models.Model):
    _name = 'gestio_clinica_dental.Textmedicalhistory'
    _description = 'Text inside in the medical history and write from the doctor'

    name = fields.Char()
    description = fields.Char()
    phone1 = fields.Char()
    phone2 = fields.Char()

    speciaity = fields.Selection([('1','Stetic'),('2','Funcionality'),('3','All modalities')])
    timeproduction = fields.Integer()
    treatmentlab = fields.Many2many(comodel_name='gestio_clinica_dental.Laboratorytra', relation='Tratment <-> laboratory')