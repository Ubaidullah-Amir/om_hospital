{
    'name': 'Hospital management',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module used for management of treating patient',
    'author': 'Odolution',
    'license': 'LGPL-3',
    'sequence': '-100',
    'depends': ["mail"],
    'demo': [],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/pateint_view.xml",
        "views/female_pateint_view.xml",
        "views/appointment_view.xml"
        ],
    'images': ['images/1.PNG', 'images/2.PNG', 'images/3.PNG','images/4.PNG','static/description/icon.png'],
    'installable': True,
    'application': True,
}
