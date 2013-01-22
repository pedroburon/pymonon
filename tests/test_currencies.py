from unittest import TestCase

from pymonon import Currency


class ImportCurrenciesTest(TestCase):
    def test_import(self):
        from pymonon import CURRENCIES
        
        self.assertIsInstance(CURRENCIES, dict)

    def test_add_currency(self):
        from pymonon import add_currency
        currency = Currency('newcurrency', 'new currency')
        add_currency(currency)
        from pymonon import CURRENCIES

        self.assertIn('NEWCURRENCY', CURRENCIES)
        self.assertEqual(CURRENCIES['NEWCURRENCY'], currency)