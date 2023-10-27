from odoo import models, fields


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Tags for patients'

    name = fields.Char(string='Tag Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color')
    color_2 = fields.Char(string='Color 2')
    sequence = fields.Integer()

    _sql_constraints = [
        ("unique_tag_name", "UNIQUE (name)", "Tag name must be unique."),
        ("check_sequence", "Check ( sequence > 0 )","Sequence must be non zero positive number.")
    ]

