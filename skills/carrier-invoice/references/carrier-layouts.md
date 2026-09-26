# Carrier layouts examined

These notes guide classification, not automatic trust. Confirm the actual columns and totals on each new invoice.

## DHL Morocco

- A freight invoice may list each airbill over multiple pages. Use the waybill's final `Sous-total`/total-charges amount, including fuel, local-service tax, remote-area and other surcharges, as shipping cost. Do not use only the `TRANSPORT` line or add itemized charges on top of the subtotal.
- A separate customs invoice may list the same waybill with `DUTY TAX PAID`, `REGULATORY CHARGES`, and `IMPORT EXPORT DUTIES`. Its per-waybill subtotal is DDP cost. `DUTY TAX PAID` is a service-fee line in the examined layout, not the complete DDP subtotal.
- The examined examples reconcile 23 freight waybills to 18,515.34 MAD and four customs waybills to 1,999.84 MAD. Do not bundle the customer's actual invoices or waybill numbers in this repository.

## Aramex Morocco

- The examined outbound invoice has `HAWB`, `Base Charge`, `Autres Charges`, and `Net Montant` per shipment. Four displayed `Net Montant` values total 1,289.67 MAD.
- The invoice also shows 80.00 MAD VAT at invoice level, for a printed total of 1,369.67 MAD. It does not explicitly allocate the VAT to individual HAWBs. A final tax-inclusive shipping cost cannot be read directly from its four rows. Obtain the user's allocation or pre-VAT convention before finalizing those rows.
- An optional cash-payment stamp-duty note is not an invoiced shipment charge unless a later document establishes that it was actually billed.

## FedEx

No FedEx sample has been examined. Validate its shipment key, taxes, adjustments, currency, and line-versus-invoice totals on the first supplied sample. Do not claim tested support beforehand.
