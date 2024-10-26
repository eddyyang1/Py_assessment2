
# Question 5: Print Keys with Even Values

# This function accepts a dictionary and prints keys whose values are even.

def print_keys_with_even_values(my_dict):
    # Loop through each key-value pair in the dictionary
    for key, value in my_dict.items():
        # Check if the value is even
        if value % 2 == 0:
            print(key)

# Example dictionary
# my_dict = {'a': 2, 'b': 3, 'c': 4}
# print_keys_with_even_values(my_dict)  # Expected output: a, c
