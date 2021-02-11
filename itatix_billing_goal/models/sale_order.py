from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    billing_goal = fields.Float(related='user_id.billing_goal', group_operator="avg", store=True)