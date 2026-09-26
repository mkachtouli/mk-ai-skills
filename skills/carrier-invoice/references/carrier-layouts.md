# Carrier layouts examined

These notes guide classification, not automatic trust. Confirm the actual columns and totals on each new invoice.

## DHL Morocco

- A freight invoice may list each airbill over multiple pages. Use the waybill's final `Sous-total`/total-charges amount, including fuel, local-service tax, remote-area and other surcharges, as shipping cost. Do not use only the `TRANSPORT` line or add itemized charges on top of the subtotal.
- A separate customs invoice may list the same waybill with `DUTY TAX PAID`, `REGULATORY CHARGES`, and `IMPORT EXPORT DUTIES`. Its per-waybill subtotal is DDP cost. `DUTY TAX PAID` is a service-fee line in the examined layout, not the complete DDP subtotal.
- The examined examples reconcile 23 freight waybills to 18,515.34 MAD and four customs waybills to 1,999.84 MAD. Do not bundle the customer's actual invoices or waybill numbers in this repository.

## Aramex Morocco

- The examined outbound invoice has `HAWB`, `Base Charge`, `Autres Charges`, and `Net Montant` per shipment. Four displayed `Net Montant` values total 1,289.67 MAD.
- Atlasty confirmed that Aramex taxes 100.00 MAD per shipment at 20%, making VAT 20.00 MAD per HAWB on this invoice. Add that to each `Net Montant`: 319.17, 304.02, 319.17, and 427.31 MAD. Their sum is the printed `Montant TTC` of 1,369.67 MAD. Use this rule on another invoice only if the taxable base equals 100.00 MAD × shipment count, the VAT rate is 20%, and the final sum reconciles.
- An optional cash-payment stamp-duty note is not an invoiced shipment charge unless a later document establishes that it was actually billed.

## FedEx

No FedEx sample has been examined. Validate its shipment key, taxes, adjustments, currency, and line-versus-invoice totals on the first supplied sample. Do not claim tested support beforehand.
