from odoo import api, models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _prepare_purchase_order_line(
            self, product_id, product_qty, product_uom, company_id, values, po
    ):
        """Apply the discount to the created purchase order"""
        res = super()._prepare_purchase_order_line(
            product_id, product_qty, product_uom, company_id, values, po
        )
        date = None
        if po.date_order:
            date = po.date_order.date()
        seller = product_id._select_seller(
            partner_id=values["supplier"].name,
            quantity=product_qty,
            date=date,
            uom_id=product_uom,
        )
        res.update(self._prepare_purchase_order_line_from_seller(seller))
        return res

    @api.model
    def _prepare_purchase_order_line_from_seller(self, seller):
        """Overload this function to prepare other data from seller,
        like in purchase_triple_discount module"""
        if not seller:
            return {}
        return {"discount": seller.discount}