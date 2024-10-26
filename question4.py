
# Question 4: Reversed Strings in List

# This function accepts a list of strings and returns a new list with each string reversed.

def reverse_each_string(strings):
    # Initialize an empty list to store the reversed strings
    reversed_strings = []
    # Loop through each string in the list
    for string in strings:
        # Reverse the string using slicing and append to the result list
        reversed_strings.append(string[::-1])
    return reversed_strings

# Example list
# strings = ["apple", "banana", "cherry"]
# print(reverse_each_string(strings))  # Expected output: ['elppa', 'ananab', 'yrrehc']
