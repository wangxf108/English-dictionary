import json                                              #使程序更加友好，更加智能，提示选项，错误选项，重新输入等
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()                           
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) 
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."   
        else:                                                             #如果输入了非N/Y的其他信息
            return "We didn't understand your entry."
    else:                                                                                
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))