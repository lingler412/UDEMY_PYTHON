range_of_nums = range(1,51) # generate a set of numbers between 1 and 50


for num in range_of_nums:
    if num % 3 == 0 and num % 5 == 0: # is the num divisiable by 3 & 5?
        print("FizzBuzz")
    elif num % 3 == 0 and num % 5 != 0: # is the num ONLY divisible by 3?
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0: # is the num ONLY divisible by 5?
        print("Buzz")
    else:
        print(num) # if none of the above, just print the num
    
    
    
    
    
        
