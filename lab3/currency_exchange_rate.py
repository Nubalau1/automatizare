import requests
import sys
import json
import os
import datetime as dt


def log_error(message: str):
    with open("error.log", "a", encoding="utf-8") as f:
        f.write(f"{dt.datetime.now()} - {message}\n")


if len(sys.argv) != 4:
    error_msg = "Nu sunt destui parametri"
    log_error(error_msg)
    sys.exit(error_msg)

from_currency = sys.argv[1].lower()
to_currency = sys.argv[2].lower()

data = sys.argv[3]
today = dt.date.today()

try:
    date_obj = dt.datetime.strptime(data, "%Y-%m-%d").date()
    if date_obj >= today:
        raise ValueError("Data nu este valida: trebuie sa fie mai mica decat ziua de azi")
except ValueError:
    error_msg = "Data nu este valida: Formatul necesar YYYY-MM-DD si trebuie sa fie mai mica decat ziua de azi"
    print(error_msg)
    log_error(error_msg)
    sys.exit(1)

directory_path = "data"


url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{data}/v1/currencies/{from_currency}.json"
response = requests.get(url)

if response.status_code != 200:
    error_msg = f"Moneda de bază '{from_currency}' nu există în baza de date."
    print(error_msg)
    log_error(error_msg)
    sys.exit(1)


formated_information = response.json()

if to_currency not in formated_information.get(from_currency, {}):
    error_msg = f"Moneda țintă '{to_currency}' nu este disponibilă pentru conversie din '{from_currency}'."
    print(error_msg)
    log_error(error_msg)
    sys.exit(1)

data_to_save = {
    "data": data,
    f"{to_currency}": formated_information[from_currency][to_currency]
}

os.makedirs(directory_path, exist_ok=True)

with open(f"{directory_path}/{from_currency}_{to_currency}_{data}.json", "w") as json_file:
    json.dump(data_to_save, json_file, separators=(', ', ': '))
