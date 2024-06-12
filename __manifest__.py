{
    'name': 'Hospital management',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module used for management of treating patient',
    'author': 'Odolution',
    'license': 'LGPL-3',
    'sequence': '-100',
    'depends': ["mail",
                "report_xlsx"
                ],
    'demo': [],
    'data': [
        "security/ir.model.access.csv",
        "data/cron.xml",
        "wizard/patient_report_view.xml",
        "views/menu.xml",
        "views/pateint_view.xml",
        "views/female_pateint_view.xml",
        "views/appointment_view.xml",
        "views/doctor_view.xml",
        "report/patient_card.xml",
        "report/patient_details_template.xml",
        "report/report.xml"
        ],
    'images': ['images/1.PNG', 'images/2.PNG', 'images/3.PNG','images/4.PNG','static/description/icon.png'],
    'installable': True,
    'application': True,
}
