my_num1 = int(input("Give me a number so I can give you it's factorial! ")) # give me a whole integer


def calc_factorial(my_num): # here is a function to caluate the factorial of thr provided integer
    aggregate_num = my_num # definitng a local variable to hold my aggregate number, gets initial value of user input
      
      
    while my_num > 1: # while loop, must be greater than 1 to ensure my noting gets multiplied by zero
        aggregate_num *= my_num - 1 # reassigning with multiple of my_num -1 (iterating mutioes 1 lower the each before)
        my_num -= 1 # decrement my_num for the While loop
        
        
    return aggregate_num # returning teh end result wich is the factorial


my_factorial = calc_factorial(my_num1) # calling my function with user input as my argument

print("The factorial of " + str(my_num1) + " is " + str(my_factorial)) # printing my original user input along with my calulated factorial