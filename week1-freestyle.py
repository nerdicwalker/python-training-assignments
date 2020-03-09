#!/usr/local/bin/python3

user_input_number = input("Enter a number from 1 - 999: ")

try:
    # test if user input is a valid number
    test_user_input = int(user_input_number)
    if int(user_input_number) < 1:
        print("Incorrect input.")
    elif int(user_input_number) > 999:
        print("Incorrect input.")
    else:
        print(user_input_number)
except ValueError:
    try:
        test_user_input = float(user_input_number)
        print("Incorrect input.")
    except ValueError:
        print("Incorrect input.")
