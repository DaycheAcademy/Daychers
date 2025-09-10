import random

print("Welcome to Rock-Paper-Scissors!")
print("Choices: rock (r), paper (p), scissors (s)")
print("Type 'exit' anytime to quit the game.")

# Ask user for number of rounds
while True:
    try:
        total_rounds = int(input("How many rounds do you want to play? "))
        if total_rounds > 0:
            break
        else:
            print(" Please enter a positive number.")
    except ValueError:
        print(" Invalid input! Please enter a number.")

choices = ["rock", "paper", "scissors"]
shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}

# Scores
user_score = 0
computer_score = 0
round_num = 0

# Play for the fixed number of rounds
while round_num < total_rounds:
    round_num += 1
    print(f"\n Round {round_num} of {total_rounds}")

    # Get user choice
    while True:
        user_input = input("Enter your choice: ").lower().split()  # split input into words

        # Check if user wants to exit
        if "exit" in user_input:
            print("\n You exited the game!")
            print(f" Final Score → You: {user_score} | Computer: {computer_score}")
            exit()

        # Detect choice
        user_choice = None
        for word in user_input:
            if word in choices:  # exact match (rock, paper, scissors)
                user_choice = word
                break
            elif word in shortcuts:  # shortcut (r, p, s)
                user_choice = shortcuts[word]
                break

        if user_choice:
            break
        else:
            print(" Invalid choice! Please include rock, paper, or scissors (or r/p/s), or type 'exit' to quit.")

    # Computer choice
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    # Decide round winner
    if user_choice == computer_choice:
        print(" It's a tie! No points awarded.")
    elif (user_choice == "rock" and computer_choice == "scissors") \
            or (user_choice == "paper" and computer_choice == "rock") \
            or (user_choice == "scissors" and computer_choice == "paper"):
        print(" You win this round!")
        user_score += 1
    else:
        print(" Computer wins this round!")
        computer_score += 1

    # Show current score
    print(f" Score → You: {user_score} | Computer: {computer_score}")

# Final result
print("\n Game Over!")
print(f"Final Score → You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print(" Congratulations! You won the game!")
elif computer_score > user_score:
    print(" Computer won the game!")
else:
    print(" It's a tie overall!")
