{
    "name": "Hospital Management",
    "version": "1.0.0",
    "author": "Md. Shihab Uddin",
    "category": "generic module",
    "description": """
    Hospital Management
    """,
    "depends": [
        'mail', 'product', 'sale',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/patient.tag.csv',
        'data/patient_tag_data.xml',
        'data/patient_sequence.xml',
        'wizard/cancel_appointment.xml',
        'views/sale_order_inherit.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/patient_tag_view.xml',
        'views/odoo_playground_view.xml',
        'views/res_config_settings_view.xml',
        'views/menu.xml',
    ],
    "sequence": -1,
    "demo_xml": [],
    "installable": True,
    "application": True,
    "license": "AGPL-3",
}
