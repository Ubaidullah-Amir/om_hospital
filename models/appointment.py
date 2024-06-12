from odoo import models, fields,api

class Appointment(models.Model):
    _name = 'om_hospital.appointment'
    _description = 'this is a model for appointment'
    _inherit = ["mail.thread","mail.activity.mixin"]
    ref = fields.Char(string='Ref',help="Reference to patient's ref")

    prescription = fields.Html(string='Prescription')

    _rec_name = "ref"

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
    
    pateint_id = fields.Many2one("om_hospital.pateint",string="Pateint")
    appointment_time= fields.Datetime(string="Appointment Time" ,default=fields.Datetime.now)
    booking_Date= fields.Date(string="Booking Time",default=fields.Date.context_today)
    gender = fields.Selection(related="pateint_id.gender")


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

    
