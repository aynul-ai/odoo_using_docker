# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_days = fields.Integer(string="Cancel Days", config_parameter="om_hospital.cancel_days")
    # config_parameter is the key of the field in the database
    # it will create a value in ir.config_parameter table
