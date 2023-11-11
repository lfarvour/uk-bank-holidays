# But Then There Was Time Now: A Python Project for Cyber Defenders
>This is a python project designed to help cybersecurity defenders learn how to code in Python. It is intended to accompany a talk for the SANS New2Cyber Summit in 2024, should the talk be accepted.

Time is one of the most important concepts for a cyber defender facing an automation task. To know when a thing occurred is to understand its place in the context of the landscape, and as the refrain goes, "one must know a thing to secure a thing."

Not only is time vital for cyber defense automation, it is a pain in the... butt (PITA). This project uses publicly available data, UK Bank Holidays, that is served via an unauthenticated API.

The project asks learners to make an unauthenticated HTTP request to receive API data, parse the data that is returned, and answer various questions that require time manipulation and comparison.

## UK Bank Holidays

### User Story

As a human being who lives in the United States of America, I would like to know more about bank holidays i the United Kingdom. 

I would like to know what holidays are honored by banks, whether they need bunting, and what bunting is (though I don't know if the API can answer that for us :) ). 

### Your Mission, should you choose it...

Some tasks below will have related examples. Keep in mind that there are myriad ways the same task can be completed when solving problems using prgoramming languages -- it's parallel to real life implementation of language. Folks have distinct style, teams have dialects, etc.

You are welcome to use the examples below before writing your own code, if that works for your learning and particularly if you are brand new to development. Reading code is an excellent way to learn code!

| # | Task | Criteria | Unstick Yourself - Example |
| -- | -- | -- | -- |
| 1 | Retrieve Data | By making an HTTP request using python, retrieve the [UK Bank Holiday API data](https://www.gov.uk/bank-holidays.json) | |
| 2-1 | Cache Data Locally | Retrieve once and store the data locally; you will develop a program that interacts with local files. | |
| 2-2 | Store Data Ephemerally | Retrieve data from the API each time the program runs and interact with data stored in volatile (random access) memory. Never write all of the data to the local filesystem directly. | |
| 2-3 | Cached with Updates | Store data and set criteria for when to check the API using network calls. Consider doing a comparison and only updating holidays that have changed | |
| 3 | Answer Questions about Data | |

