# User Validation

while True:
    # Take first name input from the user
    first_name = input("Enter Your First Name: ")

    # Define valid characters for letters and spaces
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


    # Initialize validation without using a separate boolean variable
    for char in first_name:
        # Check if character is a number
        if len(first_name) < 3 or len(first_name) > 10:
            print("Error: First name not valid.")
            break
        elif char>='0' and char<='9':
            print("Error: First name contains numbers.")
            break
        elif char == " ":
            print("Error: First name contains spaces.")
            break
        # Check if character is a special character
        elif char not in valid_chars:
            print("Error: First name contains special characters.")
            break
    else:
        # This else block is executed if no break occurred in the for loop,
        # meaning the first name is valid
        print("First Name:", first_name)
        break

while True:
    phone_number = input("Enter Phone Number :")

    valid_number = "0,1,2,3,4,5,6,7,8,9"

    for num in phone_number:
        if num not in valid_number:
            print("Error: phone number contains other value")
            break

        elif len(phone_number)<10 or len(phone_number)>10:
            print("Error: Phone number contains invalid digit")
            break

        elif num == " ":
            print("Error: Phone number contains space")
            break

    else:
        print("Phone Number: ", phone_number)
        break
