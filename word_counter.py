user_str = input("Give me something to work with: ")
indiv_words = user_str.strip("!.*").replace("!", "").replace("*", "").split() # sucks you can only replce one character at a time rather than a list
num_of_words = len(indiv_words)
print("Your " + str(num_of_words) + " words are " + str(indiv_words))