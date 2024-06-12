from odoo import models, fields

class PatientReportWizard(models.TransientModel):
    _name = 'om_hospital.patient.report.wizard'
    _description = 'Print Patient Wizard'

    def action_print_report(self):
        return self.env.ref('om_hospital.report_patient_details_xls').report_action(self)

