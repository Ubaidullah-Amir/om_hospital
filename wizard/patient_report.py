from odoo import models, fields

class PatientReportWizard(models.TransientModel):
    _name = 'om_hospital.patient.report.wizard'
    _description = 'Print Patient Wizard'

    def action_print_report(self):

        # Fetch all patient records
        patients = self.env['om_hospital.pateint'].search([])
        patient_data = []
        for patient in patients:
            patient_data.append({
                'name': patient.name,
                'gender': patient.gender,
                'age': patient.age,
                'ref': patient.ref,
                'address': patient.address,
                'date_of_birth': str(patient.date_of_birth),
            })
        
        # Pass the fetched data to the report
        data = {
            'patients': patient_data,
        }
        return self.env.ref('om_hospital.report_patient_details_xls').report_action(self, data=data)
