
# Question 6: Largest Number in a Tuple

# This function accepts a tuple of numbers and returns the largest number.

def find_largest_number(numbers):
    # Initialize the largest variable with the first element of the tuple
    largest = numbers[0]
    # Iterate through each number in the tuple
    for number in numbers:
        # Update largest if a larger number is found
        if number > largest:
            largest = number
    return largest

# Example tuple
numbers = (10, 20, 30, 40, 50)
print(find_largest_number(numbers))  
