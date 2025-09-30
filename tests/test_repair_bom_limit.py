from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestRepairBomLimit(TransactionCase):

    def setUp(self):
        super().setUp()
        
        # Create test products
        self.product_main = self.env['product.product'].create({
            'name': 'Main Product',
            'type': 'product',
        })
        
        self.component_1 = self.env['product.product'].create({
            'name': 'Component 1',
            'type': 'product',
        })
        
        self.component_2 = self.env['product.product'].create({
            'name': 'Component 2',
            'type': 'product',
        })
        
        self.non_bom_product = self.env['product.product'].create({
            'name': 'Non-BoM Product',
            'type': 'product',
        })
        
        # Create BoM
        self.main_bom = self.env['mrp.bom'].create({
            'product_tmpl_id': self.product_main.product_tmpl_id.id,
            'product_id': self.product_main.id,
            'product_qty': 1.0,
            'type': 'normal',
        })
        
        self.env['mrp.bom.line'].create([
            {
                'bom_id': self.main_bom.id,
                'product_id': self.component_1.id,
                'product_qty': 1.0,
            },
            {
                'bom_id': self.main_bom.id,
                'product_id': self.component_2.id,
                'product_qty': 1.0,
            }
        ])
        
        # Create repair order
        self.repair_order = self.env['mrp.repair'].create({
            'product_id': self.product_main.id,
            'product_qty': 1.0,
            'state': 'draft',
        })

    def test_allowed_bom_components_positive(self):
        """Test that BoM components are correctly identified"""
        allowed_components = self.repair_order._get_allowed_bom_components()
        expected_components = self.component_1 | self.component_2
        self.assertEqual(allowed_components, expected_components)

    def test_repair_line_validation_positive(self):
        """Test that valid BoM components can be added"""
        repair_line = self.env['mrp.repair.line'].create({
            'repair_id': self.repair_order.id,
            'product_id': self.component_1.id,
            'product_uom_qty': 1.0,
            'type': 'add',
        })
        self.assertTrue(repair_line.id)

    def test_repair_line_validation_negative(self):
        """Test that non-BoM components raise ValidationError"""
        with self.assertRaises(ValidationError):
            self.env['mrp.repair.line'].create({
                'repair_id': self.repair_order.id,
                'product_id': self.non_bom_product.id,
                'product_uom_qty': 1.0,
                'type': 'add',
            })
