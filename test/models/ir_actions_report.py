from odoo import models, fields


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    user_print_id = fields.Many2one('res.users', 'User For Print')
    print_count = fields.Integer('Count For Print', default=0)

    def _render_qweb_pdf_prepare_streams(self, report_ref, data, res_ids=None):
        res = super()._render_qweb_pdf_prepare_streams(report_ref, data, res_ids=res_ids)
        if self._get_report(report_ref).report_name == 'sale.report_saleorder':
            self._get_report(report_ref).user_print_id = self._get_report(report_ref).model_id.env.uid
            self._get_report(report_ref).print_count += 1
        return res
