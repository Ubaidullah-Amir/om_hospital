from odoo import models, fields

class HospitalDepartment(models.Model):
    _name = "om_hospital.department"
    _description = "Hospital Department"

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')  # Color field to store hex color codes
    doctors_ids = fields.Many2many('om_hospital.doctor', string='Doctors')
    reference_record = fields.Reference([("om_hospital.pateint","Patient"),("om_hospital.appointment","Appointment")],string="Record")

