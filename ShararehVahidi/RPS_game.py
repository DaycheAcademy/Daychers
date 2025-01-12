import random
numOfGames=input ('''*press q to exit the program*
 Rock Paper Scissors is a classic chance game.
First things first!, rules:
\trock crushes scissors
\tpaper covers rock
\tscissors cuts paper
How many times do you like to play in this round?:''')

while numOfGames.lower() not in ('q','quit') :
        if not numOfGames.isdecimal():
            numOfGames = input("Plese Enter a positive Integer : ")
        elif numOfGames == '0':
                print("It seems that you are not in the mood of playing :(")
                break
        else:
            numOfGames=int(numOfGames)
            won = 0
            lost = 0
            draw = 0
            while numOfGames >0:
                user_choice= input("To try your chance, Enter p for paper, r for rock or s for scissors:")
                if user_choice.lower() in ('q','quit'):
                    print('Bye!')
                    exit()
                else:
                    RPS= 'rock', 'paper', 'scissors'
                    comp_choice=random.choice(RPS)

                    rock= 'r','rock','rack','ruck','roc'
                    paper='p','paper','peper','papar'
                    scissors='s','scissors','scisors','sissor','scissor'

                    words=(user_choice.lower().split(' '))
                    # print(words)

                    if any(word in rock for word in words ):
                        print(f'your choice is rock, mine was {comp_choice}:')
                        if comp_choice=='paper':
                            print("I'm the winner!")
                            lost +=1
                        elif comp_choice=='scissors':
                            print("you're the winner!")
                            won +=1
                        else:
                            print("draw!")
                            draw +=1
                        numOfGames -= 1


                    elif any(word in paper for word in words ):
                        print(f'your choice is paper, mine was {comp_choice}:')
                        if comp_choice=='scissors':
                            print("I'm the winner!")
                            lost +=1
                        elif comp_choice=='rock':
                            print("you're the winner!")
                            won +=1
                        else:
                            print("draw!")
                            draw +=1

                        numOfGames -= 1


                    elif any(word in scissors for word in words ):
                        print(f'your choice is scissors, mine was {comp_choice}:')
                        if comp_choice=='rock':
                            print("I'm the winner!")
                            lost +=1
                        elif comp_choice=='paper':
                            print("you're the winner!")
                            won +=1
                        else:
                            print("draw!")
                            draw +=1
                        numOfGames -= 1
                    else:
                        continue
                    # print(numOfGames)
                    continue
                break
            print(f"you'r scores in this round: \nwon: {won}, lost:{lost}, draw:{draw}")
            numOfGames=input('if you wanna play again, enter number of the games in this round:')
            if numOfGames.lower() in ('q', 'quit'):
                break
            else:
                continue
            break
        # print('where am I?')
else:
    print('Bye!')
    exit()
