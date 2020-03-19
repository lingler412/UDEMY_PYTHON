my_num1 = int(input("Give me a number so I can give you it's factorial! ")) # give me a whole integer


def calc_factorial(my_num): # here is a function to caluate the factorial of the provided integer
    for num in range(my_num - 1, 1, -1):
        my_num *= num
    return my_num


my_factorial = calc_factorial(my_num1) # calling my function with user input as my argument

print("The factorial of " + str(my_num1) + " is " + str(my_factorial)) # printing my original user input along with my calulated factorial