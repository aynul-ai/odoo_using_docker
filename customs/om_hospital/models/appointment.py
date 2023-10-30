from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Appointment Record"
    _rec_name = "patient_id"

    patient_id = fields.Many2one(
        comodel_name='hospital.patient', string='Patient', required=True, ondelete='cascade')
    patient_gender = fields.Selection(related='patient_id.gender', readonly=False,
                                      help="non readonly can effect parent model")  # non readonly can effect parent model
    appointment_time = fields.Datetime(
        string='Appointment Time', required=True, default=fields.Datetime.now)
    booking_date = fields.Date(
        string='Booking Date', required=True, default=fields.Date.today)
    ref = fields.Char(string='Reference', required=False,
                      help="Reference of the patient")
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection(
        [('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'Very High')], string='Priority')
    doctor_id = fields.Many2one(
        comodel_name='res.users', string='Doctor')

    hide_sales_price = fields.Boolean(string='Hide Sales Price')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    pharmacy_line_ids = fields.One2many(
        'appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def object_test(self):
        # rainbow effect
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Click Successfull",
                'type': 'rainbow_man',
            }
        }

    def cancel_appointment_action(self):
        # ONE WAY

        # return {
        #     'name': _('Cancel Appointment'),
        #     'view_mode': 'form',
        #     'res_model': 'cancel.appointment.wizard',
        #     'target': 'new',
        #     'context': {'default_appointment_id': self.id}
        # }

        # SECOND WAY

        action = self.env.ref("om_hospital.cancel_appointment_wizard_action").read()[0]
        return action

    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError("You cannot delete a done appointment")
        return super(HospitalAppointment, self).unlink()

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_days')
        days_before_cancel = self.booking_date - fields.date.today()
        print(type(days_before_cancel.days))
        print(days_before_cancel.days)
        if days_before_cancel.days >= int(cancel_day):
            self.state = 'cancel'
        else:
            raise ValidationError(f'Cannot cancel {cancel_day} days before booking')

    def action_draft(self):
        self.state = 'draft'

    def action_in_consultation(self):
        if self.state == 'draft':
            self.state = 'in_consultation'


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    appointment_id = fields.Many2one(
        comodel_name='hospital.appointment', string='Appointment')
    product_id = fields.Many2one(
        comodel_name='product.product', string='Product', required=True)
    product_qty = fields.Integer(string='Quantity', default=1)
    price_unit = fields.Float(
        string='Unit Price', related='product_id.list_price')
