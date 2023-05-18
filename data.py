import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        yesno = input("Do you mean %s instead? If Yes press y else press n: " % get_close_matches(word, data.keys())[0])
        if yesno == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno == "n":
            return ("The word doesn't exist")
        else:
            return ("Invalid entry")
                
    else:
        return ("The word doesnt exist")

word = input("Enter word: ")
output = dictionary(word)

if type(output) == list:
    for item in output:
        print (item)
else:
    print(output)