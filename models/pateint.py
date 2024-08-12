from odoo import models, fields,api
from datetime import date
from odoo.exceptions import UserError,ValidationError

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
    is_birthday = fields.Boolean("Is_Birthday",default=False,compute="_compute_birthday")

    
    active = fields.Boolean(string='Active',default=True) # use to archeive and unarcheive

    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string='Age',compute="_compute_age",tracking=True)

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for rec in self:
            if rec["date_of_birth"] and rec["date_of_birth"] > fields.Date.today():
                raise ValidationError("Please select the valid date of birth")
                
    def _compute_birthday(self):
        for rec in self:
            today_date = date.today()
            if rec.date_of_birth:
                if rec.date_of_birth.month == today_date.month and rec.date_of_birth.day == today_date.day:
                    rec.is_birthday = True
                else:
                    rec.is_birthday = False
            else:
                rec.is_birthday = False
            
    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age
    @api.model
    def test_cron_job(self):
        pass

    def get_table_definition(self):
        # This is an example method. Adjust as needed for your use case.
        columns = self._fields
        table_definition = {field: columns[field].type for field in columns}
        return table_definition

    def action_test(self):
        value = self.get_table_definition()
        raise UserError("Table definition: %s" % value)
    @api.model
    def name_create(self,name):
        # raise UserError(name)
        return self.create({"ref":name,"name":name}).name_get()[0]
    
    def action_edit_patient(self):
        self.ensure_one()  # Ensure the method is called on a single record
        return {
            'type': 'ir.actions.act_window',
            'name': 'Edit Patient',
            'res_model': 'om_hospital.pateint',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }