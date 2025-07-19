total = 0
count = 0

while True:
    user_input = input("Enter an integer (or 'q' to quit to stop): ")
    if user_input.lower() == 'q' or user_input.lower() == 'quit':
        break
    if user_input.strip().lstrip('-').isdigit():
        total += int(user_input)
        count += 1
    else:
        print("Invalid input. Please enter an integer or 'q' to quit.")

if count > 0:
    mean = total / count
    print(f"Mean of entered numbers: {mean}")
else:
    print("No valid integers were entered.")



