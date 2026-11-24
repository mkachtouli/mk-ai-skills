# Input contract and provenance

## User input

Normally only the product URL. Discover the brand and product details there. Optional overrides: language, units, page limit, configuration to cover, approved drawings or replacement source document. Ask only for missing information that affects correctness.

## Local manifest

Keep this JSON beside each job's source files, not in the public skills repository:

```json
{
  "product_url": "https://example.com/products/model",
  "product_name": "Model / Product type",
  "brand": "Brand name",
  "support_url": "https://example.com/pages/contact",
  "support_url_verified": true,
  "qr_url": "https://example.com/pages/contact",
  "units": "in",
  "page_limit": 2,
  "facts": [
    {"key": "material", "label": "Material", "value": "Solid brass", "status": "sourced", "source": "https://example.com/products/model", "critical": false}
  ],
  "parts": [
    {"ref": "1", "name": "Source part name", "quantity": 1, "status": "sourced", "source": "local original specification, page 1"}
  ],
  "illustrations": [
    {"role": "components", "path": "components.png", "status": "user-confirmed", "source": "approved original drawing", "callouts": ["1"], "geometry_checked": true}
  ],
  "configurations": [
    {"name": "Product only", "included": ["Confirmed included item"], "status": "sourced", "source": "https://example.com/products/model"}
  ]
}
```

This example documents structure, not product facts. Relative asset paths resolve against the manifest directory. `facts`, `parts`, `illustrations`, and `configurations` can be empty when not applicable; do not manufacture entries to fill them.

Every published fact, parts row and configuration needs `status` (`sourced` or `user-confirmed`) and a traceable `source`. Use `unknown` only for unresolved records kept outside the printed data. Unknown critical facts block a customer edition; unknown optional facts must be omitted from it. A user-confirmed correction takes priority over stale page data; retain the disagreement in the source record.

For measurements, additionally record `source_value`, `source_unit`, and `precision_note` when converting or displaying approximate values. Do not put approximate hose lengths in the customer specification unless explicitly requested as a specification. A drawing's `geometry_checked` flag records the author's visual/source check; the validator cannot prove CAD accuracy.

The components illustration's `callouts` must match the set of `parts.ref` values. Repeated visual callouts for paired identical parts do not require duplicate table rows. If both dimensions and components are provided, both need a source-geometry check; use the same master wherever possible. Never infer cartridge, seal or fastener designs from a closed product photograph.

## Job outputs

Customer PDF plus local manifest, source/provenance notes, editable composition source and page renders. Keep internal unknowns, extracted raw data and customer/order information out of the customer PDF and out of a public repository. A request to create this guide does not authorize publishing it to the store.
