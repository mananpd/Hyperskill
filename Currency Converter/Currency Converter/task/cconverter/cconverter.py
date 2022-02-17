import requests
import json


def my_currency_code():
    return input()


def exchange_currency_code():
    return input()


def input_amount():
    return input()


def get_rate(get_currency_code, receive_currency_code):
    rates = requests.get(f"https://www.floatrates.com/daily/{get_currency_code}.json")
    rates = json.loads(rates.text)
    return rates.get(receive_currency_code.lower())


def make_cache(currency_code, cache_code):
    with open(f"exchange_rate_{cache_code.lower()}.json", "w") as json_file:
        json.dump(get_rate(currency_code, cache_code), json_file)


def check_cache(check_code):
    print("Checking the cache...")
    try:
        with open(f"exchange_rate_{check_code}.json", "r") as file_exchange:
            print("Oh! It is in the cache!")
            return True
    except FileNotFoundError:
        print("Sorry, but it is not in the cache!")
        return False


def convert_from_cache(check_code, convert_amount):
    with open(f"exchange_rate_{check_code}.json", "r") as file_exchange:
        return json.load(file_exchange)['rate'] * convert_amount


def convert_from_web(input_code, output_code, convert_amount):
    rates = get_rate(input_code, output_code)
    return rates['rate'] * convert_amount


in_currency_code = my_currency_code()
cache_codes = ["USD", "EUR"]
for code in cache_codes:
    make_cache(in_currency_code, code)

while True:
    out_currency_code = exchange_currency_code()
    if out_currency_code == "":
        break
    amount = input_amount()
    if amount == "" or amount == "0":
        break
    amount = float(amount)
    in_cache = check_cache(out_currency_code)
    if in_cache:
        converted_amount = convert_from_cache(out_currency_code, amount)
    else:
        converted_amount = convert_from_web(in_currency_code, out_currency_code, amount)
        make_cache(in_currency_code, out_currency_code)
    print(f"You received {str(round(converted_amount, 2))} {out_currency_code}")
