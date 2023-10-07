from odoo import _, api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    cancel_reason = fields.Text(string='Reason', required=False)

    def action_cancel_appointment(self):
        self.appointment_id.write({'state': 'cancel'})
        print("Appointment Cancelled")
        return True