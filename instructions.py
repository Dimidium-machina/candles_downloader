
"""

Edit the following parameters to get the desired data from Binance API.

symbol (string):  symbol to get candles
interval (string): interval to get candles
date (dict): start and end date to get candles
    start (string): start date of the candles in the following format "YYYY-MM-DDTHH:MM" 
    end (string): end date of the candles in the following format "YYYY-MM-DDTHH:MM" 

"""

candles_params = {
    "symbol": "BTCUSDT",
    "interval": "5m",
    "date": {
        "start": "2023-11-01T00:00",
        "end": "2023-12-31T23:00"
    }
}
