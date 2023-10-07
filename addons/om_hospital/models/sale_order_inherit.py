from odoo import _, api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    test = fields.Boolean(string="Test")
    confirm_user_id = fields.Many2one('res.users', string="Confirm User")


    def test_function(self):
        print("Hello World")
        return True