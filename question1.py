
# Question 1: FizzBuzz Program

# This program prints numbers from 1 to 50. 
# For multiples of 3, it prints "Fizz" instead of the number.
# For multiples of 5, it prints "Buzz" instead of the number.
# For multiples of both 3 and 5, it prints "FizzBuzz".

for number in range(1, 51):  # Loop through numbers from 1 to 50
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # Multiples of both 3 and 5
    elif number % 3 == 0:
        print("Fizz")  # Multiples of 3 only
    elif number % 5 == 0:
        print("Buzz")  # Multiples of 5 only
    else:
        print(number)  # Numbers not multiples of 3 or 5
