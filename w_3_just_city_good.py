import spacy
import requests

nlp = spacy.load("en_core_web_md")

api_key = "7f344331d0b2323597bb5c0818ed1cce"


def chatbot(statement):
    weather = nlp("Current weather in a city")
    statement = nlp(statement)
    min_similarity = 0.70
    
    if weather.similarity(statement) >= min_similarity:
        #pass
        #test_1:
        #similarity = weather.similarity(statement)
        #return similarity
        
        for ent in statement.ents:
            if ent.label_ == "GPE": # GeoPolitical Entity
                city = ent.text
                #break
                return city
            else:
                return "You need to tell me a city to check."      

#test_2:	
	
city1 = chatbot("What is the weather in Kiev")
print(city1)  	
	

