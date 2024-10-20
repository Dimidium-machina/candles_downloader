

# CANDLES DOWNLOADER


This is a fragment from Dimidium/Light-backtester

Able to download candles from:

- Binance



## HOW TO RUN

Create the virtual environment using virtualenv

> virtualenv .env

Install dependencies

> pip install -r requirements.txt

Start the virtual environment

> source .env/Scripts/activate

Run the program

> python run.py



# HOW TO CONFIG

Update the instructions.py to change the parameters used to download the candles

``` json

candles_params = {
    "symbol": "BTCUSDT",
    "interval": "5m", // 5m, 15m, 1h, 4h ...
    "date": {
        "start": "2023-01-01T00:00", // format YYYY-mm-ddThh:mm
        "end": "2023-12-31T23:00"
    }
}


```

All candles generated will be storaged in the folder ./candles
