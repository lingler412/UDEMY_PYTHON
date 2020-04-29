user_str = input("Give me something to work with: ")
# commenting out because a for loop is cleaner and accounts for all specoial characters:  indiv_words = user_str.strip("!.*").replace("!", "").replace("*", "").split() # sucks you can only replce one character at a time rather than a list

no_special = ""

for char in user_str:
    if char.isalnum() or char.isspace():
        no_special += char
        

num_of_words = len(no_special.split())

print("Your {} words are {}".format(str(num_of_words), str(no_special.split()))) # used format method raher than concatenation 