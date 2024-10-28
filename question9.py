# Question 9: Two Distinct Numbers Adding up to Target Sum

# This function checks if there are two distinct numbers in the list that add up to a given target sum.

def has_pair_with_sum(numbers, target_sum):
    # Initialize an empty set to store numbers we've seen
    seen_numbers = set()
    # Loop through each number in the list
    for number in numbers:
        # Calculate the complement that would add up to the target sum
        complement = target_sum - number
        # Check if the complement is in the seen numbers
        if complement in seen_numbers:
            return True  # Pair found
        # Add the current number to the set
        seen_numbers.add(number)
    return False  # No pairs found

# Example list and target sum
numbers = [1, 2, 3, 9]
target_sum = 5
print(has_pair_with_sum(numbers, target_sum))  
