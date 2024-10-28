
# Question 8: Dictionary Keys with Values Greater than n

# This function accepts a dictionary and an integer n, returning a list of keys with values > n.

def keys_with_values_greater_than_n(my_dict, n):
    # Initialize an empty list to store qualifying keys
    result_keys = []
    # Iterate over dictionary items
    for key, value in my_dict.items():
        # Add key to result list if value is greater than n
        if value > n:
            result_keys.append(key)
    return result_keys

# Example dictionary and integer
my_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_with_values_greater_than_n(my_dict, n))  
