import random
first_time = True

while True:
    if first_time:
        dor = int(input('''slm in ye bazie sang kaghaz gheychie!
         ghavanin be in soorat hastan:
         sang gheychi ro mishkane,
         gheychi kaghazo mibore,
         kaghaz sango migire
         hala baraye shoro aval bgo bazi be chand :'''))
        first_time = False
    else:
        dor = int(input('bazi be chand?'))


    emtiaze_man=0
    emtiaze_to=0


    def print_score():
        print(f'emtiaze man: {emtiaze_man}, emtiaze to: {emtiaze_to}')

    def print_com_choice():
        print(f'entekhabe man: {entekhabe_man}')
    while emtiaze_man+emtiaze_to<dor:


        entekhabe_to=(input('hala sang ya kaghaz ya gheychi ro entekhab kon:').lower().split())
        gheychi=['gheychi','g']
        sang=['sang','s']
        kaghaz=['kaghaz','k']
        if any(i in entekhabe_to for i in gheychi) :
            entekhabe_to= 'gheychi'

        elif any(i in entekhabe_to for i in sang) :
            entekhabe_to= 'sang'
        elif any(i in entekhabe_to for i in kaghaz) :
            entekhabe_to= 'kaghaz'
        else:
            print('entekhab eshtebah')
            continue

        s_k_g = ["sang", "kaghaz", "gheychi"]
        entekhabe_man = random.choice(s_k_g)

        if entekhabe_to == entekhabe_man:
            print_com_choice()
            print("mosavi")
            print_score()

        elif entekhabe_to == "sang":
            if entekhabe_man == "kaghaz":
                print_com_choice()
                print("in dor man bordam!")
                emtiaze_man+=1
                print_score()

            else:
                print_com_choice()
                print("in dor to bordi!")
                emtiaze_to+=1
                print_score()

        elif entekhabe_to == "kaghaz":
            if entekhabe_man == "gheychi":
                print_com_choice()
                print("in dor man bordam!")
                emtiaze_man+=1
                print_score()

            else:
                print_com_choice()
                print("in dor to bordi!")
                emtiaze_to+=1
                print_score()


        elif entekhabe_to == "gheychi":
            if entekhabe_man == "sang":
                print_com_choice()
                print("in dor man bordam")
                emtiaze_man+=1
                print_score()

            else:
                print_com_choice()
                print("in dor to bordi")
                emtiaze_to+=1
                print_score()





    else:
        if emtiaze_man>emtiaze_to:
            print('MOTEASEFANE BAKHTI!!!')
        elif emtiaze_man<emtiaze_to:
            print('TABRIK!!! BORDI!')
        else:
            print('MOSAVI SHODIM!')

        replay = (input('dobare bazi mikoni? (Y/N):')).lower()
        if replay == 'y':
            continue
        elif replay == 'n':
            break
        else:
            print('entekhab eshtebah')
            continue




# another solution!  :

# import random
# first_time = True
#
# while True:
#     if first_time:
#         dor = int(input('''Welcome to Rock-Paper-Scissors!
#          The rules are simple:
#          Rock crushes Scissors,
#          Scissors cuts Paper,
#          Paper covers Rock
#          How many rounds do you want to play? '''))
#         first_time = False
#     else:
#         dor = int(input('How many rounds this time?'))
#
#
#     com_score=0
#     my_score=0
#
#
#     def print_score():
#         print(f'Computer Score: {com_score}, Your Score: {my_score}')
#
#     def print_com_choice():
#         print(f'Computer chose: {com_choice}')
#     while com_score+my_score<dor:
#
#
#         my_choice=(input('Rock, Paper, or Scissors? ').lower().split())
#         rock=['rock','r']
#         paper=['paper','p']
#         scissors=['scissors','s']
#         if any(i in my_choice for i in rock) :
#             my_choice= 'rock'
#
#         elif any(i in my_choice for i in paper) :
#             my_choice= 'paper'
#         elif any(i in my_choice for i in scissors) :
#             my_choice= 'scissors'
#         else:
#             print('Invalid choice, try again!')
#             continue
#
#         r_p_s = ["rock", "paper", "scissors"]
#         com_choice = random.choice(r_p_s)
#
#
#         if my_choice == com_choice:
#             print("It's a tie!")
#         elif (my_choice == "rock" and com_choice == "scissors") or \
#              (my_choice == "scissors" and com_choice == "paper") or \
#              (my_choice == "paper" and com_choice == "rock"):
#             print(f"{my_choice.capitalize()} beats {com_choice}, you win!")
#             my_score += 1
#         else:
#             print(f"{com_choice.capitalize()} beats {my_choice}, computer wins!")
#             com_score += 1
#
#         print(f"Score - You: {my_score}, Computer: {com_score}")
#
#
#
#     else:
#         if com_score>my_score:
#             print('Computer wins the game!')
#         elif com_score<my_score:
#             print('You win the game! Congratulations!')
#         else:
#             print('It\'s a tie game!')
#
#         replay = (input('Do you want to play again? (Y/N):')).lower()
#         if replay == 'y':
#             continue
#         elif replay == 'n':
#             break
#         else:
#             print('Invalid input, try again!')
#             continue
