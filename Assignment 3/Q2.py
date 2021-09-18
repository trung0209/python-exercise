def convert_to_krw(currency, amount):
    currency = currency.upper()
    dict_of_currency = {"USD": 1123.46,
                        "EUR": 1336.46,
                        "GBP": 1545.01,
                        "JPY": 10.27}  # Apr 13, 2021, 10:18 UTC

    converted_money = 0

    if currency in dict_of_currency:
        converted_money = float(amount * dict_of_currency[currency])

    if converted_money <= 100000:
        cost_rate = 0.05
        convert_cost = converted_money * cost_rate
        total = convert_cost + converted_money
    elif 100001 < converted_money <= 500000:
        cost_rate = 0.04
        convert_cost = converted_money * cost_rate
        total = convert_cost + converted_money
    elif 500001 < converted_money <= 2000000:
        cost_rate = 0.03
        convert_cost = converted_money * cost_rate
        total = convert_cost + converted_money
    elif 2000001 < converted_money <= 5000000:
        cost_rate = 0.02
        convert_cost = converted_money * cost_rate
        total = convert_cost + converted_money
    else:
        cost_rate = 0.01
        convert_cost = converted_money * cost_rate
        total = convert_cost + converted_money

    print(f"{amount} {currency} --> {converted_money} KRW")
    print(f"Today's rate: {dict_of_currency[currency]}")
    print(f"Conversion cost: {convert_cost}")
    print(f"Final amount: {total}")


print("Welcome to Sejong’s Korean Won Exchange Bank!")
currency_exchange = input("Please input a currency (USD, EUR, GBP, JPY): ")
amount_exchanged = float(input("Please input amount: "))

convert_to_krw(currency_exchange, amount_exchanged)
