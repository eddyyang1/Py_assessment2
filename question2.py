
# Question 2: Continuous Input Until 'exit'

# This program repeatedly asks the user for input until they type "exit".
# It prints each input before asking for the next one.

def get_user_input():
    while True:  # Infinite loop to keep asking for input
        user_input = input("Enter a word (type 'exit' to quit): ")  # Get user input
        if user_input.lower() == "exit":  # Check if input is "exit"
            break  # Exit the loop if "exit" is entered
        print(user_input)  # Print the user's input

# Call the function to execute the input loop
get_user_input()
