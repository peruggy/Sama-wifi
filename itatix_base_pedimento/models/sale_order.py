from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def _default_lot_ids(self):
        if self.product_id:
            lot_id = self.env['stock.production.lot'].search([('product_id', '=', self.product_id.id), ('import_document', '!=', False)])
            if not lot_id:
                return {'domain': {'lot_id': [('id', '=', [])]}}
            res = {'domain': {'lot_id': [('id', 'in', lot_id.ids)]}}
            return res
    lot_id = fields.Many2one(
        'stock.production.lot', 'Lot/Serial Number',
        domain="[('product_id', '=', product_id), ('company_id', '=', company_id)]", check_company=True,
        help="Lot/Serial Number of the product to unbuild.", copy=False)

    # Esto solo funciona para un solo ID, salvo que el requerimiento sea que sean multi tags (ManyToMany)
    # def _prepare_invoice_line(self, **optional_values):
    #     res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
    #     res['lot_id'] = self.lot_id.id or False
    #     return res