from random import randint # import randint function

random_num = randint(1,20) # generate a number between 1 and 20

user_int = int(input("Pick a number between 1 and 20: ")) # take input

if user_int > random_num:
    print("You're a little high, my number was " + str(random_num))
elif user_int < random_num:
    print("You're a little low, my number was " + str(random_num))
else:
    print("You're a mind reader!")
