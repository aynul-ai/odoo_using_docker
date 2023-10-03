from odoo import _, api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Appointment Record"

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient', required=True)
