my_str = "Hello World"

split_str = my_str.split()

print(split_str)

print(type(split_str))

test_list = [1, 1.3, "test"]

print(test_list[1])

print(type(test_list[0]))

print(type(test_list[1]))

print(type(test_list[2]))

my_list = [1,2,3,4,5]

print(my_list[1])

lists_on_lists = [[1, 2, 3], ["a", "b", "c"]]

print(lists_on_lists[1][2])

del lists_on_lists [1]

print(lists_on_lists)

ordinary_lists = [1, 2, 3, 4, 5]

print(ordinary_lists[-1]) # negative indexes to start from the right

ordinary_lists.append(4)

print(ordinary_lists)

ordinary_lists.remove(4) # removes the first occurance of 4 in the list

print(ordinary_lists)

print(ordinary_lists[2: ])

print(ordinary_lists[ :2])

ordinary_lists[0] = 10

print(ordinary_lists)

give_me_the_last_one = ordinary_lists.pop(1) # can pop anitem off the list and assign it to a variable

print(give_me_the_last_one)