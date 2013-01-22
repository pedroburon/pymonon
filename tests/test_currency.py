from unittest import TestCase

from pymonon import Currency


class CurrencyTest(TestCase):
    def test_create_instance(self):
        currency = Currency(code='usd', name='US Dollar')
        self.assertIsInstance(currency, Currency)
        self.assertEqual('USD', currency.code)
        self.assertEqual('US Dollar', currency.name)

    def test_equal(self):
        currency1 = Currency('usd', name='US Dollar')
        currency2 = Currency('Usd', name='Dollar')

        self.assertEqual(currency1, currency2)

    def test_not_equal(self):
        currency1 = Currency('usd', name='US Dollar')
        currency2 = Currency('clp', name='Chile Peso')

        self.assertNotEqual(currency1, currency2)
