import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('validator', Path(__file__).parents[1] / 'scripts/validate_manifest.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        (self.base / 'drawing.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.data = dict(product_url='https://example.com/product', product_name='Test model', brand='Test',
                         support_url='https://example.com/contact', support_url_verified=True,
                         qr_url='https://example.com/contact', units='in', page_limit=2,
                         facts=[dict(key='mount', label='Mount', value='Deck', status='sourced', source='product page')],
                         parts=[dict(ref='13', name='Hoses', quantity=2, status='user-confirmed', source='user')],
                         illustrations=[dict(role='components', path='drawing.svg', callouts=['13'],
                                             status='user-confirmed', source='approved drawing', geometry_checked=True)])
    def tearDown(self):
        self.tmp.cleanup()
    def report(self):
        return v.validate(self.data, self.base, True)
    def test_valid(self):
        self.assertEqual(self.report()['errors'], [])
        self.assertFalse(self.report()['engineering_accuracy_verified'])
    def test_missing_or_extra_callout(self):
        self.data['illustrations'][0]['callouts'] = ['12']
        self.assertTrue(self.report()['errors'])
    def test_duplicate_part(self):
        self.data['parts'].append(copy.deepcopy(self.data['parts'][0]))
        self.assertIn('Duplicate parts table references', self.report()['errors'])
    def test_unknown_customer_fact(self):
        self.data['facts'][0]['status'] = 'unknown'
        self.assertTrue(self.report()['errors'])
        self.assertFalse(v.validate(self.data, self.base, False)['errors'])
    def test_wrong_support_qr(self):
        self.data['qr_url'] = self.data['product_url']
        self.assertIn('Support QR must point to support_url', self.report()['errors'])
    def test_geometry_and_missing_asset(self):
        self.data['illustrations'][0]['geometry_checked'] = False
        (self.base / 'drawing.svg').unlink()
        self.assertEqual(len(self.report()['errors']), 2)
    def test_evidence_required(self):
        self.data['facts'][0]['source'] = ''
        self.assertTrue(self.report()['errors'])

if __name__ == '__main__':
    unittest.main()
