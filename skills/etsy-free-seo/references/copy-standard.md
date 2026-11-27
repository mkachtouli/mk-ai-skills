# Stable description template

Start with a short **unheaded opening**: accurate product noun, main use and one or two verified distinctions. Use short paragraphs and simple bullets that paste into Etsy. Do not rely on HTML, ornamental fonts or many emojis.

Keep these English headings and order across products:

1. **FEATURES** — useful design, function, configuration and real options. No unsupported performance, handmade or certification claims.
2. **DIMENSIONS & FIT** — confirmed dimensions with precise measurement names; approximate/source-listed wording and inches only. Never estimate physical sizes from pixels or props. If no reliable dimensions exist, omit this section and record the missing inputs outside buyer copy.
3. **MATERIAL & FINISH** — verified substrate and finish; supported finish behavior. If image-only material is unknown, omit rather than naming a metal from its color. Do not list finishes that are not actually offered.
4. **WHAT’S INCLUDED** — exact quantity/components; distinguish props, optional accessories and bundles. A photo showing several objects is not proof they all ship. If exact packing is unknown, state only the evidenced item and flag accessories in seller notes.
5. **SHIPPING & SUPPORT** — confirmed shop/product terms only. Fallback: “Please see the shipping and returns sections of this listing for processing times, delivery estimates and return eligibility. Have a question about this item? Send us an Etsy message before ordering.” No copied free shipping, express delivery, DDP, warranty or support promises. Use `[BRAND_NAME]` for the seller’s brand. Include a warranty only with current user-confirmed duration, start event, coverage and remedy for this shop/product; never inherit another brand’s two-year or other warranty. If unconfirmed, omit the warranty paragraph and flag it in seller notes. Do not invent exclusions or replace statutory rights.
6. **PRODUCT IDENTIFICATION** — confirmed SKU/model only. Omit if unknown. Never invent SKU from photo, competitor listing ID or inferred naming scheme.

Keep the remaining order if a section is omitted. No empty headings, TODO/TBD or seller instructions in buyer copy. The intentional exception is `[BRAND_NAME]`, plus explicitly requested warranty-template variables listed below; declare every used variable and flag replacement before publication. Do not introduce other unfinished placeholders.

## Editable brand and warranty template

Keep `[BRAND_NAME]` literal wherever the brand appears. Do not insert a source shop’s brand, personal details or a brand remembered from another task. A warranty paragraph is optional, never a default.

If all warranty terms are confirmed, write them with `[BRAND_NAME]`; for example, ONLY when the user confirms these terms: “[BRAND_NAME] offers a 2-year warranty from the date of delivery covering manufacturing and finish defects, with replacement or refund.” This example is not a standard warranty policy.

When explicitly requested as a reusable warranty template: “[BRAND_NAME] offers a [WARRANTY_DURATION] warranty starting [WARRANTY_START], covering [WARRANTY_COVERAGE], with [WARRANTY_REMEDY].” Do not add this paragraph when no warranty is confirmed or requested. Declare used variables in `template_variables` with a confirmed value or null, and note that unresolved placeholders must be replaced before publication.

## Optional sections

Insert only useful, supported sections **after WHAT’S INCLUDED and before SHIPPING & SUPPORT**:

- **INSTALLATION & CARE** for fixtures/handling; if extensive use **INSTALLATION**, then **CARE**.
- **PERSONALIZATION** for actually offered customization with confirmed instructions.
- **DIGITAL DELIVERY & FILES** for real digital goods, confirmed formats/quantity/software needs and delivery.

Reuse the same names and placement rather than inventing a layout per listing. No rigid description word count or keyword density: explain the product, put the primary phrase naturally in the opening and distribute accurate synonyms in relevant sections. Don't copy competitor prose or add their names to buyer copy.

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
- `research_sources`: entries with surface, URL/input, observation date, settings and actual finding.
- `omitted_sections`: object mapping omitted heading to reason, e.g. `{"PRODUCT IDENTIFICATION":"No confirmed SKU"}`.
- `seller_notes`: missing/ambiguous facts, assumptions and actual limitations.

Add category/attributes, source URL, confirmed SKU/options and price observations as useful. Photo-only output may omit unverified dimensions/material/identification; affected copy/price stays provisional. If identity cannot be resolved, provide supported work and the needed clarification instead of claiming upload readiness.
