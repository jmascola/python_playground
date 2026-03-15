# ITP Week 3 Day 2 Exercise

# import in the two modules for making API calls and parsing the data

import requests
import json

# set a url variable to "https://rickandmortyapi.com/api/character"

url = "https://rickandmortyapi.com/api/character"

# set a variable response to the "get" request of the url

response = requests.get(url)

# print to verify we have a status code of 200

print(response)

print(type(response))

# assign a variable json_data to the responses' json

json_data = response.json()

# print to verify a crazy body of strings!

print(json_data)

# lets make it into a python dictionary by using the appropriate json method (may not be necessary)

python_dict = json.loads(response.text)

# print the newly created python object

print(python_dict)

for item in python_dict.items():
    print(item)
    
    print(python_dict['info']) 
    print(f"There are {python_dict['info']['count']} characters in the Rick and Morty API.") 
    print(python_dict['results'][9]['name']) 
    print(python_dict['results'][9]['origin']['name']) 
    print(f"Let us see who else in there: {python_dict['results'][9]['name']}!") 