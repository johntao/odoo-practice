# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.fields import Command


class EstatePropertyAccount(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        self.ensure_one()
        super().action_sold()
        print("overriden action_sold")
        self._create_invoice()
        return True

    def _create_invoice(self):
        (
            self.env["account.move"]
            .sudo()
            .with_context(default_move_type="out_invoice")
            .create(
                {
                    # "ref": self.client_order_ref or "",
                    # "narration": self.note,
                    # "currency_id": self.currency_id.id,
                    # "campaign_id": self.campaign_id.id,
                    # "medium_id": self.medium_id.id,
                    # "source_id": self.source_id.id,
                    # "team_id": self.team_id.id,
                    # "partner_shipping_id": self.partner_shipping_id.id,
                    # "fiscal_position_id": (
                    #     self.fiscal_position_id
                    #     or self.fiscal_position_id._get_fiscal_position(
                    #         self.partner_invoice_id
                    #     )
                    # ).id,
                    # "invoice_origin": self.name,
                    # "invoice_payment_term_id": self.payment_term_id.id,
                    # "invoice_user_id": self.user_id.id,
                    # "payment_reference": self.reference,
                    # "transaction_ids": [Command.set(self.transaction_ids.ids)],
                    # "company_id": self.company_id.id,
                    # "user_id": self.user_id.id,
                    "invoice_line_ids": [
                        Command.create(
                            {
                                # "display_type": self.display_type or "product",
                                # "sequence": self.sequence,
                                # "product_id": self.product_id.id,
                                # "product_uom_id": self.product_uom.id,
                                # "discount": self.discount,
                                # "tax_ids": [Command.set(self.tax_id.ids)],
                                # "sale_line_ids": [Command.link(self.id)],
                                # "is_downpayment": self.is_downpayment,
                                # 6% of the selling price
                                "name": self.name,
                                "quantity": 1,
                                "price_unit": self.selling_price * 0.06,
                            }
                        ),
                        Command.create(
                            {
                                # an additional 100.00 from administrative fees
                                "name": "Administrative fees",
                                "quantity": 1,
                                "price_unit": 100,
                            }
                        ),
                    ],
                    "move_type": "out_invoice",
                    "partner_id": self.buyer_partner_id.id,
                }
            )
        )
