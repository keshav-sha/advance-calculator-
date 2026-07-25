import requests


class CurrencyConverter:

    BASE_URL = "https://api.frankfurter.app/latest"
    CURRENCY_URL = "https://api.frankfurter.app/currencies"

    @staticmethod
    def convert(amount: float, from_currency: str, to_currency: str):

        params = {
            "amount": amount,
            "from": from_currency.upper(),
            "to": to_currency.upper()
        }

        try:
            response = requests.get(
                CurrencyConverter.BASE_URL,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            if "rates" not in data:
                raise ValueError("Invalid currency code.")

            return {
                "amount": amount,
                "from": from_currency.upper(),
                "to": to_currency.upper(),
                "converted_amount": list(data["rates"].values())[0]
            }

        except requests.exceptions.RequestException:
            raise ValueError("Unable to connect to the currency server.")

    @staticmethod
    def supported_currencies():

        try:
            response = requests.get(
                CurrencyConverter.CURRENCY_URL,
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            raise ValueError("Unable to fetch currency list.")