#!/usr/bin/env python3
"""Validate Etsy copy limits, section order and price sanity, not SEO success."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

CORE = ['FEATURES', 'DIMENSIONS & FIT', 'MATERIAL & FINISH', 'WHAT’S INCLUDED', 'SHIPPING & SUPPORT', 'PRODUCT IDENTIFICATION']
OPTIONAL = ['INSTALLATION & CARE', 'INSTALLATION', 'CARE', 'PERSONALIZATION', 'DIGITAL DELIVERY & FILES']


def inspect(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ['Root must be a JSON object.'], warnings
    title = data.get('title')
    if not isinstance(title, str) or not title.strip():
        errors.append('Nonempty title required.')
    elif len(title) > 140:
        errors.append(f'Title exceeds 140 characters: {len(title)}.')
    elif len(title.split()) >= 15:
        warnings.append('15+ title words; review Etsy brevity recommendation (not a hard limit).')
    tags = data.get('tags')
    if not isinstance(tags, list):
        errors.append('Tags must be an array.')
    else:
        if len(tags) != 13:
            errors.append(f'Expected 13 tags; found {len(tags)}.')
        seen, signatures = set(), {}
        for tag in tags:
            if not isinstance(tag, str) or not 1 <= len(tag) <= 20 or tag != tag.strip():
                errors.append(f'Invalid tag type/length/edge spacing: {tag!r}.')
                continue
            key = unicodedata.normalize('NFKC', tag).casefold()
            if key in seen:
                errors.append(f'Duplicate tag: {tag!r}.')
            seen.add(key)
            if not tag[0].isalnum() or any(not (c.isalnum() or c in " '-’") for c in tag):
                errors.append(f'Unsupported tag punctuation: {tag!r}.')
            sig = tuple(sorted(re.findall(r'\w+', key)))
            if sig in signatures:
                warnings.append(f'Reordered tag intent: {signatures[sig]!r} / {tag!r}.')
            signatures[sig] = tag
    allowed_variables = {'[BRAND_NAME]', '[WARRANTY_DURATION]', '[WARRANTY_START]', '[WARRANTY_COVERAGE]', '[WARRANTY_REMEDY]'}
    variables = data.get('template_variables', {})
    if not isinstance(variables, dict):
        errors.append('template_variables must be an object.')
        variables = {}
    copy_fields = [data.get('title'), data.get('description')]
    if isinstance(tags, list):
        copy_fields.extend(tags)
    used_variables = set(re.findall(r'\[[^\]\n]+\]', '\n'.join(x for x in copy_fields if isinstance(x, str))))
    for token in sorted(used_variables):
        if token not in allowed_variables:
            errors.append(f'Unsupported unfinished placeholder: {token}.')
        elif token not in variables:
            errors.append(f'Declare template variable: {token}.')
    if used_variables & allowed_variables:
        if data.get('publication_ready') is not False:
            errors.append('Set publication_ready to false while editable variables remain.')
        warnings.append('Editable template: replace declared variables before publication.')
    desc = data.get('description')
    if not isinstance(desc, str) or not desc.strip():
        errors.append('Nonempty description required.')
    else:
        lines = [line.strip().replace("WHAT'S INCLUDED", 'WHAT’S INCLUDED') for line in desc.splitlines()]
        found = [line for line in lines if line in CORE + OPTIONAL]
        indices = [CORE.index(h) for h in found if h in CORE]
        if indices != sorted(indices) or len(found) != len(set(found)):
            errors.append('Core headings out of order or headings duplicated.')
        omitted = data.get('omitted_sections', {})
        if not isinstance(omitted, dict):
            errors.append('omitted_sections must be an object.')
            omitted = {}
        for heading in CORE:
            if heading not in found and not omitted.get(heading):
                errors.append(f'Missing section {heading!r}; include or document omission.')
        for heading in OPTIONAL:
            if heading in found and ('WHAT’S INCLUDED' not in found or 'SHIPPING & SUPPORT' not in found or not found.index('WHAT’S INCLUDED') < found.index(heading) < found.index('SHIPPING & SUPPORT')):
                errors.append(f'{heading!r} must be after contents and before shipping.')
        if found and lines.index(found[0]) == 0:
            warnings.append('Add an unheaded opening paragraph.')
        if re.search(r'\b(?:TODO|TBD)\b|\[(?:insert|confirm|unknown)[^\]]*\]', desc, re.I):
            errors.append('Unfinished buyer-copy placeholder.')
        if re.search(r'\d\s*(?:cm|mm|centimeters?|millimeters?)\b', desc, re.I):
            warnings.append('Metric dimension found; default buyer units are inches.')
    price = data.get('price_recommendation')
    if not isinstance(price, dict):
        errors.append('price_recommendation object required, nulls for unknown numbers.')
    else:
        def numeric(value):
            return isinstance(value, (int, float)) and not isinstance(value, bool)
        suggested, bounds = price.get('suggested_usd'), price.get('range_usd')
        if suggested is not None and (not numeric(suggested) or suggested <= 0):
            errors.append('Suggested price must be positive or null.')
        if bounds is not None:
            if not isinstance(bounds, list) or len(bounds) != 2 or not all(numeric(v) and v > 0 for v in bounds) or bounds[0] > bounds[1]:
                errors.append('Price range must be ordered positive [low, high] or null.')
            elif numeric(suggested) and not bounds[0] <= suggested <= bounds[1]:
                errors.append('Suggested price outside range.')
        count, median = price.get('usable_comparable_count', 0), price.get('regular_median_usd')
        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            errors.append('Comparable count must be a nonnegative integer.')
        elif median is not None:
            if not numeric(median) or median <= 0:
                errors.append('Median must be positive or null.')
            if count < 3:
                warnings.append('Median has fewer than three comparables; explain limited sample.')
        if not price.get('shipping_basis'):
            errors.append('State price shipping_basis.')
    if not data.get('research_sources'):
        warnings.append('No research_sources; do not claim evidence-backed completion.')
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('listing', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.listing.read_text())
    except (OSError, ValueError) as exc:
        print('ERROR:', exc)
        return 1
    errors, warnings = inspect(data)
    for error in errors:
        print('ERROR:', error)
    for warning in warnings:
        print('WARNING:', warning)
    if not errors:
        print(f"PASS: {len(data['title'])}/140 title characters; {len(data['tags'])}/13 tags.")
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
