from random import randint # importing only what function I need (fucntion import)


gal_per_tank = randint(10,25) # Randomly generting the gallons per tank
miles_per_tank = randint(200,400) # Randomly generatig the miles dirven per full tank


def calc_mpg(miles, gallons): # chose to define a function...might be overkill :-)
    return miles // gallons


mpg = calc_mpg(miles_per_tank, gal_per_tank) # Passing my arguments
print(mpg) 