import os


def fill_zeros(symbol):
    length = len(symbol)
    fill = 4 - length
    symbol = '0' * fill + symbol
    return symbol


def main():
    here = os.path.dirname(__file__)
    with open(os.path.join(here, 'currencies.csv'), 'r') as csv:
        with open(os.path.join(here, 'pymonon', 'currencies.py'), 'w') as module:
            module.write('# Module created by currencies_to_module.py from currencies.csv\n\n')
            module.write('CURRENCIES_CODES = (\n')
            first = True
            for line in csv.readlines():
                if first:
                    first = False
                    continue
                name, code, symbols, decimals= map(lambda x: x.strip(), line.strip().split(';'))
                symbol = map(lambda x: x.strip(), symbols.split(','))
                symbol = map(fill_zeros, symbol)
                symbol = map(lambda x: '\\u' + x, symbol)
                symbol = reduce(lambda x, y: x + y, symbol, '')
                module.write("\t(\"%s\", \"%s\", u\"%s\", %s),\n" % (name, code, symbol, decimals))
            module.write(')\n')

    from pymonon.currencies import CURRENCIES_CODES

    for currency in CURRENCIES_CODES:
        print u"%s, %s, %s, %s" % currency

if __name__ == '__main__':
    main()
