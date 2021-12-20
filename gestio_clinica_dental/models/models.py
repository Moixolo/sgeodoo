# -*- coding: utf-8 -*-

from datetime import time
from re import match
from xmlrpc.client import DateTime
from odoo import models, fields, api

# *************************************************************************************   
# PEOPLE DATES
# *************************************************************************************  


class patient(models.Model):
    _name = 'gestio_clinica_dental.patient'
    _description = 'All information from patient'

    #personal dates
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()
    years = fields.Integer()
    photo = fields.Image()

    #medical dates
    medicalid = fields.Integer()
    patientshortdescription = fields.Text()
    salutformulary = fields.Many2many(comodel_name='gestio_clinica_dental.salutformulary', relation='formclinic')#restric to one
    #anamnesispat = fields.Many2many(comodel_name="gestio_clinica_dental.anamnesis",relation='anampatient')#restric to one
    medicalstory = fields.Many2many(comodel_name='gestio_clinica_dental.medicalhistory', relation='medicalhistoryonepatient')#restric to one
    doctorpac = fields.Many2many(comodel_name='gestio_clinica_dental.doctor', relation='doctorpatientassigned')

    #economicdates
    patientbud = fields.Many2one(comodel_name='gestio_clinica_dental.budget')
    paysstatus = fields.Selection([("1","No pay"), ("2","Parcial pay"), ("3","Finalized")])

    #schedule dates
    quotes = fields.Many2one(comodel_name='gestio_clinica_dental.quotes', relation='quotesagendfrompatient')
    status = fields.Selection([("1","Advised"), ("2","Inside cabinet"), ("3","Finalized"), ("4","Other")])

    #others
    afterimg = fields.Image()
    beforeimg = fields.Image()


class doctor (models.Model):
    _name = 'gestio_clinica_dental.doctor'
    _description = 'doctor description'
    #personal dates
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    phonenumber = fields.Char()
    direction = fields.Text()
    
    
    #profesional dates
    collegiatenumber = fields.Char()
    specialitydoc = fields.Selection([('1','General'),('2','Surgery'),('3','Orthodontics'),('4','Endodontics'),('5','Stetic'),('6','Prosthodontist'),('7','Pediatric')])
    #forenkeys
    #items dates 
    patientsintervened = fields.Many2many(comodel_name='gestio_clinica_dental.patient', relation='doctorpatientassigned')
    doctorsch = fields.Many2many(comodel_name='gestio_clinica_dental.principalschedule', relation='doctorschedule')
    


class medicalassistant (models.Model):
    _name = 'gestio_clinica_dental.medicalassistant'
    _description = 'Medical assistant description'

    #personal dates
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    phonenumber = fields.Char()
    direction = fields.Text()

    #profesional dates
    collegiatenumber = fields.Char()
    #items dates
    assistantbud= fields.Many2many(comodel_name='gestio_clinica_dental.budget', relation='assistatintervention')#assistant



# *************************************************************************************   
# MEDICAL DOCUMENTATION DATES
# *************************************************************************************   
 
class salutformulary(models.Model):
    _name = 'gestio_clinica_dental.salutformulary'
    _description = 'The patient write this obligatorily'
    #basic dates
    idform = fields.Integer()
    alergiesbool = fields.Boolean()                 #obligatory
    alergies = fields.Char()                        #obligatory 
    diseasesbool = fields.Boolean()                 #obligatory
    diseases = fields.Char()                        #obligatory
    afterdentalproblemsbool = fields.Boolean()
    afterdentalproblems = fields.Char()
    #forenkeys
    patientssal = fields.Many2many(comodel_name='gestio_clinica_dental.patient', relation='formclinic')#restric to one

class consent(models.Model):
    _name = 'gestio_clinica_dental.consent'
    _description = 'The patient write this obligatorily and is unic for treatment'
    #basic dates
    idform = fields.Integer()
    title = fields.Char()                 #obligatory
    text = fields.Text()                  #obligatory 
    youconsent = fields.Boolean()         #obligatory
    #forenkeys
    treatmentcon = fields.Many2many(comodel_name='gestio_clinica_dental.treatment', relation='consentsd')     #restric to one

class anamnesis(models.Model):
    _name = 'gestio_clinica_dental.anamnesis'
    _description = 'All information from the patient'
    #basic dates
    idform = fields.Integer()
    alergiesbool = fields.Boolean()                 #obligatory
    alergies = fields.Char()                        #obligatory 
    diseasesbool = fields.Boolean()                 #obligatory
    diseases = fields.Char()                        #obligatory

    #patientana = fields.Many2many(comodel_name="gestio_clinica_dental.patient", relation='anampatient')#restric to one


