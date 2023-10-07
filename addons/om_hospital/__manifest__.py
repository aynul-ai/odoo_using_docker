{
    "name": "Hospital Management",
    "version": "1.0.0",
    "author": "Md. Shihab Uddin",
    "category": "generic module",
    "description": """
    Hospital Management
    """,
    "depends": [
        'mail', 'product',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'wizard/cancel_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/patient_tag_view.xml',
        'views/menu.xml',
    ],
    "sequence": -1,
    "demo_xml": [],
    "installable": True,
    "application": True,
    "license": "AGPL-3",
}
