from odoo import _, api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    test = fields.Boolean(string="Test")


    def test_function(self):
        print("Hello World")
        return True