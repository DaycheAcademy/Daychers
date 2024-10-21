# from random import randint
# from typing import List
#
# print('Hello this is the game of Rock , Paper and Scissors. \n you just '
#       'have to enter your choice (rock, paper, or scissors) and \n the computer will make its choice.')
#
# print('-' * 40)
#
# # check input of int to be correct
# while True:
#     try:
#         winning_score = int(input('Enter the winning score: '))
#         break
#     except ValueError:
#         print('Invalid input. Please enter a valid integer.')
#         continue
#
# print(f'whoever reach to {winning_score} wins, wins the game.')
#
# print('-' * 40)
#
# choices = ['scissors', 'rock', 'paper']
# #================================================================
#
# def get_human_choice():
#     choices = ['scissors', 'rock', 'paper']  # Valid choices
#
#     while True:
#         human_choice = input('Enter your choice (rock, paper, or scissors) or quit: ').lower()
#
#         # Quit the game if the user inputs 'quit' or 'q'
#         if human_choice == 'quit' or human_choice == 'q':
#             #print('Game over.')
#             return None  # Exit the function, indicating game over
#
#         # Check if the input is a valid choice
#         if human_choice in choices:
#             print('Your choice:', human_choice)
#             return human_choice
#
#         # Check for short forms 'r', 's', 'p'
#         if human_choice == 'r' or human_choice == 's' or human_choice == 'p':
#             if human_choice == 'r':
#                 human_choice = 'rock'
#             elif human_choice == 's':
#                 human_choice = 'scissors'
#             else:
#                 human_choice = 'paper'
#             print('Your choice:', human_choice)
#             return human_choice
#
#         else:
#             # Split the input into words in case there are multiple words
#             words = human_choice.split()
#
#             # Flag to track if a valid choice was found
#             found_valid_choice = False
#
#             # Loop through each word and check if it's a valid choice or short form
#             for word in words:
#                 if word in choices:
#                     print('Your choice:', word)
#                     found_valid_choice = True
#                     return word  # Return the valid choice
#
#                 if word == 'r' or word == 's' or word == 'p':
#                     found_valid_choice = True
#                     if word == 'r':
#                         human_choice = 'rock'
#                     elif word == 's':
#                         human_choice = 'scissors'
#                     else:
#                         human_choice = 'paper'
#                     print('Your choice:', human_choice)
#                     return human_choice
#
#             # If no valid word is found in the input, prompt again
#             if not found_valid_choice:
#                 print('Invalid input. Please enter a valid choice (rock, paper, or scissors).')
#                 print('-' * 40)
#
#
# print('-' * 40)
#
#
# human = 0
# computer = 0
# # check the winner
# while True:
#     print('-'* 40)
#     if human == winning_score:
#         print('You won the game!')
#         play_again = input('Do you want to play again? (yes/no): ').lower()
#         if play_again!= 'yes' or play_again.startswith('n'):
#             print('Game ended.')
#             break
#         else:
#             human = 0
#             computer = 0
#             continue
#
#     if computer == winning_score:
#         print('Computer won the game!')
#         play_again = input('Do you want to play again? (yes/no): ').lower()
#         if play_again != 'yes':
#             print('Game ended.')
#             break
#         else:
#             human = 0
#             computer = 0
#             continue
#
#     computer_choice = choices[randint(0, 2)]
#     human_choice = get_human_choice()
#     if human_choice is None:
#         print('Game ended.')
#         break
#
#     print(f'Computer chose: {computer_choice}')
#
#     if human_choice == computer_choice:
#         print('It is a tie!')
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#     if (human_choice == 'rock' and computer_choice =='scissors'):
#         human += 1
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#     if (human_choice == 'rock' and computer_choice == 'paper'):
#         computer += 1
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#     if (human_choice == 'paper' and computer_choice == 'rock'):
#         human += 1
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#     if (human_choice == 'paper' and computer_choice =='scissors'):
#         computer += 1
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#     if (human_choice =='scissors' and computer_choice == 'rock'):
#         computer += 1
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#     if (human_choice =='scissors' and computer_choice == 'paper'):
#         human += 1
#         print(f'computer score : {computer}')
#         print(f'human score: {human}')
#         continue
#
#
#
from random import randint



# Get the winning score
# while True:
#     try:
#         winning_score = int(input('Enter the winning score: '))
#         break
#     except ValueError:
#         print('Invalid input. Please enter a valid integer.')

# print(f'Whoever reaches {winning_score} wins the game.')
# print('-' * 40)

from random import randint

print('Hello, this is the game of Rock, Paper, and Scissors.\nYou just '
      'have to enter your choice (rock, paper, or scissors) and \n the computer will make its choice.')

print('-' * 40)

choices = ['scissors', 'rock', 'paper']
human_score = 0
computer_score = 0
play_again = True

# Game logic including human choice input and comparison
while True:
    flag = False

    if play_again:
        # Get the user input first as a string
        try:
            user_input = input('Enter the winning score (or type "q" or "quit" to exit): ')
        except EOFError:
            print('\nGame ended by user (EOF).')
            break

        # Check if the user wants to quit
        if user_input.lower() in ['q', 'quit']:
            print('Game ended.')
            break

        # Try to convert the input to an integer
        try:
            winning_score = int(user_input)
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue  # Go back and ask for the winning score again

    play_again = False

    # Check if human or computer reached the winning score
    if human_score == winning_score:
        print('You won the game!')
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Game ended.')
            break
        else:
            human_score = 0
            computer_score = 0
            play_again = True
            continue

    if computer_score == winning_score:
        print('Computer won the game!')
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Game ended.')
            break
        else:
            human_score = 0
            computer_score = 0
            play_again = True
            continue

    # Get human choice
    try:
        human_choice = input('Enter your choice (rock, paper, or scissors) or quit: ').lower()
    except EOFError:
        print('\nGame ended by user (EOF).')
        break

    if len(human_choice.split(' ')) > 1:
        # Check if any word in the split human_choice is in choices
        for word in human_choice.split(' '):
            if word in choices:
                human_choice = word
                flag = True

    else:
        if human_choice in ['quit', 'q']:
            print('Game ended.')
            break

        if human_choice in ['r', 'rock']:
            human_choice = 'rock'
        elif human_choice in ['p', 'paper']:
            human_choice = 'paper'
        elif human_choice in ['s', 'scissors']:
            human_choice = 'scissors'
        else:
            print('Invalid input. Please enter a valid choice (rock, paper, or scissors).')
            continue

    if not flag and len(human_choice.split(' ')) > 1:
        print('Invalid input. Please enter a valid choice.')
        continue

    # Computer choice
    computer_choice = choices[randint(0, 2)]
    print(f'Computer chose: {computer_choice}')

    # Compare choices and update scores
    if human_choice == computer_choice:
        print('It\'s a tie!')
    elif (human_choice == 'rock' and computer_choice == 'scissors') or \
            (human_choice == 'scissors' and computer_choice == 'paper') or \
            (human_choice == 'paper' and computer_choice == 'rock'):
        human_score += 1
        print(f'You won this round! Human: {human_score}, Computer: {computer_score}')
    else:
        computer_score += 1
        print(f'Computer won this round! Human: {human_score}, Computer: {computer_score}')