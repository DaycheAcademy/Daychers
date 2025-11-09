from random import randint

while True:
    winningScore = input('Please type in a value for the winning score: ')
    if winningScore.isdigit():
        winningScore = int(winningScore)
        break

rock = ['r', 'rock']
paper = ['p', 'paper']
scissors = ['s', 'scissor']
stopGame = ['q', 'quit']

computerScore = 0
userScore = 0

while userScore != winningScore and computerScore != winningScore:
    userInp = input('Please select either Rock, Paper or Scissors (or Quit to exit): ')
    userInpUpper = userInp.upper().split()
    userChoice = None

    for i in stopGame:
        if i.upper() in userInpUpper:
            print("Game ended by user.")
            quit()

    if not userChoice:
        for i in rock:
            if i.upper() in userInpUpper:
                userChoice = "Rock"
                break

    if not userChoice:
        for i in paper:
            if i.upper() in userInpUpper:
                userChoice = "Paper"
                break

    if not userChoice:
        for i in scissors:
            if i.upper() in userInpUpper:
                userChoice = "Scissors"
                break

    computerChoices = ['Rock', 'Paper', 'Scissors']
    computerChoice = computerChoices[randint(0, 2)]

    if computerChoice == userChoice:
        print('It’s a tie!')

    elif computerChoice == 'Rock' and userChoice == 'Paper':
        userScore += 1

    elif computerChoice == 'Rock' and userChoice == 'Scissors':
        computerScore += 1

    elif computerChoice == 'Paper' and userChoice == 'Rock':
        computerScore += 1

    elif computerChoice == 'Paper' and userChoice == 'Scissors':
        userScore += 1

    elif computerChoice == 'Scissors' and userChoice == 'Rock':
        userScore += 1

    elif computerChoice == 'Scissors' and userChoice == 'Paper':
        computerScore += 1

    print('-------------------------------------')
    print(f'Computer Choice: {computerChoice}')
    print(f'Your Choice: {userChoice}')
    print('-------------------------------------')
    print(f'Computer Score: {computerScore}')
    print(f'User Score: {userScore}')
    print('-------------------------------------')

print('-------------------------------------')

if userScore == winningScore:
    print('You won!')
elif computerScore == winningScore:
    print('You lost!')
