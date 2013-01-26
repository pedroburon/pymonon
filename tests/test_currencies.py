from compatibility import TestCase

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

    def test_default_currency(self):
        expected = Currency('usd', 'US Dollar')

        self.assertEqual(expected, Currency.get_default())

    def test_set_default_currency(self):
        expected = Currency('eur', 'EURO')
        from pymonon import set_default_currency

        set_default_currency(expected)

        self.assertEqual(expected, Currency.get_default())

    def test_set_default_currency_in_currencies(self):
        expected = Currency('xxx', 'XXX')
        from pymonon import set_default_currency, CURRENCIES

        set_default_currency(expected)

        self.assertIn(expected.code, CURRENCIES)

