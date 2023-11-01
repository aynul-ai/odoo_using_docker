from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval


class OdooPlayground(models.Model):
    _name = 'odoo.playground'
    _description = 'Odoo Playground'

    DEFAULT_ENV_VARIABLES = """ #Avaiable variables:
    # - self: Current Object
    # - self.env: Odoo Environment on which the action is triggered
    # - self.env.user: Retutn the current user (as an instance)
    # - self.env.is_system: Return whether the current user has group "Settings", or is in superuser mode.
    # - self.env.is_admin: Return whether the current user has group "Access Rights", or is in superuser mode.
    # - self.env.is_superuser: Return whether the current user is in superuser mode.
    # - self.env.company: Return the current user's company (as an instance)
    # - self.env.companies: Return the recordset of the enabled companies by the user
    # - self.env.lang: Return the current user's language code \n\n\n\n
    """
    model_id = fields.Many2one('ir.model', string='Model')
    code = fields.Text(string='Code', default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string='Result')

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            if self.code:
                self.result = safe_eval(self.code.strip(), {'self': model}, mode='eval')
            else:
                self.result = 'No code to execute'
        except Exception as e:
            self.result = str(e)
