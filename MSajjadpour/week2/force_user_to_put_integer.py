while True:
    user_input = input("Enter an integer: ")
    if user_input.lstrip('-').isdigit():
        number = int(user_input)
        break
    else:
        print(" Invalid input. Please enter a valid integer.")
print('='*40)


