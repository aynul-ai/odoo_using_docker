from odoo import fields, models, api


class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _log_access = False

    doctor_id = fields.Many2one('res.users', string="Doctor")
    operation_name = fields.Char(string="Operation Name")


    @api.model
    def name_create(self, name):
        return self.create({
            'operation_name': name
        }).name_get()[0]



