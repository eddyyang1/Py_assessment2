
# Question 3: Sum of All Numbers in a List

# This function calculates the sum of all numbers in a given list.

def sum_of_list(nums):
    # Initialize a variable to keep track of the sum
    total = 0
    # Iterate over each number in the list and add it to the total
    for num in nums:
        total += num
    return total

# Example list
# nums = [1, 2, 3, 4, 5]
# print(sum_of_list(nums))  # Expected output: 15
