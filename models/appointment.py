from odoo import models, fields,api

class Appointment(models.Model):
    _name = 'om_hospital.appointment'
    _description = 'this is a model for appointment'
    _inherit = ["mail.thread","mail.activity.mixin"]
    ref = fields.Char(string='Ref')

    _rec_name = "ref"
    

    pateint_id = fields.Many2one("om_hospital.pateint",string="Pateint")
    appointment_time= fields.Datetime(string="Appointment Time" ,default=fields.Datetime.now)
    booking_Date= fields.Date(string="Booking Time",default=fields.Date.context_today)
    gender = fields.Selection(related="pateint_id.gender")


    @api.onchange("pateint_id")
    def onchange_patient_id(self):
        self.ref = self.pateint_id.ref
