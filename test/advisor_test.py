import os

from app.robo_advisor import to_usd, write_to_csv

def test_to_usd():
    assert to_usd(123456.8) == "$123,456.80"

def test_write_to_csv():

    # SETUP

    parsed_response = [
        {'date': '2018-06-08', 'open': '101.0924', 'high': '101.9500', 'low': '100.5400', 'close': '101.6300', 'volume': '22165128'},
        {'date': '2018-06-07', 'open': '102.6500', 'high': '102.6900', 'low': '100.3800', 'close': '100.8800', 'volume': '28232197'},
        {'date': '2018-06-06', 'open': '102.4800', 'high': '102.6000', 'low': '101.9000', 'close': '102.4900', 'volume': '21122917'},
        {'date': '2018-06-05', 'open': '102.0000', 'high': '102.3300', 'low': '101.5300', 'close': '102.1900', 'volume': '23514402'},
        {'date': '2018-06-04', 'open': '101.2600', 'high': '101.8600', 'low': '100.8510', 'close': '101.6700', 'volume': '27281623'},
        {'date': '2018-06-01', 'open': '99.2798', 'high': '100.8600', 'low': '99.1700', 'close': '100.7900', 'volume': '28655624'}
    ]

    csv_filepath = os.path.join(os.path.dirname(__file__), "example_reports", "temp_prices.csv")

    if os.path.isfile(csv_filepath):
        os.remove(csv_filepath)

    # INVOCATION

    result = write_to_csv(parsed_response, csv_filepath)

    # EXPECTATIONS

    assert result == True
    assert os.path.isfile(csv_filepath) == True
