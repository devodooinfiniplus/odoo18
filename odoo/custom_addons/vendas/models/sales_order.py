from odoo import models, fields

class SalesOrder(models.Model):
    _inherit = "sale.order"

    short_note = fields.Char(string='Short Note')