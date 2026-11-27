"""Regression cases from real listing handoffs; no network access."""
import copy
import importlib.util
from pathlib import Path
import unittest
spec = importlib.util.spec_from_file_location('checker', Path(__file__).resolve().parents[1] / 'scripts/check_listing.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            'title': 'Copper Rain Shower Head',
            'description': 'A round copper shower head.\n\nFEATURES\nRound rainfall design.\n\nDIMENSIONS & FIT\nApproximately 6 inches.\n\nMATERIAL & FINISH\nCopper.\n\nWHAT’S INCLUDED\nOne head.\n\nSHIPPING & SUPPORT\nPlease see the shipping and returns sections of this listing for processing times, delivery estimates and return eligibility.',
            'tags': ['copper shower head','rain shower head','rainfall showerhead','outdoor shower head','solid copper','unlacquered copper','round shower head','handmade shower','rustic bathroom','coastal bathroom','poolside shower','living finish','bathroom renovation'],
            'omitted_sections': {'PRODUCT IDENTIFICATION': 'No confirmed SKU'},
            'policy_claims': [],
            'research_sources': [{'id': str(i), 'surface': 'Etsy organic result', 'date': '2026-11-27', 'reference': 'https://example.org/offer/'+str(i), 'observation': 'Selected one matching 6 inch copper head; free shipping.'} for i in range(3)],
            'price_comparables': [{'source_id':str(i),'seller':'seller'+str(i),'option':'6 inch copper head, quantity 1, no arm','placement_status':'organic','placement_evidence':'Full result card and enclosing block observed without ad label.','regular_usd':100+i*10,'sale_usd':None,'shipping_usd':0,'included':True,'reason':'Same diameter/material and head configuration.'} for i in range(3)],
            'price_recommendation': {'suggested_usd':110,'range_usd':[100,120],'regular_median_usd':110,'usable_comparable_count':3,'shipping_basis':'US 10001, verified shipping included','comparison_basis':'delivered','confidence':'moderate'}
        }
    def errors(self):
        return checker.inspect(self.data)[0]
    def test_documented_copy_passes(self):
        self.assertEqual([], self.errors())
    def test_replaced_heading_rejected(self):
        self.data['description']=self.data['description'].replace('FEATURES','KEY FEATURES')
        self.assertTrue(self.errors())
    def test_extra_reference_heading_rejected(self):
        self.data['description']+='\nREFERENCE CODE\nABC123'
        self.assertTrue(self.errors())
    def test_unconfirmed_warranty_rejected(self):
        self.data['description']+='\n5-year warranty (verify before publishing).'
        self.assertTrue(self.errors())
    def test_confirmed_policy_requires_linked_evidence(self):
        claim='A 2-year warranty starts on delivery.'
        self.data['description']+='\n'+claim
        self.data['policy_claims']=[{'text':claim,'source_id':'user','confirmed_by_current_user':True,'scope':'target_shop_product'}]
        self.assertTrue(self.errors())
        self.data['research_sources'].append({'id':'user','surface':'Current-user confirmation','date':'2026-11-27','reference':'Current conversation, dated warranty confirmation','observation':claim})
        self.assertEqual([], self.errors())
    def test_unsupported_shipping_rejected(self):
        self.data['description']+='\nFree US shipping; ships within 48 hours.'
        self.assertTrue(self.errors())
    def test_false_statistics_rejected(self):
        self.data['price_recommendation']['usable_comparable_count']=5
        self.data['price_recommendation']['regular_median_usd']=420
        self.assertTrue(self.errors())
    def test_paid_comparator_rejected(self):
        self.data['price_comparables'][0]['placement_status']='sponsored'
        self.assertTrue(self.errors())
    def test_unknown_shipping_rejected_for_delivered(self):
        self.data['price_comparables'][0]['shipping_usd']=None
        self.assertTrue(self.errors())
    def test_small_sample_median_rejected(self):
        self.data['price_comparables'].pop()
        self.data['price_recommendation']['usable_comparable_count']=2
        self.assertTrue(self.errors())
    def test_provisional_without_comparators(self):
        self.data['price_comparables']=[]
        self.data['price_recommendation'].update(usable_comparable_count=0,regular_median_usd=None,confidence='provisional')
        self.assertEqual([],self.errors())
    def test_missing_sources_rejected(self):
        self.data['research_sources']=[]
        self.assertTrue(self.errors())

if __name__ == '__main__':
    unittest.main()
