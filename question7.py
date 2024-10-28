
# Question 7: Remove Duplicates from List

# This function accepts a list and returns a new list with all duplicate elements removed.

def remove_duplicates(my_list):
    # Initialize an empty list to store unique elements
    unique_list = []
    # Iterate through each element in the list
    for item in my_list:
        # Only add elements not already in unique_list
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example list
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))  # Expected output: [1, 2, 3, 4, 5]
