import json                                        
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()                           
    if w in data:
        return data[w]
    elif w.title() in data:                     # w.title()  会将w中的单词的首字母大写， 因此可以查找Paris 这类单词。
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]                  # w.upper()  会将w中的单词所有字母都大写，因此可以查找USA 这类单词。
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) 
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."   
        else:
            return "We didn't understand your entry."
    else:                                                                                
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)