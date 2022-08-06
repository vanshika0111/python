import json
from difflib import get_close_matches

data = json.load(open("data.json"))
# print(data)
# print(data["air"])

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in word:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print(f"Did you mean {get_close_matches(word, data.keys())} [0]")
        decision = input ("y or n")
        if decision == "y" or "Y":
            return data[get_close_matches(word, data.keys()) [0]]
        elif decision == "n" or "N":
            return ("Oh! Next time.")
        else:
            return ("Wrong input!")
    else:
        print("Word out of the scope of this dictionary")

word = input ("Enter a word to search: ")
meaning = search(word)
# print(meaning)
if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)