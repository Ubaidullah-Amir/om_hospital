from odoo import models, fields,api,_
from odoo.exceptions import UserError
class Appointment(models.Model):
    _name = 'om_hospital.appointment'
    _description = 'this is a model for appointment'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _order = "id desc"
    ref = fields.Char(string='Ref',help="Reference to patient's ref")

    prescription = fields.Html(string='Prescription')

    _rec_name = "sequence_number"

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority") # from mrp model
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled ')],required=True,default= "draft", string="Status") # status bar for appointment status 
    

    age = fields.Integer(string='Age', related='pateint_id.age', tracking=True, store=True)
    doctor_id = fields.Many2one('om_hospital.doctor', string="Doctor")
    note = fields.Text(string='Description')
    
    pateint_id = fields.Many2one("om_hospital.pateint",string="Pateint",required=True)
    appointment_time= fields.Datetime(string="Appointment Time" ,default=fields.Datetime.now)
    booking_Date= fields.Date(string="Booking Time",default=fields.Date.context_today)
    gender = fields.Selection(related="pateint_id.gender")

    sequence_number = fields.Char(string='Sequence', required=True, copy=False, readonly=True, default=lambda self: _('New'))

    # @api.model
    # def create(self, vals):
    #     if vals.get('sequence_number', _('New')) == _('New') and self.state == "done":
    #         vals['sequence_number'] = self.env['ir.sequence'].next_by_code('om_hospital.appointment') or _('New')
    #     return super(Appointment, self).create(vals)
    
    def write(self, vals):
        if  self.sequence_number == _('New') and (self.state == "done" or vals.get('state', "none") =="done") :
            vals['sequence_number'] = self.env['ir.sequence'].next_by_code('om_hospital.appointment') or _('New')
        return super(Appointment, self).write(vals)

    @api.onchange("pateint_id")
    def onchange_patient_id(self):
        self.ref = self.pateint_id.ref

    def method_name(self):
       
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Click Successful",
                'type': 'rainbow_man',
            }
        }
    
    def action_make_appointment_done(self):
        self.state = 'done'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Click Successful",
                'type': 'rainbow_man',
            }
        }
    
    def action_create_appointment(self):
        self.state = 'in_consultation'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Click Successful",
                'type': 'rainbow_man',
            }
        }
    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_delete_appointment(self):

        self.ensure_one()  # Ensure the method is called on a single record
        action = {
            'type': 'ir.actions.act_window',
            'name': 'Appointment Delete',
            'res_model': 'om_hospital.appointment_delete_wizard',
            'view_mode': 'form',
            'target': 'new',
        #     'context': {
        #     'default_appointment_id': self.id,
        # },
        }
        return action
    
