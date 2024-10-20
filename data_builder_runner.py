from rich.console import Console
from datetime import datetime

from candles_downloader import CandlesDownloader


def date_to_milliseconds(date: str) -> str:
    """
    Parse date in the following format "YYYY-MM-DDTHH:MM:SSZ" to milliseconds
    """

    # Convert the date string to a datetime object (in UTC)
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M")

    # Convert the datetime to timestamp (in seconds) and then to milliseconds
    milliseconds = int(date_obj.timestamp() * 1000)

    return milliseconds


def generate_data(instructions: dict) -> None:
    """
    Generate data from instructions
    """
    file_name = f"{instructions['symbol']}_{instructions['interval']}_{instructions['date']['start']}_{instructions['date']['end']}.xlsx"

    instructions['date']['start'] = date_to_milliseconds(
        instructions['date']['start'])
    instructions['date']['end'] = date_to_milliseconds(
        instructions['date']['end'])

    candles = CandlesDownloader.get_historical_klines(instructions)

    candles.to_excel(f"candles/{file_name}")
    Console().print("Candles xlsx file generated", style="green")
