celsius_input = int(input("Please enter a celsius value to convert to fahrenheit: ")) # variable for celsius input
 

def calculate_fahrenheit_temp(celsius_input): # defining a function to convert celsius user input into fahrenheit degrees
    return (celsius_input * 18 + 320) / 10


fahrenheit_temp = round(calculate_fahrenheit_temp(celsius_input), 1) # using the round function to ensure no more than 1 place after decimal is retruned

# print(fahrenheit_temp)
# print(type(fahrenheit_temp))


print("The fahrenheit equivalent of " + str(celsius_input) + " degrees celsius is " + str(fahrenheit_temp) + " degrees fahrenheit!")
# converted both varaibles to string before printing concatenated strings