from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'

    name = fields.Char(string='Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    age = fields.Integer(string='Age', tracking=True, compute='_compute_age',
                         help="Computed field(non stored) cannot be used in search view")
    gender = fields.Selection([
        ("male", "Male"), ("female", "Female")])
    ref = fields.Char(string='Reference')
    active = fields.Boolean(string='Active', default=True)
    image = fields.Binary(string='Image')
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count", store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.constrains('date_of_birth')
    def check_date_of_birth(self):
        for rec in self:
           if rec.date_of_birth > fields.date.today():
               raise ValidationError("Birthday is not acceptable")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = fields.Date.today().year - rec.date_of_birth.year
            else:
                rec.age = 0  # else is mendatory from odoo 14

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code(
            'hospital.patient.sequence') or 'New'
        res = super(HospitalPatient, self).create(vals)
        return res

    def write(self, vals):
        if not self.ref:
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.sequence') or 'New'
        res = super(HospitalPatient, self).write(vals)
        return res

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.ref, rec.name)))
        return res