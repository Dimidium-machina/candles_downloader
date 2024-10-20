import pandas as pd
import ccxt
import collections


class CandlesDownloader:

    # BINGX
    '''
    def get_historical_klines(candles_params: dict) -> pd.DataFrame:
        """

        Get historical klines from binance

        Args:
            candles_params (dict):
                symbol (str): symbol to get candles
                interval (str): interval to get candles
                date (dict): start and end date to get candles
                    start (str): start date in milliseconds
                    end (str): end date in milliseconds

        """
        limit = 1000
        binance = ccxt.bingx()
        symbol = candles_params['symbol']
        interval = candles_params['interval']
        start_date = candles_params['date']['start']
        end_date = candles_params['date']['end']
        pending_klines = True
        ohlcv_list = collections.deque([])

        while pending_klines:
            ohlcv_last = binance.fetch_ohlcv(
                symbol, interval, since=start_date, limit=limit)

            if len(ohlcv_last) == 0:
                print("No candles got from binance")
                pending_klines = False
                continue

            ohlcv_list.extend(ohlcv_last)
            if len(ohlcv_list) < limit:
                pending_klines = False
                # print("ohlc_last: ", ohlcv_list)
                continue

            # Adding 60 seconds to prevent duplicate data
            start_date = ohlcv_list[-1][0] + 60
            if end_date is not None and start_date >= end_date:
                pending_klines = False

        if len(ohlcv_list) == 0:
            print("No candles got from binance")
            return pd.DataFrame()

        columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']
        candles = pd.DataFrame(list(ohlcv_list), columns=columns, dtype=float)
        return candles'''


    # BINANCE
    def get_historical_klines(candles_params: dict) -> pd.DataFrame:
        """

        Get historical klines from binance

        Args:
            candles_params (dict):
                symbol (str): symbol to get candles
                interval (str): interval to get candles
                date (dict): start and end date to get candles
                    start (str): start date in milliseconds
                    end (str): end date in milliseconds

        """
        limit = 1000
        binance = ccxt.binance()
        symbol = candles_params['symbol']
        interval = candles_params['interval']
        start_date = candles_params['date']['start']
        end_date = candles_params['date']['end']
        pending_klines = True
        ohlcv_list = collections.deque([])
        
        while pending_klines:
            ohlcv_last = binance.fetch_ohlcv(symbol, interval, since=start_date, limit=limit)
            
            if len(ohlcv_last) == 0:
                print("No candles got from binance")
                pending_klines = False
                continue
            
            ohlcv_list.extend(ohlcv_last)
            if  len(ohlcv_list) < limit:
                pending_klines = False
                #print("ohlc_last: ", ohlcv_list)
                continue
            
            start_date = ohlcv_list[-1][0] + 60  # Adding 60 seconds to prevent duplicate data
            if end_date is not None and start_date >= end_date:
                pending_klines = False
        
        if len(ohlcv_list) == 0:
            print("No candles got from binance")
            return pd.DataFrame()
        
        columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']
        candles = pd.DataFrame(list(ohlcv_list), columns=columns, dtype=float)
        return candles