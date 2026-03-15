# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]

# 1a. Create a function that takes a single string value and returns the desired dictionary

def create_user_dict(user_list):
    user_list = []
    for index, name in enumerate(users_list, start=0):
        user_dict = {"user_id": index, "name": name}
        user_list.append(user_dict)
    return user_list

print(create_user_dict(users_list))

# 1b. Create a new empty list called users_dict_list

users_dict_list = []

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list

for user in users_list:
    users_dict_list.append(create_user_dict([user])[0])

# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?

from mock_data import mock_data

# 2a. retrieve the gender of Morty Smith

for character in mock_data["results"]:
    if character["name"] == "Morty Smith":
        print(f"Gender of Morty Smith: {character['gender']}")

# 2b. retrieve the length of the Rick Sanchez episodes

for character in mock_data["results"]:
    if character["name"] == "Rick Sanchez":
        print(f"Length of Rick Sanchez episodes: {len(character['episode'])}")

# 2c. retrieve the url of Summer Smith location

for character in mock_data["results"]:
    if character["name"] == "Summer Smith":
        print(f"URL of Summer Smith location: {character['location']['url']}")