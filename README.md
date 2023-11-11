# But Then There Was Time Now: A Python Project for Cyber Defenders
>This is a python project designed to help cybersecurity defenders learn how to code in Python. It is intended to accompany a talk for the SANS New2Cyber Summit in 2024, should the talk be accepted.

Time is one of the most important concepts for a cyber defender facing an automation task. To know when a thing occurred is to understand its place in the context of the landscape, and as the refrain goes, "one must know a thing to secure a thing."

Not only is time vital for cyber defense automation, it is a pain in the... butt (PITA). This project uses publicly available data, UK Bank Holidays, that is served via an unauthenticated API.

The project asks learners to make an unauthenticated HTTP request to receive API data, parse the data that is returned, and answer various questions that require time manipulation and comparison.

## UK Bank Holidays

### User Story

As a human being who lives in the United States of America, I would like to know more about bank holidays in the United Kingdom. 

I would like to know what holidays are honored by banks, whether they need bunting, and what bunting is (I don't know that the API can answer that for us :) ). 

### Your mission, should you choose to accept it...

Write a python-backed command-line program that allows the user to ask questions about the data.

Some tasks will have related examples. Keep in mind that there are myriad ways the same task can be completed when solving problems using prgoramming languages -- it's parallel to real life implementation of language. Folks have distinct style, teams have dialects, etc.

### Do the Thing

| # | Task | Criteria | Pseudocode Example | Code Example | 
| -- | -- | -- | -- | -- |
| 1 | Retrieve Data | By making an HTTP request using python, retrieve the [UK Bank Holiday API data](https://www.gov.uk/bank-holidays.json) | | |
| 2-1 | Cache Data Locally | Retrieve once and store the data locally; you will develop a program that interacts with local files. | | |
| 2-2 | Store Data Ephemerally | Retrieve data from the API each time the program runs and interact with data stored in volatile (random access) memory. Never write all of the data to the local filesystem directly. | | |
| 2-3 | Cached with Updates | Store data and set criteria for when to check the API using network calls. Consider doing a comparison and only updating holidays that have changed | | |
| 3 | Parse Data for Question Answering | Consider the default data structure -- JSON-parseable text. Implement data parsing to apply structure to raw text. | | |
| 3-1 | Consider Objectifying Data | Before deciding how to structure the data for analysis, consider the questions themselves. | | |
| 4 | Answer Questions about Data | See the list of seed questions. Feel free to formulate your own, as well! | | |

### More, RE: Do the Thing

You are welcome to use the examples linked above before writing your own code, if that is how you like to learn and particularly if you are brand new to development. Reading code is an excellent way to learn code!

I also recommend that you read this whole table, read some of the questions posed about the data, and design your program and data structures previous to writing any code. 

To support the non-code design process with some structure, you can instead write "pseudocode". 

The following pseudocode is highly python aware and intended to help me along with typing inputs and outputs, adding docstrings, etc. It is not required that you write pseudocode so functionally :)

```python
def http_function(input:input_type) -> output_type:
    '''DO STUFF
    
    Args:
        input (input_type): brief description
    Returns:
        output (output_type): brief description'''

    url = "endpoint_url"
    response = get(url)
    return parse(response)
```