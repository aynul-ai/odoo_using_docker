from odoo import models, fields, api, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ("male", "Male"), ("female", "Female")])
    ref = fields.Char(string='Reference', required=False)
    active = fields.Boolean(string='Active', default=True)
