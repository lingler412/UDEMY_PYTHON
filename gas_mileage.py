from random import randint


gal_per_tank = randint(10,25)
miles_per_tank = randint(200,400)


def calc_mpg(miles, gallons):
    return miles // gallons


mpg = calc_mpg(miles_per_tank, gal_per_tank)
print(mpg)