# Porpoise
The purpose of this tool is to allow a U.S. user to ask and answer questions about U.K. holidays using the U.K. holidays API.'''

# Data

__Structure of data retrieved from API:__ `json`

```json
{
    "named_region": {
        "division": "division",
        "events": [
            {"title": "title",
            "date": "date",
            "notes": "notes",
            "bunting": false}
        ]
    }
}
```

# Notes

* There will be named regions at the parent level of the JSON returned from the API
* Date format is standard as YYYY-MM-DD
* There may be notes; not clear if this is user defined
* Bunting contains a boolean value; this will likely cause translation issues in Python due to capitalization in json bool vs python bool (true/false vs. True/False)

## Initial implementation 

* Rediscovered class decorators; @property finally clear! Used to enable accessing the value returned by the function as if it is a property. All thanks to Don, my senior dev and spouse.