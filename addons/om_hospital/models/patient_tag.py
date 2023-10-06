from odoo import models, fields

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Tags for patients'

    name = fields.Char(string='Tag Name', required=True)
    active = fields.Boolean(string='Active', default=True)
