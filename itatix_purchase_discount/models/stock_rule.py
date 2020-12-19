from odoo import api, models


class StockRule(models.Model):
    _inherit = "stock.rule"

    @api.model
    def _prepare_purchase_order_line_from_seller(self, seller):
        if not seller:
            return {}
        return {"discount": seller.discount}
