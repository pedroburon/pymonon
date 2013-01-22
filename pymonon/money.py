

class CurrencyError(Exception):
    pass


class Currency(object):
    def __init__(self, code, name):
        self.code = code.upper()
        self.name = name

    def __eq__(self, other):
        return self.code == other.code


class Money(object):
    def __init__(self, amount, currency):
        self.amount = amount
        if isinstance(currency, Currency):
            self.currency = currency
        else:
            try:
                self.currency = CURRENCIES[currency]
            except IndexError:
                raise CurrencyError, 'Currency does not exist.'

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

CURRENCIES = {
    'USD': Currency(code='USD', name='US Dollar')
}


def add_currency(currency):
    global CURRENCIES
    CURRENCIES.update({
        currency.code: currency
    })
