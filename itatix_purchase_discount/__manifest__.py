{
    "name": "Purchase order lines with discounts",
    "author": "ITATIX SA DE CV, "
    "Odoo Community Association (OCA)",
    "version": "13.0.0.0.2",
    "category": "Purchase Management",
    "depends": ["purchase_stock", "sale"],
    "data": [
        "views/purchase_discount_view.xml",
        "views/report_purchaseorder.xml",
        "views/product_supplierinfo_view.xml",
        "views/res_partner_view.xml",
        "views/sale_order_view.xml"
    ],
    "license": "AGPL-3",
    "installable": True,
}
