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
        'views/patient.xml',
        'views/appointment.xml',
        'views/menu.xml',
    ],
    "sequence": -1,
    "demo_xml": [],
    "installable": True,
    "application": True,
    "license": "AGPL-3",
}
