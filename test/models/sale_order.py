from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_type = fields.Many2one('crm.team', 'Order type', domain=([('name', 'in', ('lazada', 'Sales'))]))
    rientation = fields.Selection([
        ('Landscape', 'Landscape'),
        ('Portrait', 'Portrait')
    ], 'Orientation', default='Landscape')


class SaleTeam(models.Model):
    _inherit = 'crm.team'

    select_show_option = fields.Selection([
        ('sale_online', 'Sale online'),
        ('sale_offline', 'Sale offline')
    ], 'Is show select', default='')