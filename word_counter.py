user_str = input("Give me something to work with: ")
# commenting out because a for loop is cleaner and accounts for all specoial characters:  indiv_words = user_str.strip("!.*").replace("!", "").replace("*", "").split() # sucks you can only replce one character at a time rather than a list

no_special = ""

for char in user_str:
    if char.isalpha() or char.isspace() or char.isalnum():
        no_special += char
        

num_of_words = len(no_special.split())

print("Your " + str(num_of_words) + " words are " + str(no_special.split()))