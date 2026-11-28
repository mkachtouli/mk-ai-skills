# Stable description template

Start with a short **unheaded opening**: accurate product noun, main use and one or two verified distinctions. Use short paragraphs and simple bullets that paste into Etsy. Do not rely on HTML, ornamental fonts or many emojis.

Use these exact English headings and order across products. Do not rename or merge them: `KEY FEATURES`, `REFERENCE CODE`, `DIMENSIONS (APPROXIMATE)`, `WHAT’S INCLUDED & OPTIONS` and `SHIPPING, RETURNS & WARRANTY` are not substitutes. Plain headings or Markdown bold headings are accepted; straight/curly apostrophes in WHAT’S INCLUDED are equivalent.

1. **FEATURES** — useful design, function, configuration and real options. No unsupported performance, handmade or certification claims.
2. **DIMENSIONS & FIT** — confirmed dimensions with precise measurement names; approximate/source-listed wording and inches only. Never estimate physical sizes from pixels or props. If no reliable dimensions exist, omit this section and record the missing inputs outside buyer copy.
3. **MATERIAL & FINISH** — verified substrate and finish; supported finish behavior. If image-only material is unknown, omit rather than naming a metal from its color. Do not list finishes that are not actually offered.
4. **WHAT’S INCLUDED** — exact quantity/components; distinguish props, optional accessories and bundles. A photo showing several objects is not proof they all ship. If exact packing is unknown, state only the evidenced item and flag accessories in seller notes.
5. **SHIPPING & SUPPORT** — confirmed shop/product terms only. Fallback: “Please see the shipping and returns sections of this listing for processing times, delivery estimates and return eligibility. Have a question about this item? Send us an Etsy message before ordering.” No copied free shipping, express delivery, DDP, warranty or support promises. Every concrete policy promise, including dispatch time, delivery estimate, return window, shipping charge and warranty, requires explicit current-user confirmation for the target shop/product and a linked evidence record. Never insert unconfirmed terms followed by “confirm/verify before publishing”; move the question to seller notes and use the neutral fallback. Use `[BRAND_NAME]` for the seller’s brand. Include a warranty only with current user-confirmed duration, start event, coverage and remedy for this shop/product; never inherit another brand’s two-year or other warranty. If unconfirmed, omit the warranty paragraph and flag it in seller notes. Do not invent exclusions or replace statutory rights.
6. **PRODUCT IDENTIFICATION** — confirmed SKU/model only. Omit if unknown. Never invent SKU from photo, competitor listing ID or inferred naming scheme.

FEATURES, WHAT’S INCLUDED and SHIPPING & SUPPORT are required. Only DIMENSIONS & FIT, MATERIAL & FINISH and PRODUCT IDENTIFICATION may be omitted for missing evidence, with a reason in `omitted_sections`. Keep the remaining order if a section is omitted. No empty headings, TODO/TBD or seller instructions in buyer copy. The intentional exception is `[BRAND_NAME]`, plus explicitly requested warranty-template variables listed below; declare every used variable and flag replacement before publication. Do not introduce other unfinished placeholders.

## Editable brand and warranty template

Keep `[BRAND_NAME]` literal wherever the brand appears. Do not insert a source shop’s brand, personal details or a brand remembered from another task. A warranty paragraph is optional, never a default.

If all warranty terms are confirmed, write them with `[BRAND_NAME]`; for example, ONLY when the user confirms these terms: “[BRAND_NAME] offers a 2-year warranty from the date of delivery covering manufacturing and finish defects, with replacement or refund.” This example is not a standard warranty policy.

When explicitly requested as a reusable warranty template: “[BRAND_NAME] offers a [WARRANTY_DURATION] warranty starting [WARRANTY_START], covering [WARRANTY_COVERAGE], with [WARRANTY_REMEDY].” Keep reusable warranty-template wording outside the buyer description, in seller notes or a separate template field, unless every policy term is confirmed. A request for a template does not confirm a warranty. Declare used variables in `template_variables` with a confirmed value or null, and note that unresolved placeholders must be replaced before publication.

## Optional sections

Insert only useful, supported sections **after WHAT’S INCLUDED and before SHIPPING & SUPPORT**:

- **INSTALLATION & CARE** for fixtures/handling; if extensive use **INSTALLATION**, then **CARE**.
- **PERSONALIZATION** for actually offered customization with confirmed instructions.
- **DIGITAL DELIVERY & FILES** for real digital goods, confirmed formats/quantity/software needs and delivery.

