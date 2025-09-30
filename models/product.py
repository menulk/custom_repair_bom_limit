# -*- coding: utf-8 -*-
from odoo import models, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []

        if self.env.context.get("from_repair_order"):
            # Only allow products with BoMs
            args += [("bom_ids", "!=", False)]

            products = self.search(args, limit=10) 
            print("✅ Allowed repairable products:",
                  [(p.id, p.display_name) for p in products]) # type: ignore
            
        return super().name_search(name=name, args=args, operator=operator, limit=limit)
    