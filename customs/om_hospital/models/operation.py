from odoo import fields, models, api


class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _log_access = False

    name = fields.Many2one('res.users', string="Doctor")

