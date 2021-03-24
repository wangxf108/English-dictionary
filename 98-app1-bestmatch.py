import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()                           
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" %get_close_matches(w, data.keys())[0]    #此处【0】选择相似键值得第一个作为推荐
    else:                                                                          # %s 是将s用 后方 % 之后的内容代替
        return "The word doesn't exist. Please double check it."

word = input("Enter word:")

print(translate(word))