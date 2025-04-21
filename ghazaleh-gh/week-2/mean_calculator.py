user_input = ""
numbers = list()


# while 'q' not in user_input:
#     user_input = input("please enter a number, or type quit to stop: ")
#     if user_input.isnumeric():
#         numbers.append(int(user_input))
#
#     else:
#         print("invalid input. enter a number or 'quit' to stop.")
#
#
# print(f"the numbers you've entered are: {numbers}")
# print(f"the average of numbers is: {sum(numbers) / len(numbers)}")
#


# ----with infinite loop
while True:
    user_input = input("please enter a number, or type quit to stop: ")
    if 'q' not in user_input:
        if user_input.isnumeric():
            numbers.append(int(user_input))

        else:
            print("invalid input. enter a number or 'quit' to stop.")
    else:
        break

if numbers:
    print(f"the numbers you've entered are: {numbers}")
    print(f"the average of numbers is: {sum(numbers) / len(numbers)}")
else:
    print("you didn't enter any numbers.")
