pos_int = int(input("Give me a positive whole number: ")) # get the input for the loop

print("Thanks! I will now iteratatively add to " + str(pos_int)) # state the number I plan to iterate on

sum_of_my_num = pos_int # creating a variabl to hold my sum as i iterate, and set it to my initial input from pos_int

while pos_int >= 1: # loop to iteratively add up decrements of my original input
    pos_int -= 1 # decrement my orgiinal input by 1
    sum_of_my_num += pos_int # ietratively sum my int as it is decremeted each loop
       

print("Your sum is " + str(sum_of_my_num)) # print my sum
