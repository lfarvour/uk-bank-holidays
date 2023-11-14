"""Data classes for UK Holiday data; UKRegion and UKHoliday"""
from datetime import datetime

# DEFINE CONSTANTS
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
