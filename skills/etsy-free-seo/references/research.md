# Free research and market pricing

## US settings

Use English Google Search and US country targeting (`hl=en`, `gl=us` when supported). Use visible non-personalized results controls and verify the resulting state. Physical location can still matter; US parameters do not prove a US IP or fixed nationwide ranking. For Etsy, verify US/English/USD display. For delivered-price comparisons, use the same public reference destination, e.g. US ZIP 10001, explicitly not the buyer's address.

Search progressively from exact identity to matching use. Read relevant results rather than cycling through guessed URLs. Google Shopping prices require merchant/variant verification and a verified free, non-sponsored listing. Paid placements are excluded, not analyzed as a separate comparator group. A result title or shopping card does not verify the product's full specification.

Autocomplete can lag after filling text. Observe the updated dropdown before assigning suggestions; immediate ArrowDown may select an old suggestion. Separate history, generic weekly trends and shop-name searches from product suggestions. Never turn a suggestion into an invented monthly volume.

## Search-engine fallback

Google is the preferred web-search source, not a single point of failure. For a visible access error, CAPTCHA, unavailable page or rate limit, make at most one appropriate ordinary UI recovery, then continue independent public research automatically through **Bing → DuckDuckGo → Yahoo**, stopping at the first engine that supplies usable organic results. Do not keep retrying Google or require the user to unblock it before doing independent research. If that fallback fails, try the next engine; once evidence is sufficient, stop. Do not evade CAPTCHA, authentication, rate limits or security warnings; use the required takeover only if recovering that particular surface is necessary.

Use the same exact product/material/use queries and US English settings where available. Verify and record actual region/language in each engine’s UI; if US targeting cannot be established, mark that limitation rather than claiming US rankings. Do not assume Google URL parameters work on another engine. Bing, Yahoo and DuckDuckGo ads, sponsored shopping cards and ambiguous placements remain excluded. Read the original merchant/Etsy page to verify the actual offer. Deduplicate the same seller/listing across engines; repeated or syndicated results are not independent competitors or demand confirmation.

Distinguish the failed Google surface:

- **Search:** another engine’s organic results can replace discovery and vocabulary research.
- **Shopping:** use verified free shopping listings if the fallback offers them; otherwise use organic merchant results and verified direct product offers. Do not claim Shopping was inspected if it was unavailable.
- **Autocomplete:** observe actual fallback suggestions if available and identify the engine/prefix. These are not Google Autocomplete or measured search volume.
- **Trends:** Bing/Yahoo/DuckDuckGo result counts, suggestions or rankings cannot replace Google Trends indices. If Trends remains unavailable, record missing trend evidence and complete the supported research without fabricated trend data.
- **Etsy Search:** a query such as `site:etsy.com/listing <product phrase>` on an accessible engine may discover public Etsy competitors, but establishes organic appearance on that engine only, not Etsy rank or Etsy Autocomplete. Report the actual Etsy surface limitation.

For every attempt, record engine/surface, query, date, actual settings, status (`used`, `blocked`, `unavailable`) and failure reason when applicable. Accepted evidence retains source URLs, placement evidence and engine identity. Mention actual substitutions in the final handoff. If all search engines fail, complete only source-supported copy; mark competitor research and pricing provisional or unavailable.

## Organic-only eligibility

Use only verified non-sponsored Google Search, Google Shopping, Bing, DuckDuckGo, Yahoo and Etsy Search results for keyword extraction, competitor analysis and price recommendations. Exclude cards/blocks labelled Sponsored, Ad, Ads, Promoted, Etsy Ads or equivalent labels in other languages. Check the enclosing block as well as the individual card; a paid block label applies to its cards. Search position alone and missing labels in a truncated extract do not prove organic status. If status cannot be established from the visible UI/context, exclude it and record the limitation.

For each accepted search result, record query, surface, URL, date, placement status (`organic`) and visible evidence/context. Excluded paid or ambiguous results may be logged with an exclusion reason but must not supply keyword recommendations, competitor findings or price calculations. Do not open an ad-discovered merchant directly to relabel it organic. If the same listing also appears independently in an organic result, use and document that organic appearance; its ad appearance is not an automatic ban on the whole seller.

The user-supplied product URL remains the authority for identifying their requested product, regardless of how they obtained it; it does not establish organic rank or count as an independently discovered competitor. Autocomplete and Trends remain eligible on their own terms, without treating them as search-result rankings.

## Evidence classes

