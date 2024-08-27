def exchange_rates():
    return {
        'USD': {'INR': 83.94, 'EUR': 0.91},
        'EUR': {'USD': 1.10, 'INR': 92.30},
        'INR': {'USD': 0.012, 'EUR': 0.01}
    }

def convert(currency1, currency2, amount):
    rates = exchange_rates()

    if currency1 in rates and currency2 in rates[currency1]:
        rate = rates[currency1][currency2]
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount.")
            return

        converted_amount = rate * amount
        print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
        return converted_amount
    else:
        print("Exchange rate not available for the given currencies.")

def main():
    print("Welcome to the currency converter!")

    currency1 = input("Enter the base currency (e.g., USD, EUR, INR): ").upper()
    amount = input(f"Enter the amount in {currency1}: ")
    currency2 = input("Enter the currency to convert to (e.g., USD, EUR, INR): ").upper()

    convert(currency1, currency2, amount)

main()
