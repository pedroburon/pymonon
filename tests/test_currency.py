# encoding=UTF-8
from compatibility import CompatibilityTestCase

from pymonon import Currency, CURRENCIES


class CurrencyTest(CompatibilityTestCase):
    def test_create_instance(self):
        currency = Currency(code='usd', name='US Dollar', symbol=u'$P', decimals=1)
        self.assertIsInstance(currency, Currency)
        self.assertEqual('USD', currency.code)
        self.assertEqual('US Dollar', currency.name)
        self.assertEqual(u'$P', currency.symbol)
        self.assertEqual(1, currency.decimals)

    def test_create_instance_default_symbol(self):
        currency = Currency(code='usd', name='US Dollar')
        self.assertIsInstance(currency, Currency)
        self.assertEqual('USD', currency.code)
        self.assertEqual('US Dollar', currency.name)
        self.assertEqual(u'$', currency.symbol)

    def test_create_instance_default_decimals(self):
        currency = Currency(code='usd', name='US Dollar')
        self.assertIsInstance(currency, Currency)
        self.assertEqual(2, currency.decimals)

    def test_equal(self):
        currency1 = Currency('usd', name='US Dollar')
        currency2 = Currency('Usd', name='Dollar')

        self.assertEqual(currency1, currency2)

    def test_not_equal(self):
        currency1 = Currency('usd', name='US Dollar')
        currency2 = Currency('clp', name='Chile Peso')

        self.assertNotEqual(currency1, currency2)

    def test_unicode(self):
        currency = CURRENCIES['UZS']

        self.assertEqual(u'лв', unicode(currency))
