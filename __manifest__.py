{
    'name': 'Custom Repair BoM Limit',
    'version': '17.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'Restrict Repair Order Lines to Product BoM Components',
    'description': """
        This module restricts repair order lines to only allow components
        that are defined in the Bill of Materials (BoM) of the product being repaired.
        
        Features:
        - Limits repair line products to BoM components only
        - Supports multi-level BoM (flattened components)
        - Dynamic refresh when changing product to repair
        - Validation errors for invalid components
        - Works in both repair and quotation states
    """,
    'author': 'Menushi Lakshika',
    'website': '#',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mrp',
        'repair',
        #'mrp_repair',
    ],
    'data': [
        'views/repair_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_repair_bom_limit/static/src/js/repair_form.js',
        ],
    },
    'demo': [
        'demo/product_demo.xml',
        'demo/mrp_bom_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
} # type: ignore

