my_string = input("Give me a phrase I can reverse: ")
rev_str = ""


for letter in range(len(my_string) -1, -1, -1): # len if my_str -1 gives me teh start of the range (starting at the end, the stop is -1 so I include index 0 and ti step -1 (reverse))
    rev_str += my_string[letter] # I did not know that I could += to a string, first I initiatized and empty string and then incremnetally add to it
    

# rev_str = my_string[::-1] # this is an eaiser way to reverse a string using :: to indiate all characters in a string, no start and stop.  The -1 indicates reverse steps/stride
print("This is your string backwads: " + (rev_str))