Reuse the same names and placement rather than inventing a layout per listing. No rigid description word count or keyword density: explain the product, put the primary phrase naturally in the opening and distribute accurate synonyms in relevant sections. Don't copy competitor prose or add their names to buyer copy.

## Evidence records

`research.md` must include a product fact ledger with source IDs, a sourced keyword table with observed wording/settings and placement evidence, a competitor comparison, the full normalized price table and calculation/exclusions. Cite accessible source links and retrieval dates; cite uploaded/local source files by filename plus page/figure. Current-user confirmation may use a dated conversation reference instead of a public URL. Never publish private conversation content to external services.

Price comparisons must match the proposed material, size, finish, quantity and included components. If no-drain contents are unconfirmed, do not call the offer drain-excluded or average it as an exact no-drain bundle. Record the assumption and mark pricing provisional. Distinguish observed competitor intervals from a recommended planning band.

## JSON contract

Required fields for listing.json:

- `title`: one recommended title; report counts in handoff.
- `description`: unheaded opening and applicable stable headings.
- `tags`: 13 distinct accurate strings, each at most 20 characters; report a genuine shortage instead of unrelated padding.
- `market`, `currency`: default United States / USD.
- `template_variables`: object of the exact bracketed tokens used in title/description/tags, with confirmed values or null; e.g. `{"[BRAND_NAME]": null}`. Use `{}` when the brand is not mentioned and no variables occur. Brand text remains `[BRAND_NAME]` even if its intended replacement is known. Only `[BRAND_NAME]`, `[WARRANTY_DURATION]`, `[WARRANTY_START]`, `[WARRANTY_COVERAGE]`, `[WARRANTY_REMEDY]` are supported; warranty tokens require an explicitly requested template.
- `publication_ready`: false while any editable placeholder remains, even when its intended value is recorded.
- `product`: `identity`, `identity_confidence`, `facts`, `unknowns`. Fact entries identify name, value, evidence status and source. Unknowns are not silently filled from lookalikes.
- `price_recommendation`: `suggested_usd`, `range_usd` ([low, high]), `regular_median_usd`, `usable_comparable_count`, `shipping_basis`, `confidence`, `profitability_verified`. Use null for unknown numbers, not invented zero. Margin remains unverified without cost inputs.
- `research_sources`: nonempty array; each entry requires unique `id`, `surface`, `date`, `reference` (URL, file/page, or dated current-user confirmation), `observation`, plus relevant query/settings. Source-listed policy text does not confirm target-shop policies. When a search surface fails, include dated attempt records with engine/surface, query, actual settings, status (`used`, `blocked`, `unavailable`) and reason. Label substitute-engine observations truthfully; do not attribute them to Google or Etsy search.
- `policy_claims`: array (empty with neutral fallback only). Each entry requires `text` (exact buyer-copy claim), `source_id`, `confirmed_by_current_user: true`, `scope: "target_shop_product"`. The linked evidence must actually confirm these exact terms; boolean flags are not evidence. No inherited competitor/source-shop promises.
- `price_comparables`: array of rows. Each row requires `source_id`, `seller`, `option` (exact size/material/finish/quantity/bundle), `placement_status`, `placement_evidence`, `regular_usd`, `sale_usd` (number or null), `shipping_usd` (number or null), `included` (boolean), `reason`. Included rows must be verified organic, unique per seller/offer, relevant and use positive regular prices. Ads/unknown placement cannot be included.
- `price_recommendation.comparison_basis`: `delivered` (regular plus verified shipping) or `item_only` (clearly disclose missing shipping). `usable_comparable_count` must equal included rows. `regular_median_usd` must equal their normalized median and requires at least three usable rows; otherwise null with provisional pricing. Use `confidence: "provisional"` when no usable rows or bundle identity is unresolved.
- `omitted_sections`: object mapping omitted heading to reason, e.g. `{"PRODUCT IDENTIFICATION":"No confirmed SKU"}`.
- `seller_notes`: missing/ambiguous facts, assumptions and actual limitations.

Add category/attributes, source URL, confirmed SKU/options and price observations as useful. Photo-only output may omit unverified dimensions/material/identification; affected copy/price stays provisional. If identity cannot be resolved, provide supported work and the needed clarification instead of claiming upload readiness.
