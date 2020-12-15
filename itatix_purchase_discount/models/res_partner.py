from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    default_supplierinfo_discount = fields.Float(
        string="Descuento por defecto de proveedor",
        digits="Discount",
    )
