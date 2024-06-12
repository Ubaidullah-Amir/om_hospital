# -*- coding: utf-8 -*-

import base64
import io
from odoo import models



class PatientDetailsXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_details_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, wizard):
        # Get all patient records
        patients = self.env['om_hospital.pateint'].search([])

        # Add a sheet
        sheet = workbook.add_worksheet('Patient Details')

        # Add a bold format for the headers
        bold = workbook.add_format({'bold': True})

        # Write the header row
        headers = ['Name', 'Gender', 'Age', 'Reference', 'Address', 'Date of Birth']
        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header, bold)

        # Write data rows
        row = 1
        for patient in patients:
            sheet.write(row, 0, patient.name)
            sheet.write(row, 1, patient.gender)
            sheet.write(row, 2, patient.age)
            sheet.write(row, 3, patient.ref)
            sheet.write(row, 4, patient.address)
            sheet.write(row, 5, str(patient.date_of_birth))
            row += 1


