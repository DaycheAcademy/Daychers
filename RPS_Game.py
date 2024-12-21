from random import randint

# Creat a list of game choice
gameChoice = ["ROCK", "PAPER", "SCISSORS"]

validChoice = {"rock":     "r",
               "paper":    "p",
               "scissors": "s",
               "quit":     "q"}

welcomeMessage = ("Welcome to My Game!",
                  "Here You have a Chance to Play the Game of Rock-Paper-Scissors with Me.",
                  "Rules are Simple:",
                  "        Rock Smashes Scissors",
                  "        Scissors Cut Paper",
                  "        Paper Covers Rock",
                  "Hope You Enjoy it!")

userWinMessage = ("Oooh! Nice job mate, you nailed it!",
                  "What a lot of lock, wish you would not do that!",
                  "My heavens! How could you be so in luck!",
                  "Oh nooo! I can not believe this, you outsmarted me!")

compWinMessage = ("Hahaaa! In your face!",
                  "Woohoo! I'm rolling in, come on, one more!",
                  "Yayyy! I'm unstoppable, gonna win this really easy!",
                  "Clap, clap! Happiness, I'm the best!")

sameChoiceMessage = "It's a Tie! Seems our choices are the same."

userValidChoices = list(validChoice.keys()) + list(validChoice.values())
# print(userValidChoices)

print('\n')
print('*' * 75)
for message in welcomeMessage:
    print(message)
print('*' * 75)

while True:
    userWinCount, compWinCount, winningScore = 0, 0, 0
    exitGame = False

    integer = input("\nPlease type in a value for the winning score:")

    if not integer.isdigit() or int(integer) == 0:
        print("\nI need an integer bigger then \'Zero\' to carry on. Please type in an 'integer' value.")
        continue

    winningScore = int(integer)

    while max(userWinCount, compWinCount) < winningScore:

        userChoice = input("\nPlease select either Rock, Paper or Scissors (or QUIT to exit):")
        userChoiceWord = userChoice.lower().split()
        # print(userChoiceWord)
        matchingUserChoice = [word for word in userChoiceWord if word in userValidChoices]

        if matchingUserChoice:
            compChoice = gameChoice[randint(0, 2)]

            if matchingUserChoice[0] == 'q' or matchingUserChoice[0] == 'quit':
                print('\n')
                print('*' * 55)
                print('Thank you for playing this game. I really enjoy it!')
                print('*' * 55)
                exitGame = True
                break

            elif ((matchingUserChoice[0] in ["rock", "r"] and compChoice == "ROCK") or
                  (matchingUserChoice[0] in ["scissors", "s"] and compChoice == "SCISSORS") or
                  (matchingUserChoice[0] in ["paper", "p"] and compChoice == "PAPER")):
                print('\n')
                print('*' * 55)
                print(sameChoiceMessage)
                print('I had: {} and your choice was: {}'.format(compChoice, matchingUserChoice[0].upper()))
                print("So no point for any of us this time!")
                print('*' * 55)
                print(f'\nComputer Score is: {compWinCount}')
                print(f'User Score is: {userWinCount}')

            elif ((matchingUserChoice[0] in ["rock", "r"] and compChoice == "SCISSORS") or
                  (matchingUserChoice[0] in ["scissors", "s"] and compChoice == "PAPER") or
                  (matchingUserChoice[0] in ["paper", "p"] and compChoice == "ROCK")):
                userWinCount += 1
                print('\n')
                print('*' * 55)
                print(userWinMessage[randint(0,3)])
                print('I had: {} and your choice was: {}'.format(compChoice, matchingUserChoice[0].upper()))
                print('*' * 55)
                print(f'\nComputer Score is: {compWinCount}')
                print(f'User Score is: {userWinCount}')

            elif ((matchingUserChoice[0] in ["rock", "r"] and compChoice == "PAPER") or
                  (matchingUserChoice[0] in ["scissors", "s"] and compChoice == "ROCK") or
                  (matchingUserChoice[0] in ["paper", "p"] and compChoice == "SCISSORS")):
                compWinCount += 1
                print('\n')
                print('*' * 55)
                print(compWinMessage[randint(0,3)])
                print('I had: {} and your choice was: {}'.format(compChoice, matchingUserChoice[0].upper()))
                print('*' * 55)
                print(f'\nComputer Score is: {compWinCount}')
                print(f'User Score is: {userWinCount}')

        else:
            print('\n')
            print(f'\'{userChoice}\' is not a valid choice. Please try again.')
            continue

    if exitGame:
        break

    elif userWinCount == winningScore:
        print('\n')
        print('*' * 55)
        print('CONGRATS! YOU HAVE WON THE GAME!')
        print('*' * 55)

    elif compWinCount == winningScore:
        print('\n')
        print('*' * 55)
        print('WOOOHOOO! I HAVE WON THE GAME!')
        print('*' * 55)

    playAgain = input("\nCare to play another round? [yes/no]:")

    while playAgain.lower() not in ['yes', 'no']:
        print('You Need to Tell Me Exactly What to Do. I Need a \'YES\' or \'NO\'.')
        playAgain = input("\nCare to play another round? [yes/no]:")

    if playAgain.lower() == 'no':
        print('\n')
        print('*' * 55)
        print('Thank you for playing this game. I really enjoy it!')
        print('*' * 55)
        break

    else:
        print('Alright, Let\'s do one more!')
