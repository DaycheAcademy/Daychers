from random import choice

computer_choices = ["ROCK", "PAPER", "SCISSORS"]
user_possible_choices = {"ROCK": "ROCK", "R": "ROCK", "1": "ROCK",
                         "PAPER": "PAPER", "P": "PAPER", "2": "PAPER",
                         "SCISSORS": "SCISSORS", "S": "SCISSORS", "3": "SCISSORS"}


print("Here are the rules of the game:\n\tRock beats Scissors -- Scissors cut Paper -- Paper covers Rock")
print("*" * 100)


while True:
    winning_score = 0
    computer_score = 0
    user_score = 0

    user_input = input("if you want to exit, please type quit. "
                       "otherwise type a number for winning score. ")
    if 'Q' in user_input.upper():
        print("seems like you wanna go. hope to see you soon!")
        break

    elif user_input.isnumeric():
        winning_score = int(user_input)
        print(f"you need {winning_score} scores to win the game.")

        while computer_score < winning_score and user_score < winning_score:
            print("-" * 100)
            user_choice = input("tell me your choice: 1)ROCK 2)Paper 3)Scissors: (type 'quit' to stop the game) ")
            user_choice = user_choice.upper().strip()

            if "Q" in user_choice:
                print("seems like you want to stop the game.")
                break

            user_words = user_choice.split()
            for word in user_words:
                if word in user_possible_choices:
                    user_choice = user_possible_choices[word]
                    break
            else:
                print("your choice is invalid. please choose one of the valid options.")
                continue

            computer_choice = choice(computer_choices)
            if user_choice[0] == computer_choice[0]:
                print(f"It's tie!\nNo one gets a point.")
            elif user_choice[0] == "R":
                if computer_choice[0] == "P":
                    computer_score += 1
                    print("I won!")
                else:
                    user_score += 1
                    print("You won!")
            elif user_choice[0] == "P":
                if computer_choice[0] == "R":
                    user_score += 1
                    print("You won!")
                else:
                    computer_score += 1
                    print("I won!")
            elif user_choice[0] == "S":
                if computer_choice[0] == "R":
                    computer_score += 1
                    print("I won!")
                else:
                    user_score += 1
                    print("You won!")

            print(f"\nI chose [ {computer_choice} ], and you chose [ {user_choice} ].\n")
            print(f"so far the scores are...\n\tmy score: {computer_score},\t your score: {user_score}")

        print("*"*100)
        print("*"*100)

        if computer_score == winning_score:
            print("seems like i won the game!")
        else:
            print("you won the game!")
        print(f"my score is {computer_score}, and your score is {user_score}")
    else:
        print("your input was invalid. please type a valid option.")
