/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

// Patch FormController for dynamic domain updates
patch(FormController.prototype, {
    async _onFieldChanged(field, changes) {
        const result = await super._onFieldChanged(field, changes);
        
        if (this.props.resModel === "mrp.repair" && field.name === "product_id") {
            const operationsField = this.model.root.fields.operations;
            if (operationsField) {
                this.model.root.invalidateCache();
                await this.model.root.load();
            }
        }
        
        return result;
    },
});
