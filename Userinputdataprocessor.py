def validate_name_length():
    # Task: Prompt the user for their first name and remove any leading or trailing spaces
    first_name = input("Please enter your first name: ").strip()
    
    # Task: Prompt the user for their last name and remove any leading or trailing spaces
    last_name = input("Please enter your last name: ").strip()
    
    # Task: Check if the length of the first name is less than 2 characters
    if len(first_name) < 2:
        # Task: Print an error message if the first name is too short
        print("Error: The first name must be at least 2 characters long.")
    
    # Task: Check if the length of the last name is less than 2 characters
    if len(last_name) < 2:
        # Task: Print an error message if the last name is too short
        print("Error: The last name must be at least 2 characters long.")
    
    # Task: If both names are valid (at least 2 characters long), confirm successful input
    if len(first_name) >= 2 and len(last_name) >= 2:
        print("The input data is valid.")

# Task: Call the function to execute the input validation process
validate_name_length()