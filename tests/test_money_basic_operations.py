from unittest import TestCase

from pymonon import Money


class TestBasicOperationsSameCurrency(TestCase):

    def test_cmp(self):
        money1 = Money(1000, 'usd')
        money2 = Money(2000, 'usd')

        self.assertGreater(money2, money1)

    def test_cmp_not_money(self):
        money = Money(1000, 'usd')
        other = 100

        with self.assertRaisesRegexp(TypeError, r"^You can only compare Money instances.$"):
            money < other

    def test_eq(self):
        money1 = Money(1000, 'usd')
        money2 = Money(1000, 'usd')

        self.assertEqual(money1, money2)

    def test_add(self):
        money1 = Money(1000, 'usd')
        money2 = Money(2000, 'usd')
        result = Money(3000, 'usd')

        self.assertEqual(result, money1 + money2)

    def test_add_not_money(self):
        money = Money(1000, 'usd')
        other = 100

        with self.assertRaisesRegexp(TypeError, r"^You can only add Money instances.$"):
            money + other

    def test_sub(self):
        money1 = Money(1000, 'usd')
        money2 = Money(2000, 'usd')
        result = Money(-1000, 'usd')

        self.assertEqual(result, money1 - money2)

    def test_sub_not_money(self):
        money = Money(1000, 'usd')
        other = 100

        with self.assertRaisesRegexp(TypeError, r"^You can only substract Money instances.$"):
            money - other

    def test_mul_scalar(self):
        money = Money(2000, 'usd')
        scalar = 2.5
        result = Money(5000, 'usd')

        self.assertEqual(result, money * scalar)

    def test_mul_money(self):
        money = Money(1000, 'usd')
        other = Money(2000, 'usd')

        with self.assertRaisesRegexp(TypeError, r"^You cannot multiply Money values.$"):
            money * other

    def test_div_scalar(self):
        money = Money(5000, 'usd')
        scalar = 2.5
        result = Money(2000, 'usd')

        self.assertEqual(result, money / scalar)

    def test_div_money(self):
        money = Money(1000, 'usd')
        other = Money(2000, 'usd')

        with self.assertRaisesRegexp(TypeError, r"^You cannot divide Money values.$"):
            money / other


class TestBasicDifferentCurrency(TestCase):
    def setUp(self):
        self.money = Money(1000, 'usd')
        self.other = Money(2000, 'eur')

    def test_cmp_currency_mismatch(self):
        self.money = Money(1000, 'usd')
        self.other = Money(2000, 'eur')

        with self.assertRaisesRegexp(AssertionError, r"^Currency mismatch.$"):
            self.money < self.other

    def test_add_currency_mismatch(self):
        self.money = Money(1000, 'usd')
        self.other = Money(2000, 'eur')

        with self.assertRaisesRegexp(AssertionError, r"^Currency mismatch.$"):
            self.money + self.other

    def test_sub_currency_mismatch(self):
        self.money = Money(1000, 'usd')
        self.other = Money(2000, 'eur')

        with self.assertRaisesRegexp(AssertionError, r"^Currency mismatch.$"):
            self.money - self.other