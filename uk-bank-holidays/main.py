"""Main logic for uk-bank-holidays command line tool."""
import json
import requests
import argparse

from pathlib import Path

# Imports for data typing
from pathlib import PosixPath
from argparse import ArgumentParser
from typing import Union

# Local imports
from models.uk_holidays import UkRegion

# DEFINE CONSTANTS
UK_HOLIDAY_ENDPOINT = "https://www.gov.uk/bank-holidays.json"
OUTPUT_DATE_FORMAT = "%b %d"



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
        

def load_holiday_data(region=None) -> list:
    """
    Retrieve holiday data from local cache or API and objectify.

    :return: list of objectified regions with event data
    :rtype: list
    """
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
    for region_name in holiday_data.keys():
        if region == region_name:
            regions.append(UkRegion(region_name, holiday_data.get(region).get("events")))
            break
        elif not region:
            regions.append(UkRegion(region_name, holiday_data.get(region).get("events")))
    return regions


def list_holiday_data(args: dict) -> None:
    """
    Perform list function based on specified args.

    :param args: command line arguments
    :type args: dict
    """
    if args.region:
        holidays = load_holiday_data(args.region)
    else:
        holidays = load_holiday_data()
    # If a region is specified, only look at a single holiday
    for region in holidays:
        if args.bunting:
            for event in region.events:
                if event.bunting:
                    print(f"Region: {region.name} | Date: {event.date.strftime(OUTPUT_DATE_FORMAT)} | Holiday: {event.title}")
    
        

def parse_args() -> ArgumentParser:
    """
    Parse command line arguments

    :return: parsed command line arguments
    :rtype: ArgumentParser
    """
    parser = argparse.ArgumentParser(prog="UK Bank Holidays")

    subparsers = parser.add_subparsers(help="sub-command assistance")
    
    parser_list = subparsers.add_parser("list", help="List information about UK Bank Holiday data.")
    parser_list.add_argument("--bunting", action="store_true", help="List all bunting holidays. If --region is not specified, list all bunting holiday for all regions.")
    parser_list.add_argument("-r", "--region", action="store", choices=["england-and-wales","scotland","northern-ireland"], help="Perform subcommand only for the specified region.")
    parser_list.set_defaults(func=list_holiday_data)
    
    return parser.parse_args()


def main():
    """Primary handling logic."""
    
    # Parse command line arguments; handles function calls for subcommands
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
