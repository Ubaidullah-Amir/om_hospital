from odoo import models,fields

class HospitalDoctor(models.Model):
    _name = "om_hospital.doctor"
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    
    department_ids = fields.Many2many('om_hospital.department', string='Departments')
