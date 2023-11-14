"""Main logic for uk-bank-holidays command line tool."""
import json
import requests

from pathlib import Path
from datetime import datetime

# Imports for data typing
from pathlib import PosixPath

# DEFINE CONSTANTS
UK_HOLIDAY_ENDPOINT = "https://www.gov.uk/bank-holidays.json"
HOLIDAY_DATE_FORMAT = "%Y-%m-%d"


class UkHoliday():
    def __init__(self, title:str, date:str, notes:str, bunting:bool):
        self.title = title
        self.date = datetime.strptime(date, HOLIDAY_DATE_FORMAT)
        self.notes = notes
        self.bunting = bunting
    
class UkRegion():
    def __init__(self, region:str, events:list):
        self.name = region
        self.events = self._store_events(events)

    def _store_events(self, events:list) -> list:
        """Converts list of json to list of UkHoliday objects."""
        event_list = []
        for event in events:
            event_list.append(UkHoliday(event.get("title"), event.get("date"), event.get("notes"), event.get("bunting")))
        return event_list
    
    @property
    def first_holiday(self):
        """Returns the earliest holiday celebrated for the year in the region."""
        earliest_event = None
        for event in self.events:
            if not earliest_event:
                earliest_event = event
            elif earliest_event.date > event.date:
                earliest_event = event
        return earliest_event
    
    @property
    def last_holiday(self):
        """Returns the latest holiday celebrated for the year in the region."""
        latest_event = None
        for event in self.events:
            if not latest_event:
                latest_event = event
            elif latest_event.date < event.date:
                latest_event = event
        return latest_event
    


def get_holidays_by_http(cache_path: PosixPath) -> None:
    """
    Read data from the API endpoint defined in constants; write it to local cache.

    :param cache_path: path to holiday data
    :type cache_path: PosixPath
    """
    data = requests.get(UK_HOLIDAY_ENDPOINT)
    # Store data in a local cache
    with open(cache_path, "+w", encoding="utf-8") as local_cache:
        # Write the text of the HTTPResponse object to file
        local_cache.write(data.text)
        print(f"Wrote data to {local_cache}")


def main():
    """Primary handling logic."""

    # Parse command line arguments

    # Check for a local cache of data
    cwd = Path.cwd()
    cache_path = Path(cwd, "uk-bank-holidays", "uk_holiday_data.json")
    
    # TODO: How often should local cache be refreshed?
    if not cache_path.exists():
        # Retrieve data if no local cache is available
        get_holidays_by_http(cache_path)
    
    with open(cache_path, "r", encoding="utf-8") as local_cache:
        try:
            holiday_data = json.loads(local_cache.read())
        except Exception:
            print("Data retrieval from local cache failed. Retrieving data from API...")
        
    # Build regional event objects
    regions = []
    for region in holiday_data.keys():
        regions.append(UkRegion(region, holiday_data.get(region).get("events")))
    
    # Handle command line inputs.


if __name__ == "__main__":
    main()
