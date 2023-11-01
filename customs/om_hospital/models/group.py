from odoo import fields, models, api


class GroupInherit(models.Model):
    _inherit = 'res.groups'

    def get_application_groups(self, domain):
        group_to_hide = []
        # group_id = self.env.ref('project.group_project_task_dependencies').id
        # group_to_hide.append(group_id)
        # wave_group_id = self.env.ref('stock.group_stock_picking_eave.id')
        # group_to_hide.append(wave_group_id)

        return super(GroupInherit, self).get_application_groups(domain + [('id', 'not in', group_to_hide)])
