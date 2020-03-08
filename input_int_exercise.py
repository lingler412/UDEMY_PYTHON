user_int = int(input("Please enter a whole number:  ")) # taking input and changing from string to int
user_int += 10 #ading 10 to the user input, still an int
print("I have added 10 to your number making it " + str(user_int)) # temp changing to a srting to concatenate and print
print(type(user_int)) # showing that it is still an int
print(user_int + 10)