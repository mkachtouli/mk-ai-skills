#!/usr/bin/env python3
"""Check guide inputs and references; does not certify engineering accuracy."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data, base, customer=False):
    errors, warnings = [], []
    def url(value):
        p = urlparse(str(value or ''))
        return p.scheme in ('https', 'http') and bool(p.netloc)
    for key in ('product_url', 'support_url'):
        if not url(data.get(key)):
            errors.append(f'{key}: valid HTTP(S) URL required')
    for key in ('product_name', 'brand'):
        if not str(data.get(key, '')).strip():
            errors.append(f'{key}: required')
    if customer and data.get('support_url_verified') is not True:
        errors.append('Verify the support URL before using it in a customer PDF')
    if data.get('qr_url') and data['qr_url'] != data.get('support_url'):
        errors.append('Support QR must point to support_url')
    if not isinstance(data.get('page_limit', 2), int) or isinstance(data.get('page_limit'), bool) or data.get('page_limit', 2) < 1:
        errors.append('page_limit must be a positive integer')
    if data.get('units', 'in') not in ('in', 'mm', 'cm', 'mixed'):
        errors.append('units must be in, mm, cm or mixed')
    refs = []
    images = []
    for group in ('facts', 'parts', 'configurations', 'illustrations'):
        rows = data.get(group, [])
        if not isinstance(rows, list):
            errors.append(f'{group}: list required')
            continue
        for i, row in enumerate(rows):
            at = f'{group}[{i}]'
            if not isinstance(row, dict):
                errors.append(f'{at}: object required')
                continue
            status = row.get('status')
            if status not in ('sourced', 'user-confirmed', 'unknown'):
                errors.append(f'{at}: invalid status')
            elif status == 'unknown':
                if customer:
                    errors.append(f'{at}: unresolved data must be resolved or omitted from customer inputs')
                else:
                    warnings.append(f'{at}: unresolved' + (' critical fact' if row.get('critical') else ''))
            elif not str(row.get('source', '')).strip():
                errors.append(f'{at}: evidence source required')
            if group == 'facts':
                if not row.get('key') or not row.get('label') or row.get('value') in (None, ''):
                    errors.append(f'{at}: key, label and value required')
            elif group == 'parts':
                ref = str(row.get('ref', '')).strip()
                if not ref:
                    errors.append(f'{at}: part reference required')
                refs.append(ref)
                q = row.get('quantity')
                if not isinstance(q, int) or isinstance(q, bool) or q < 1:
                    errors.append(f'{at}: quantity must be a positive integer')
                if not row.get('name'):
                    errors.append(f'{at}: part name required')
            elif group == 'configurations':
                if not row.get('name') or not isinstance(row.get('included'), list) or not row.get('included'):
                    errors.append(f'{at}: configuration name and included items required')
            elif group == 'illustrations':
                path = row.get('path')
                if not path or not (base / path).is_file():
                    errors.append(f'{at}: missing local illustration')
                if row.get('role') not in ('components', 'dimensions', 'product'):
                    errors.append(f'{at}: unknown illustration role')
                if customer and row.get('role') in ('components', 'dimensions') and row.get('geometry_checked') is not True:
                    errors.append(f'{at}: source geometry must be checked')
                images.append(row)
    if len(set(refs)) != len(refs):
        errors.append('Duplicate parts table references')
    for row in images:
        if row.get('role') == 'components':
            callouts = row.get('callouts', [])
            if not isinstance(callouts, list) or set(map(str, callouts)) != set(refs):
                errors.append('Components drawing callouts do not match parts table references')
    if refs and not any(row.get('role') == 'components' for row in images):
        warnings.append('Parts table supplied without a components illustration; verify source references')
    return {'errors': errors, 'warnings': warnings, 'engineering_accuracy_verified': False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifest', type=Path)
    p.add_argument('--customer', action='store_true')
    args = p.parse_args()
    try:
        data = json.loads(args.manifest.read_text())
        if not isinstance(data, dict):
            raise ValueError('manifest must be a JSON object')
        report = validate(data, args.manifest.resolve().parent, args.customer)
    except (OSError, ValueError, TypeError) as exc:
        report = {'errors': [str(exc)], 'warnings': [], 'engineering_accuracy_verified': False}
    print(json.dumps(report, indent=2))
    return 1 if report['errors'] else 0

if __name__ == '__main__':
    raise SystemExit(main())
