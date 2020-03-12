from random import randint

my_int = randint(1,10)

if my_int == 10:
    print("The roman numeral for " + str(my_int) + " is X")
elif my_int == 9:
    print("The roman numeral for " + str(my_int) + " is IX")
elif my_int == 8:
    print("The roman numeral for " + str(my_int) + " is VIII")
elif my_int == 7:
    print("The roman numeral for " + str(my_int) + " is VII")
elif my_int == 6:
    print("The roman numeral for " + str(my_int) + " is VI")
elif my_int == 5:
    print("The roman numeral for " + str(my_int) + " is V")
elif my_int == 4:
    print("The roman numeral for " + str(my_int) + " is IV")
elif my_int == 3:
    print("The roman numeral for " + str(my_int) + " is III")
elif my_int == 2:
    print("The roman numeral for " + str(my_int) + " is II")
elif my_int == 1:
    print("The roman numeral for " + str(my_int) + " is I")
else:
    print("I have no clue")