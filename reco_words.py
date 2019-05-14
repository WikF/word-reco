# 1. User is putting word
# 2. Giving definition
# 3. If there was mistake it's asking if this is the word or it's different
# 4. a. if pointed word then give definition
# 4. b. if not that word then do you want to continue?
# 5. then apply the rule

import json
from difflib import get_close_matches
data = json.load(open('data.json'))



def dictionary():
    w = input("Please provide me with the word: ")

    if w in data:
        print(data[w])


    elif len(get_close_matches(w, data))> 0:
        print("Did you mean :", get_close_matches(w, data)[0])
        y =input("For yes click 'y', for no click 'n' ")
        if y.lower() == 'y':
            print(data[get_close_matches(w, data)[0]])
        else:
            print("Do you want to try next one?")
            next = input("For yes click 'y', for no click 'n' ")
            if next.lower() == 'y':

                dictionary()
            else:
                print("Bye!")
    elif w not in data:
        print("This word does not exist, do you want to try next one?")
        next = input("For yes click 'y', for no click 'n' ")
        if next.lower() == 'y':
            dictionary()
        else:
            print("Bye!")




dictionary()



