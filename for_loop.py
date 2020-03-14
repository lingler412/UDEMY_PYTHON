
my_string = input("Please provide me a statement so I can count the number of letters: ") # give me a string please

no_spaces = my_string.replace(" ", "") # using the replace fucn tion to remove all spaces

count = 0 # my count of characters


for char in no_spaces: # Looping through to count characters
    count += 1
    # print(char) # leanring that char is a variable declared in my loop
    

# print(char) # showing that char is still a global variable, so local scop is just within functions

print("Your string is " + str(count) + " characters long!")

# print(no_spaces) # Using to verfy removal of spaces