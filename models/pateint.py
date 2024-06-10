from odoo import models, fields,api
from datetime import date
class Pateint(models.Model):
    _name = 'om_hospital.pateint'
    _description = 'this is a model for pateint'
    _inherit = ["mail.thread","mail.activity.mixin"]
    name = fields.Char(string='Name', required=True,tracking=True)
    ref = fields.Char(string='Ref',tracking=True,default="odoo mates")
    address = fields.Text(string='Address')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender',default="female")
    image = fields.Binary(string= "Patient Image")
    appointment_ids = fields.One2many("om_hospital.appointment", "pateint_id", string="Appointment")


    
    active = fields.Boolean(string='Active',default=True) # use to archeive and unarcheive

    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string='Age',compute="_compute_age",tracking=True)
    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age