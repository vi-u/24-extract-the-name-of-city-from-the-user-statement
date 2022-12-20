# 24-extract-the-name-of-city-from-the-user-statement

>>> Step 4. The final step is to extract the city from the user’s statement 
so you can pass it to the get_weather() function to retrieve the weather from the API call. 

Save previous file w_2_similarity_good.py as  w_3_city_good.py

and

Add the following highlighted for loop to implement this:

    if weather.similarity(statement) >= min_similarity:
      for ent in statement.ents:
        if ent.label_ == "GPE": # GeoPolitical Entity
          city = ent.text
        break

then add test 3 call:

    #test_3
    #Check city name extraction from "statement"
	
    city1 = chatbot("What is the weather in Lima")
    print(city1)  
    
and run this file;

    python w_3_city_good.py

the outcome be like:

    ┌──(my_weather)─(vit㉿acer)-[~]
    └─$ python w_3_city_good.py
    clear sky
    Lima

