EXCHANGE_RATES = {
    "USD": 1,
    "ZAR": 19.5,
    "EUR": 0.92
}

def convert(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    usd_amount = amount / EXCHANGE_RATES[from_currency]
    return round(usd_amount * EXCHANGE_RATES[to_currency], 2)
