# app/robo_advisor.py

import csv
import datetime
import json
import os

from dotenv import load_dotenv
import requests

load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", "demo") # default to using the "demo" key if an Env Var is not supplied

def get_response(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def transform_response(parsed_response):
    # parsed_response should be a dictionary representing the original JSON response
    # it should have keys: "Meta Data" and "Time Series Daily"
    tsd = parsed_response["Time Series (Daily)"]

    rows = []
    for date, daily_prices in tsd.items(): # see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/dictionaries.md
        row = {
            "timestamp": date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)

    return rows

def write_to_csv(rows, csv_filepath):
    # rows should be a list of dictionaries
    # csv_filepath should be a string filepath pointing to where the data should be written

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for row in rows:
            writer.writerow(row)

    return True

def to_usd(my_price):
    # utility function to convert float or integer to usd-formatted string (for printing)
    return "${0:,.2f}".format(my_price) #> $12,000.71

if __name__ == "__main__":

    time_now = datetime.datetime.now() #> datetime.datetime(2019, 3, 3, 14, 44, 57, 139564)

    #
    # INFO INPUTS
    #

    symbol = input("Please specify a stock symbol (e.g. AMZN) and press enter: ")

    parsed_response = get_response(symbol)

    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

    rows = transform_response(parsed_response)

    latest_close = rows[0]["close"]
    high_prices = [row["high"] for row in rows] # list comprehension for mapping purposes!
    low_prices = [row["low"] for row in rows] # list comprehension for mapping purposes!
    recent_high = max(high_prices)
    recent_low = min(low_prices)

    #
    # INFO OUTPUTS
    #

    # WRITE PRICES TO CSV FILE

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

    write_to_csv(rows, csv_filepath)

    # DISPLAY RESULTS

    formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S") #> '2019-03-03 14:45:27'

    formatted_csv_filepath = csv_filepath.split("../")[1] #> data/prices.csv

    print("-------------------------")
    print(f"SYMBOL: {symbol}")
    print("-------------------------")
    print(f"REQUEST AT: {formatted_time_now}")
    print(f"REFRESH DATE: {last_refreshed}")
    print("-------------------------")
    print(f"RECENT HIGH:  {to_usd(recent_high)}")
    print(f"LATEST CLOSE: {to_usd(latest_close)}")
    print(f"RECENT LOW:   {to_usd(recent_low)}")
    print("-------------------------")
    print("RECOMMENDATION: TODO") # TODO
    print("BECAUSE: TODO") # TODO
    print(f"WRITING DATA TO CSV: {formatted_csv_filepath}")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")
