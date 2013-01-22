# encoding=UTF-8
from pymonon.currencies import CURRENCIES_CODES

__version__ = '0.0.1'


class CurrencyError(Exception):
    pass


class Currency(object):
    def __init__(self, code, name, symbol=u'$'):
        self.code = code.upper()
        self.name = name
        self.symbol = symbol

    def __eq__(self, other):
        return self.code == other.code

    @staticmethod
    def get_default():
        return DEFAULT_CURRENCY

    def __unicode__(self):
        return unicode(self.symbol)


class Money(object):
    def __init__(self, amount, currency=None):
        self.__set_currency(currency)
        self.amount = amount

    def __set_currency(self, currency):
        if currency is None:
            self.currency = Currency.get_default()
        elif isinstance(currency, Currency):
            self.currency = currency
        elif isinstance(currency, basestring) and currency.upper() in CURRENCIES:
            self.currency = CURRENCIES[currency.upper()]
        else:
            raise CurrencyError('Currency does not exist.')

    def __cmp__(self, other):
        if not isinstance(other, Money):
            raise TypeError("You can only compare Money instances.")
        assert self.currency == other.currency, "Currency mismatch."

        return self.amount - other.amount

    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("You can only add Money instances.")
        assert self.currency == other.currency, "Currency mismatch."

        amount = self.amount + other.amount
        return Money(amount, currency=self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError("You can only substract Money instances.")
        assert self.currency == other.currency, "Currency mismatch."

        amount = self.amount - other.amount
        return Money(amount, currency=self.currency)

    def __mul__(self, other):
        if isinstance(other, Money):
            raise TypeError("You cannot multiply Money values.")
        amount = self.amount * other
        return Money(amount, currency=self.currency)

    def __div__(self, other):
        if isinstance(other, Money):
            raise TypeError("You cannot divide Money values.")
        amount = self.amount / other
        return Money(amount, currency=self.currency)

    def __unicode__(self):
        return u'%s%s' % (self.currency, self.amount)


def set_default_currency(currency):
    global DEFAULT_CURRENCY
    add_currency(currency)
    DEFAULT_CURRENCY = currency


def add_currency(currency):
    global CURRENCIES
    CURRENCIES.update({
        currency.code: currency
    })

CURRENCIES = {}

for name, code, symbol in CURRENCIES_CODES:
    add_currency(Currency(code=code, name=name, symbol=symbol))

DEFAULT_CURRENCY = CURRENCIES['USD']
