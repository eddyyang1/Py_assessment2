# Question 10: Convert List of Tuples to Dictionary

# This function takes a list of tuples where each tuple contains a string and an integer,
# and returns a dictionary with strings as keys and integers as values.

def tuples_to_dictionary(tuples_list):
    # Initialize an empty dictionary to store the results
    result_dict = {}
    # Loop through each tuple in the list
    for key, value in tuples_list:
        # Add the string as the key and integer as the value in the dictionary
        result_dict[key] = value
    return result_dict

# Example list of tuples
# tuples_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
# print(tuples_to_dictionary(tuples_list))  # Expected output: {'apple': 5, 'banana': 3, 'cherry': 7}
