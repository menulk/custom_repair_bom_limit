# Odoo 17 Custom Repair BoM Limit Module by Menushi Lakshika
## Overview
This module restricts repair order lines to only allow components from the product's Bill of Materials.

## Features
- BoM component restriction for repair lines
- Multi-level BoM support
- Dynamic domain updates

## Installation
1. Copy module to custom addons directory
2. Restart Odoo server
3. Go to Apps > Update Apps List
4. Install "Custom Repair BoM Limit"

## Usage
1. Create repair order with a product that has BoM
2. Products that have a BoM will be available in dropdown
3. Add repair lines - only BoM components will be available
4. Validation prevents limits to adding non-BoM components

## Limitations
1. Alternative BoMs not supported
If a product has multiple BoMs, only the default BoM is considered. No option to select which BoM should apply.
2. Limited to standard repair workflow
Module tested mainly with repair.order (community edition). May need adjustments for enterprise features like inventory or operational integrations.
3. Stock availability not validated
Restriction ensures only BoM components are selectable, but does not check if the product is available in stock.

