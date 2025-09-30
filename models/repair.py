# -*- coding: utf-8 -*-
from odoo import models, api

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    @api.onchange('product_id')
    def _onchange_product_id_set_context(self):
        global current_bom_line_product_ids

        if self.product_id: # type: ignore
            print(f"🔹 Onchange product_id selected: {self.product_id.display_name} (ID: {self.product_id.id})") # type: ignore

            # Get the product template ID
            tmpl_id = self.product_id.id # type: ignore
        
            print(f"🔹 Parent product template ID: {tmpl_id}")

            # Find the BoM for this product template
            bom = self.env["mrp.bom"].search([("product_tmpl_id", "=", tmpl_id)], limit=1)

            if bom:
                print(f"BoM ID {bom.id} for product template {tmpl_id}:")
                # Clear and populate the global list
                current_bom_line_product_ids = []
                for line in bom.bom_line_ids:
                    current_bom_line_product_ids.append(line.product_id.id)
                    print(f" - Part product ID: {line.product_id.id}, Name: {line.product_id.display_name}, Qty: {line.product_qty}, UoM: {line.product_uom_id.name}")
                
                print(f"📋 Exported BoM line product IDs: {current_bom_line_product_ids}")
                
            else:
                print(f"No BoM found for product template {tmpl_id}")
                current_bom_line_product_ids = []



class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        global current_bom_line_product_ids
        args = args or []

        if self.env.context.get("default_detailed_type"):
            if current_bom_line_product_ids:
                # Only show products that are in the current BoM lines
                args += [('id', 'in', current_bom_line_product_ids)]
                
                products = self.search(args, limit=limit)
                print("✅ Available BoM component products from global list:")
                for p in products:
                    print(f" - Product ID: {p.id}, Name: {p.display_name}") # type: ignore
            else:
                print("❌ No BoM line product IDs in global list")
                # Return empty result if no BoM line data
                return []

        return super().name_search(name=name, args=args, operator=operator, limit=limit)