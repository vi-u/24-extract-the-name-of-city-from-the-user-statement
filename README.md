# 24-extract-the-name-of-city-from-the-user-statement

>>> Step 4. The final step is to extract the city from the user’s statement 
so you can pass it to the get_weather() function to retrieve the weather from the API call. 

To do this, you’re using spaCy’s named entity recognition feature. A named entity is a real-world noun that has a name, like a person, or in our case, a city. You want to extract the name of the city from the user’s statement.

To extract the city name, you get all the named entities in the user’s statement and check which of them is a geopolitical entity (country, state, city). To do this, you loop through all the entities spaCy has extracted from the statement in the ents property, then check whether the entity label (or class) is “GPE” representing Geo-Political Entity. If it is, then you save the name of the entity (its text) in a variable called city.

Save previous file w_2_similarity_good.py as  w_3_city_good.py


Add the following  "for loop" to implement this:

    if weather.similarity(statement) >= min_similarity:
      for ent in statement.ents:
        if ent.label_ == "GPE": # GeoPolitical Entity
          city = ent.text
        break

You also need to catch cases where no city was entered by adding an "else block":

import spacy

...

def chatbot(statement):
  weather = nlp("Current weather in a city")
  statement = nlp(statement)
  min_similarity = 0.75

  if weather.similarity(statement) >= min_similarity:
    for ent in statement.ents:
      if ent.label_ == "GPE": # GeoPolitical Entity
        city = ent.text
        break
      else:
        return "You need to tell me a city to check."



and


then add test 3 call:

    #test_3
    #Check city name extraction from "statement"
	
    city1 = chatbot("What is the weather in Lima")
    print(city1)  
    
and run this file;

    python w_3_city_good.py

the outcome be like:

    ┌──(my_env_weather)─(user㉿acer)-[~]
    └─$ python w_3_city_good.py
    clear sky
    Lima

