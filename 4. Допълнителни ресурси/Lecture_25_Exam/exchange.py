def main():
    try:
        exchange_rates_fn = input()
        amounts_fn = input()

        exchange_rates = load_exchange_rates(exchange_rates_fn)
        amounts = load_amounts(amounts_fn)
        for currency, amount in amounts:
            if currency not in exchange_rates:
                raise Exception('Currency not found')
            amount_in_bgn = amount / exchange_rates[currency]
            print("{:.2f}".format(amount_in_bgn))
    except:
        print("INVALID INPUT")


def load_exchange_rates(fn: str) -> dict:
    """
    Expected format of input file:
        USD 0.57276
        EUR 0.5111
    :param fn:
    :return:
    """
    result = {}
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_parts = line.split(' ')
                # if the number of items in the list is != 2,
                # the following will raise an error
                currency, rate = line_parts
                rate = float(rate)
                result[currency] = rate
    return result


def load_amounts(fn: str) -> list:
    """
    Amounts must be loaded in a list, because the order
    in which the results are output is significant

        623.83 USD
        572.53 EUR
        12 CHF
        1182.08 AUD
        24 CHF

    :param fn:
    :return: list of tuples - (currency, amount)
    """
    result = []
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_parts = line.split(' ')
                # if the number of items in the list is != 2,
                # the following will raise an error
                amount, currency = line_parts
                amount = float(amount)
                result.append((currency, amount))
    return result

if __name__ == '__main__':
    main()