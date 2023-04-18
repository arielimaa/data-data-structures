# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {'USDEUR': 0.85,'GBPEUR': 1.13, 'CHFEUR': 0.86,'EURGBP': 0.885}


def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    original_amount = amount[0]
    original_currency = amount[1]
    rate = original_currency + currency
    
    RATES_list = list(RATES.keys())
    if rate not in RATES_list:
        return None
    else:
        return round(RATES[rate] * original_amount)
