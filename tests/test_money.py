# encoding=UTF-8
from __future__ import with_statement
from compatibility import TestCase

from pymonon import Currency, Money, CurrencyError, CURRENCIES


class MoneyTest(TestCase):
    def test_initialize(self):
    	currency = CURRENCIES['USD']
        money = Money(1000, 'usd')

        self.assertIsInstance(money, Money)
        self.assertEqual(currency, money.currency)

    def test_initialize_with_currency(self):
    	currency = CURRENCIES['USD']
    	money = Money(1000, currency)

    	self.assertEqual(currency, money.currency)

    def test_initialize_with_inexistent_currency_code(self):
    	with self.assertRaisesRegexp(CurrencyError, 'Currency does not exist.'):
            Money(1000, 'notexist')

    def test_initialize_without_currency(self):
        money = Money(1000)

        self.assertEqual(Currency.get_default(), money.currency)

    def test_unicode(self):
        money = Money(1000, 'UZS')

        self.assertEqual(u'лв1000', unicode(money))


