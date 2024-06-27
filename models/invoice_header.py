from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    x_text_top = fields.Html(string='Custom Header Text')

    def _get_invoice_number_for_print(self):
        return self.name or ''

class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        try:
            if report_ref == 'account.report_invoice_with_payments':
                data = data or {}
                context = data.get('context', {})
                context['show_invoice_number_on_all_pages'] = True
                if res_ids:
                    invoice = self.env['account.move'].browse(res_ids[0])
                    invoice_number = invoice._get_invoice_number_for_print()
                    if invoice_number:
                        context['invoice_number'] = invoice_number
                data['context'] = context
            result = super(IrActionsReport, self)._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
            return result
        except Exception as e:
            raise UserError(f"Det uppstod ett fel vid generering av fakturan: {str(e)}")

    def _get_report_from_name(self, report_name):
        return super(IrActionsReport, self)._get_report_from_name(report_name)
    