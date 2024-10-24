# Project Networking

## API Overview
This is a Would You Rather? game where users can play the game itself, add scenarios, and change verbs and nouns in existing scenarios. The API has endpoints to manage scenarios and play the game.



### Model
Scenario: stores the scenarios and their corresponding choices



### Endpoints (you may want to CMD MINUS to see the whole table easier)

| **Endpoint**  	| **Description**                                                                                                                                	| **Parameters**                                                                                                                                            	| **Example**                                        	|
|---------------	|------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------	|----------------------------------------------------	|
| GET/all       	| Returns a list of all the scenarios.                                                                                                           	| none                                                                                                                                                      	| N/A                                                	|
| POST/new      	| Adds a new scenario to the to the database.                                                                                                    	| noun - the first noun in the scenario verb - the verb in the scenario noun2 - the second noun in the scenario happy - is the scenario positive? (boolean) 	| noun: dragon verb: eat noun2: you happy: False     	|
| GET/one       	| Returns the scenario with the given ID.                                                                                                        	| id - the ID of the scenario they want                                                                                                                     	| id: 1                                              	|
| POST/change   	| Changes either the first noun, the second noun, or the verb.                                                                                   	| id - the ID of the scneario wordclass - the word class of the word you wish to change word - what you would like to change the old word to                	| id: 1 change: verb word: chase                     	|
| DELETE/one    	| Deletes the scenario with the given ID.                                                                                                        	| id - the ID of the scenario                                                                                                                               	| id: 1                                              	|
| GET/option    	| Chooses two random scenarios and displays them.                                                                                                	| none                                                                                                                                                      	| N/A                                                	|
| POST/choice   	| Lets the user make a choice between the two given scenarios in GET/option.                                                                     	| id - the ID of the chosen scenario                                                                                                                        	| id: 3                                              	|
| json_response 	| Returns all of the useful properties of the scenario.                                                                                          	| none                                                                                                                                                      	| N/A                                                	|
| change_noun   	| used in POST/change to replace the noun of the scenario.                                                                                       	| new_word                                                                                                                                                  	| new_word: a baby                                   	|
| change_verb   	| Used in POST/change to replace the verb of the scenario.                                                                                       	| new_word                                                                                                                                                  	| new_word: attacks                                  	|
| change_noun2  	| Used in POST/change to replace the second noun of the scenario.                                                                                	| new_word                                                                                                                                                  	| new_word: your family                              	|
| json_options  	| Model: used in GET/option to compare scenarios in a "'scenario' OR 'scenario'" structure.                                                      	| N/A                                                                                                                                                       	| N/A                                                	|
| json_play     	| Mode: used in POST/choose to display the options to choose from.                                                                               	| N/A                                                                                                                                                       	| Would You Rather: eat a burger      OR eat a roach 	|
| json_chosen   	| Model: used in POST/choose to display the response after the user choosen between the scenarios.                                               	| N/A                                                                                                                                                       	| eat a burger (50%)      OR eat a roach (50%)       	|
| increase      	| Model: used in POST/choose to increase the amount of times the scenario had gotten chosen. This is used in json_chosen to display percentages. 	| N/A                                                                                                                                                       	| N/A                                                	|

---

## Setup

poetry shell
banjo --debug

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



