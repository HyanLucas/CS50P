import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            response = requests.get("https://blockchain.info/ticker")
            data = {}
            data = response.json()
            bitcoin_usd_value_15m = data["USD"]["15m"]
            print("$", bitcoin_usd_value_15m*float(sys.argv[1]), sep="")
        except ValueError:
            print("Command-line argument is not a number")
    elif len(sys.argv) > 2:
        print("Too many arguments in command-line")
    else:
        print("Missing command-line argument")


main()
