from unittest import TestCase

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
    		money = Money(1000, 'notexist')
