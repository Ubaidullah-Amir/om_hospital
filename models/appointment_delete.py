from odoo import models, fields, api
from odoo.exceptions import UserError


class AppointmentDeleteWizard(models.TransientModel):
    _name = 'om_hospital.appointment_delete_wizard'
    _description = 'Delete appointment'

    appointment_id = fields.Many2one('om_hospital.appointment', string="Appointment")
    
    def delete_appointment(self):
        raise UserError("delete appointment")
    @api.model
    def default_get(self,fields):
        res = super(AppointmentDeleteWizard ,self).default_get(fields)
        res["appointment_id"] = self.env.context.get("active_id")
        return res
  