class medicalhistory (models.Model):
    _name = 'gestio_clinica_dental.medicalhistory'
    _description = 'Important regist medical'
    #basic dates
    datecreated = DateTime()
    #forenkeys
    patientmed =fields.Many2many(comodel_name='gestio_clinica_dental.patient', relation='medicalhistoryonepatient')#restric to one
    textmed = fields.One2many(comodel_name='gestio_clinica_dental.textmedicalhistory', inverse_name='textwritemed')

class textmedicalhistory (models.Model):
    _name = 'gestio_clinica_dental.textmedicalhistory'
    _description = 'Text inside in the medical history and write from the doctor'
    #basic dates
    datewrited = fields.Datetime()
    insertiondate = fields.Date()
    shortdecriptionmedicalh = fields.Char()
    longdescriptionmedicalh = fields.Text()
    #forenkeys
    textwritemed = fields.Many2one(comodel_name='gestio_clinica_dental.medicalhistory')   




# *************************************************************************************   
# SCHEDULE DATES
# ************************************************************************************* 

class principalschedule (models.Model):
    _name = 'gestio_clinica_dental.principalschedule'
    _description = 'Organization patients '
    #basic dates
    hours = fields.Datetime()
    #forenkeys
    principalschedulequo = fields.Many2many(comodel_name='gestio_clinica_dental.quotes', relation='quotesschedule')#quotes
    principalscheduledoc = fields.Many2many(comodel_name='gestio_clinica_dental.doctor', relation='doctorschedule')#doctor

class quotes (models.Model):
    _name = 'gestio_clinica_dental.quotes'
    _description = 'quotes and specification intervention '
    #basic dates
    idquotes = fields.Integer()
    datetime = fields.Datetime()
    #forenkeys
    quotespat = fields.Many2one(comodel_name='gestio_clinica_dental.patient', relation='quotesagendfrompatient')#patient 
    quotespri = fields.Many2many(comodel_name='gestio_clinica_dental.principalschedule', relation='quotesschedule')#quotes


# *************************************************************************************   
# MEDICAL DATES
# *************************************************************************************

class treatment (models.Model):
    _name = 'gestio_clinica_dental.treatment'
    _description = 'treatment description'
    #basic dates
    name = fields.Char()
    description = fields.Text()
    #specificdates
    specialitytre = fields.Selection([('1','General'),('2','Surgery'),('3','Orthodontics'),('4','Endodontics'),('5','Stetic'),('6','Prosthodontist'),('7','Pediatric')])
    category = fields.Selection([('1','Primary'),('2','Secondary')])
    duration = fields.time()
    price = fields.Float()
    #forenkeys

    #tratmenttra = fields.Many2many(comodel_name='gestio_clinica_dental.treatment', relation='treatment2category')
    tratmentcons = fields.Many2many(comodel_name='gestio_clinica_dental.consent', relation='treatmentconsent')
    treatmentbud = fields.Many2many(comodel_name='gestio_clinica_dental.budget', relation='budgettreatment')
    treatmentlab = fields.Many2many(comodel_name='gestio_clinica_dental.laboratory', relation='Tratmentlaboratory')




# *************************************************************************************   
# FINANCES DATES
# ************************************************************************************* 
class budget (models.Model):
    _name = 'gestio_clinica_dental.budget'
    _description = 'Intervention type'
    #basic dates
    idbudget = fields.Integer()
    anotations = fields.Text()
    logoimg = fields.Image()
    makedate = fields.Datetime()
    #specific dates
    duration    = fields.time()
    methotpay = fields.Selection([('1','full pay'), ('2','financed'), ('3','Make & pay'), ('4','Other')])
    discountmanual = fields.Float()
    totalprice = fields.Float()#2compute total and discount methot pay
    #forenkeys
    budgettre = fields.Many2many(comodel_name='gestio_clinica_dental.treatment', relation='budgettreatment')#patient
    budgetpat = fields.One2many(comodel_name="gestio_clinica_dental.patient", inverse_name="patientbud")
    assistantmake = fields.Many2many(comodel_name='gestio_clinica_dental.medicalassistant', relation='assistatintervention')#assistant

# *************************************************************************************   
# OTHERS DATES
# ************************************************************************************* 


class laboratory (models.Model):
    _name = 'gestio_clinica_dental.laboratory'
    _description = 'Text inside in the medical history and write from the doctor'
    #basic dates
    name = fields.Char()
    description = fields.Char()
    phone1 = fields.Char()
    phone2 = fields.Char()
    #specific dates
    speciaity = fields.Selection([('1','Stetic'),('2','Funcionality'),('3','All modalities')])
    timeproduction = fields.Integer()
    #forenkeys
    laboratorytre = fields.Many2many(comodel_name='gestio_clinica_dental.treatment', relation='Tratmentlaboratory')


# *************************************************************************************   
# ADITIONAL TABLES FROM MANY2MANY
# ************************************************************************************* 