|Public observation|Supports|Does not establish|
|---|---|---|
|Autocomplete|Wording actually offered in that session|Volume, global popularity, sales|
|Organic query result|Observed visibility/relevance|Fixed rank, visits, ranking cause|
|Competitor title/description|Positioning and vocabulary|Full 13-tag set, traffic keywords|
|Item reviews|Reported experience of those buyers|Independent testing, all-unit quality|
|Shop score/sales|Shop-wide reputation/activity|Listing reviews or unit sales|
|Trends index|Relative Google interest in selected scope|Monthly counts, Etsy demand, conversion|
|Merchant card price|Lead to verify|Matching bundle, delivered total|

Call competitor phrases **visible keywords / observed appearance**, never confirmed visit drivers without authorized analytics showing them. Public “Explore related searches” is not the seller's entered tags. Inaccessible tags remain unknown. Keep Google and Etsy evidence separate.

## Competitor selection

Normally study 3–5 listings. Select comparable verified organic offers only; ads and ambiguous placements are ineligible. Exclude Recently viewed/recommendation modules from organic ranking observations. A seller can appear both in an Ad and organically; document the independent organic result used. Record:

- Actual selected finish, size, quantity, material, bundle and accessories.
- Public title/description phrases and main use.
- Whole product, installation, details, packing list and dimension images where present. Distinguish a caption from a photograph you actually inspected.
- Buyer objections: fit, sealing, missing pieces, unclear options, finish or shipping.
- Seller-stated policies, clearly attributed. Never transfer them to the user’s brand.
- Item ratings/count separately from shop reputation; an established shop may have no reviews on that item.

Strengths are observed features or reasoned interpretations, not proven reasons for revenue. Paraphrase review concerns rather than copying long reviews. Similar dimensions/SKUs that conflict with the supplied source are gaps to resolve, not permission to merge specifications.

## Price normalization

Try for 5–8 genuinely comparable observed offers when feasible; fewer clean offers are better than misleading minimums. Deep competitor review and price research can reuse the same sources. Record:

`URL | date | discovery query/surface | placement status/evidence | merchant | selected variation | quantity | material/finish | dimensions | currency | regular | sale | shipping to reference destination | eligible/excluded reason`

1. Admit only offers discovered through verified organic/free listings; exclude paid or ambiguous discoveries from sample size, medians, ranges and recommendations. Then normalize the **offer before price**. A cheap stopper-only minimum is not a complete P-trap kit. Explicitly choose the correct option where possible; exclude ambiguous unselected `+` prices, samples, deposits, per-piece minima used as pack totals and unrelated add-ons from normalized calculations.
2. Use regular prices as this seller's main benchmark; show current sales separately. Do not manufacture an artificial regular price/discount for the proposed item.
3. Compare USD delivered totals (item plus mandatory shipping) to one destination where verified. Unknown shipping is not free. State whether a median is item-only or delivered. Keep unverified taxes/duties unknown. If currency conversion is needed, verify dated rate and retain original values.
4. For a reasonably comparable sample, normally at least three usable offers, report sample size, regular median and a typical observed interval, explaining exclusions/outliers. Do not call a handpicked minimum/maximum a market average. With sparse/heterogeneous evidence, propose a provisional reasoned range and no representative median.
5. Recommend one defensible price and shipping assumption. A delivered/free-shipping target depends on actual costs. Product, packing, labor, fees, Ads, shipping and returns allowance are needed for profitability. Competitor prices do not prove margins. Do not automatically undercut the cheapest offer.

## Required evidence handoff

Always deliver `research.md` and `listing.json` with the copy. Supply linked source IDs and dated observations for specifications, SKU, keywords, organic discovery and each price row. Report counts and medians only when reproducible from included `price_comparables`; one independently selected seller offer per comparable, keeping other sizes in separate comparison groups. Do not count the user-supplied source in an independent competitor median. When fewer than three eligible rows exist, leave the representative median null and state the limited evidence. Unknown shipping remains null, never zero; identify item-only comparisons explicitly.

Current-user confirmation for the target shop/product is required for concrete shipping, returns and warranty promises. Competitor/source policies can be documented as attributed research but cannot enter buyer copy or be legitimized by a “verify before publishing” note.

## Blockers and audit trail

Save dates, actual settings and relevant raw evidence. Do not claim autocomplete used if only a prefix was typed, or Trends used if no report loaded. If one source fails after a reasonable UI recovery, follow the search-engine fallback above, continue other supported work and identify the actual limit. Never replace missing free-source evidence with paid databases without explicit authorization.
