# app/robo_advisor.py

import csv
import json
import os

from dotenv import load_dotenv
import requests

load_dotenv() #> loads contents of the .env file into the script's environment

# utility function to convert float or integer to usd-formatted string (for printing)
# ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

#
# INFO INPUTS
#

# ASSEMBLE REQUEST URL

api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "demo") # default to using the "demo" key if an Env Var is not supplied

symbol = "MSFT" # TODO: accept user input

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

# ISSUE REQUEST AND PARSE RESPONSE

response = requests.get(request_url)
parsed_response = json.loads(response.text)
metadata = parsed_response["Meta Data"]
tsd = parsed_response["Time Series (Daily)"]

last_refreshed = metadata["3. Last Refreshed"]

# TRANSFORM DATA INTO A MORE FAMILIAR / USABLE STRUCTURE (LIST OF DICTIONARIES :-D)

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

# breakpoint()
# (pdb) rows[0]
#> {'timestamp': '2019-02-20', 'open': 107.86, 'high': 107.94, 'low': 106.295, 'close': 107.15, 'volume': 21604807}
latest_close = rows[0]["close"]

high_prices = [row["high"] for row in rows] # list comprehension for mapping purposes!
low_prices = [row["low"] for row in rows] # list comprehension for mapping purposes!
recent_high = max(high_prices)
recent_low = min(low_prices)

#
# INFO OUTPUTS
#

# WRITE PRICES TO CSV FILE
# see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/csv.md#writing-csv-files

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") # see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_filepath, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for row in rows:
        writer.writerow(row)

# DISPLAY RESULTS

printable_csv_filepath = csv_filepath.split("../")[1] #> data/prices.csv

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT: 2018-02-20 14:00") # TODO: dynamic datetime
print("-------------------------")
print(f"LAST REFRESH: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!") # TODO
print("BECAUSE: TODO") # TODO
print("-------------------------")
print(f"WRITING DATA TO CSV: {printable_csv_filepath}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
