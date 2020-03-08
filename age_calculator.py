my_age = int(input("how old are you? "))


def calc_age_in_seconds(my_age):
    return my_age * 31536000


my_age_in_seconds = calc_age_in_seconds(my_age)

formatted_age = "{:,}".format(my_age_in_seconds)

print("You are " + formatted_age + " seconds old!")
print(type(formatted_age))
print(type(my_age_in_seconds))