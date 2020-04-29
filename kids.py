x = True

while x == True:
    name = input("What is your name? ")
    if name.lower().startswith("stop"):
        x = False
    elif name.lower().startswith("shelby"):
        print("You're my little princess!!")
    elif name.lower().startswith("aaron"):
        print("You're my little bubbyman!!")
    else:
        print("You're a little jerk!")