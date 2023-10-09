from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_type = fields.Many2one('crm.team', 'Order type', domain=([('name', 'in', ('lazada', 'Sales'))]))
    rientation = fields.Selection([
        ('Landscape', 'Landscape'),
        ('Portrait', 'Portrait')
    ], 'Orientation', default='Landscape')
    # count_action_report = fields.Integer('Count Action Report', default=0)

    # def _check_print_count(self):
    #     if self.sudo().search([('print_count', '>=', 1)]):
    #         raise UserError(_("You cannot print this report because it is restricted from printing."))


class SaleTeam(models.Model):
    _inherit = 'crm.team'

    select_show_option = fields.Selection([
        ('sale_online', 'Sale online'),
        ('sale_offline', 'Sale offline')
    ], 'Is show select', default='')