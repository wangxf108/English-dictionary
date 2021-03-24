import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()                            #将大写字母变成小写字母
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word:")

print(translate(word))