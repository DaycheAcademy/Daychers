####################################################### FIRST WAY #######################################################


### FUNC_1
def decision_cpu () :
    from random import randint
    cpu_choices_tuple = ("rock", "paper", "scissors")
    return cpu_choices_tuple[randint(0, 2)]

### FUNC_2
def investigating_user_input( level , string ) :
    if level == 1 and not string.isdigit() and ("quit" in string.lower().split(" ")) :
        return (1,"see you later")                          ### break
    if level == 1 and not string.isdigit() and ("quit" not in string.lower().split(" ")) :
        return (2," you shoud have entered an integer number (in simple form , without '.' ) or quit the game . not anything else.")                             ### continue
    if level == 1 and  string.isdigit() :
        return (3,"")                             ### OK
    if level == 2 and ( not string.isdigit() ) and ( "quit" in string.lower().split(' ') ) :
        return (4 ,"see you later")                            ### break
    if level == 2 and ( not string.isdigit() ) and ("paper" not in string.lower().split(' ')) and ("scissors" not in string.lower().split(' ')) and ("rock" not in string.lower().split(' ')):
        return (5,"please enter one of 'quit,rock,paper,scissors' . " )
    if level == 2 and string.isdigit() :
        return (6, "it is not a logical input , it shoud not be a number . ")
    if level == 2 and ( not string.isdigit() ) and (("paper" in string.lower().split(' ')) or ("scissors" in string.lower().split(' ')) or ( "rock" in string.lower().split(' ') ) ) :
        return (7,"")
    if level == 3 and string.lower() == "n" or string.lower() == "no":
        return (8,"see you later")                             ### break
    if level == 3 and string.lower() == "y" or string.lower() == "yes":
        return (9,"")                             ### continue  repeat
    if level == 3 and string.lower() != "n" and string.lower() != "no" and string.lower() != "y" and string.lower() != "yes":
        return (10,"invalid input.....enter just y(yes) or n(no). ")                             ### continue

### FUNC_3
def telling_current_result ( my_choice , cpu_choice ) :
    if "rock" in my_choice.lower().split(" ") and cpu_choice == "scissors":
        string = "you have entered rock while the cpu had choosen {0}".format(cpu_choice)
        return  (1  , string)
    if "scissors" in my_choice.lower().split(" ") and cpu_choice == "paper":
        string = "you have entered scissors while the cpu had choosen {0}".format(cpu_choice)
        return (1 , string)
    if "paper" in my_choice.lower().split(" ") and cpu_choice == "rock":
        string = "you have entered paper while the cpu had choosen {0}".format(cpu_choice)
        return (1 , string)
    if "scissors" in my_choice.lower().split(" ") and cpu_choice == "rock":
        string = "you have entered scissors while the cpu had choosen {0}".format(cpu_choice)
        return(0, string)
    if "paper" in my_choice.lower().split(" ") and cpu_choice == "scissors":
        string = "you have entered paper while the cpu had choosen {0}".format(cpu_choice)
        return (0, string)
    if "rock" in my_choice.lower().split(" ") and cpu_choice == "paper":
        string = "you have entered rock while the cpu had choosen {0}".format(cpu_choice)
        return (0, string)
    if ("rock" in my_choice.lower().split(" ") and cpu_choice == "rock") or ("scissors" in my_choice.lower().split(" ") and cpu_choice == "scissors") or ("paper" in my_choice.lower().split(" ") and cpu_choice == "paper"):
        string = "you and cpu have entered the same case , so the match result doesnt change. "
        return (-1, string)
    else :
        return (-1 , "ERROR")

### FUNC_4
def telling_final_result ( numb_win_you , numb_win_cpu , thrshld ) :
    if numb_win_you == int(thrshld) :
        return (1 ,"Congratulations you won the game!")
    elif numb_win_cpu == int(thrshld) :
        return (2 , "OH , The cpu won the game!")
    else:
        return (3 ,"")

### MAIN_BODY
flag_1 = 0
flag_2 = 0
flag_3 = 0
win_me = 0
win_cpu = 0
while (True) :
    if ( flag_1 == 0 ) :
        if flag_2 == 0 :
            string_input_1 = input( " if you want to play , enter number of wins for winner . and if you dont want, you can quit the game. : ")
            if investigating_user_input(1, string_input_1)[0] == 1 :
                print(investigating_user_input(1, string_input_1)[1])
                break
            if investigating_user_input(1, string_input_1)[0] == 2 :
                print(investigating_user_input(1, string_input_1)[1])
                continue
            if investigating_user_input(1, string_input_1)[0] == 3 :
                flag_2 = 1
        if investigating_user_input(1, string_input_1)[0] == 3 or (flag_1 == 0 and flag_2 == 1) :
            if flag_3 == 0 :
                selection_of_cpu = decision_cpu()
                my_choice_2 = input("Enter your choice while the CPU has choosen its choice : ")
                if investigating_user_input(2, my_choice_2)[0] == 4 :
                    print( investigating_user_input(2, my_choice_2)[1] )
                    break
                if investigating_user_input(2, my_choice_2)[0] == 5 :
                    print( investigating_user_input(2, my_choice_2)[1] )
                    flag_1 = 1
                    flag_2 = 1
                    continue
                if investigating_user_input(2, my_choice_2)[0] == 6 :
                    print( investigating_user_input(2, my_choice_2)[1] )
                    flag_1 = 1
                    flag_2 = 0
                    continue
                if investigating_user_input(2, my_choice_2)[0] == 7 :

                    if telling_current_result ( my_choice_2 , selection_of_cpu )[0] == 1 :
                        win_me += 1
                        print(telling_current_result(my_choice_2, selection_of_cpu)[1])
                        print("you : {0} , cpu : {1} ".format(win_me,win_cpu))
                    if telling_current_result( my_choice_2, selection_of_cpu )[0] == 0 :
                        win_cpu += 1
                        print(telling_current_result(my_choice_2, selection_of_cpu)[1])
                        print("you : {0} , cpu : {1} ".format(win_me, win_cpu))
                    if telling_current_result( my_choice_2, selection_of_cpu )[0] == -1 :
                        print(telling_current_result(my_choice_2, selection_of_cpu)[1])
                        print("you : {0} , cpu : {1} ".format(win_me, win_cpu))
                    elif (telling_final_result( win_me , win_cpu , string_input_1 )[0] == 1) or (telling_final_result( win_me , win_cpu , string_input_1 )[0] == 2) :
                        print( telling_final_result(win_me, win_cpu, string_input_1)[1] )
                        play_again_3 = input("Do you want to play again ? (yes/no) : ")
                        if investigating_user_input(3, play_again_3)[0] == 8 :
                            print(investigating_user_input(3, play_again_3)[1])
                            win_me = 0
                            win_cpu = 0
                            break
                        elif investigating_user_input(3, play_again_3)[0] == 9 :
                            print(investigating_user_input(3, play_again_3)[1])
                            flag_2 = 0
                            flag_1 = 0
                            flag_3 = 0
                            win_me = 0
                            win_cpu = 0
                            continue
                        elif investigating_user_input(3, play_again_3)[0] == 10:
                            print(investigating_user_input(3, play_again_3)[1])
                            flag_1 = -1
                            flag_2 = -1



            if flag_3 == 1 :
                play_again_3 = input("Do you want to play again ? (yes/no) : ")
                if investigating_user_input(3, play_again_3)[0] == 8 :
                    print(investigating_user_input(3, play_again_3)[1])
                    win_me = 0
                    win_cpu = 0
                    break
                elif investigating_user_input(3, play_again_3)[0] == 9 :
                    print(investigating_user_input(3, play_again_3)[1])
                    flag_1 = 0
                    flag_2 = 0
                    flag_3 = 0
                    win_me = 0
                    win_cpu = 0
                    continue
                elif investigating_user_input(3, play_again_3)[0] == 10 :
                    print( investigating_user_input(3, play_again_3)[1] )
                    flag_1 = -1
                    flag_2 = -1





    if ( flag_1 == -1 and flag_2 == -1 ):
        flag_1 = 0
        flag_2 = 1
        flag_3 = 1
    if ( flag_1 == 1 and flag_2 == 1 ):
        flag_1 = 0
        flag_2 = 1
    if ( flag_1 == 1 and flag_2 == 0 ):
        flag_1 = 0
        flag_2 = 1
        flag_3 = 0



####################################################### SECOND WAY #######################################################


win_me = 0
win_cpu = 0
flag_1 = 0
flag_2 = 0
flag_3 = 0
from random import randint

cpu_choices_tuple = ( "rock" , "paper" , "scissors" )

while (True) :


    if ( flag_1 == 0 ) :
        if flag_2 == 0 :
            inpt_number = input(" if you want to play , enter number of wins for winner . and if you dont want, you can quit the game. : ")
            if not inpt_number.isdigit():
                if "quit" in inpt_number.lower():
                    break
                else:
                    print(" you shoud have entered an integer number (in simple form , without '.' ) or quit the game . not anything else.")
                    continue
            if  inpt_number.isdigit():
                flag_2  = 1

        # elif inpt_number.isdigit() or ( flag_1 == 0 and flag_2 == 1):
        elif inpt_number.isdigit() or (flag_1 == 0 and flag_2 == 1):
            if flag_3 == 0:
                cpu_choice = cpu_choices_tuple[randint(0, 2)]
                my_choice = input("Enter your choice while the CPU has choosen its choice : ")
                my_choice_split = my_choice.lower().split(' ')
                if (not my_choice.isdigit()) and ("quit" in my_choice.lower().split(' ')):
                    break
                if (not my_choice.isdigit()) and ("paper" not in my_choice_split) and ("scissors" not in my_choice_split) and ("rock" not in my_choice_split):
                    flag_1 = 1
                    flag_2 = 1
                if my_choice.isdigit() or (flag_1 == 1 and flag_2 == 0):
                    flag_1 = 1
                    flag_2 = 0
                if (not my_choice.isdigit()) and (
                        ("paper" in my_choice_split) or ("scissors" in my_choice_split) or (
                        "rock" in my_choice_split)):
                    if "rock" in my_choice.lower().split(" ") and cpu_choice == "scissors":
                        print("you have entered rock while the cpu had choosen {0}".format(cpu_choice))
                        win_me += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if "scissors" in my_choice.lower().split(" ") and cpu_choice == "paper":
                        print("you have entered scissors while the cpu had choosen {0}".format(cpu_choice))
                        win_me += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if "paper" in my_choice.lower().split(" ") and cpu_choice == "rock":
                        print("you have entered paper while the cpu had choosen {0}".format(cpu_choice))
                        win_me += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if "scissors" in my_choice.lower().split(" ") and cpu_choice == "rock":
                        print("you have entered scissors while the cpu had choosen {0}".format(cpu_choice))
                        win_cpu += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if "paper" in my_choice.lower().split(" ") and cpu_choice == "scissors":
                        print("you have entered paper while the cpu had choosen {0}".format(cpu_choice))
                        win_cpu += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if "rock" in my_choice.lower().split(" ") and cpu_choice == "paper":
                        print("you have entered rock while the cpu had choosen {0}".format(cpu_choice))
                        win_cpu += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if ("rock" in my_choice.lower().split(" ") and cpu_choice == "rock") or (
                            "scissors" in my_choice.lower().split(" ") and cpu_choice == "scissors") or (
                            "paper" in my_choice.lower().split(" ") and cpu_choice == "paper"):
                        print("you and cpu have entered the same case , so the match result doesnt change. you : {0}, cpu : {1}".format(win_me, win_cpu))

                    if win_me == int(inpt_number) or win_cpu == int(inpt_number):  #### there is a winner
                        if (win_me > win_cpu):
                            print("Congratulations you won the game!")
                        elif (win_me < win_cpu):
                            print("OH , The cpu won the game!")
                        inpt = input("Do you want to play again ? (yes/no) : ")
                        if inpt.lower() == "n" or inpt.lower() == "no":
                            # flag_2 = 1
                            # flag_1 = 1
                            win_me = 0
                            win_cpu = 0
                            break
                        elif inpt.lower() == "y" or inpt.lower() == "yes":
                            flag_2 = 0
                            flag_1 = 0
                            flag_3 = 0
                            win_me = 0
                            win_cpu = 0
                            continue
                        else:
                            flag_1 = -1
                            flag_2 = -1

            if flag_3 == 1:
                inpt = input("Do you want to play again ? (yes/no) : ")
                if inpt.lower() == "n" or inpt.lower() == "no":
                    win_me = 0
                    win_cpu = 0
                    break
                elif inpt.lower() == "y" or inpt.lower() == "yes":
                    flag_2 = 0
                    flag_1 = 0
                    flag_3 = 0
                    win_me = 0
                    win_cpu = 0
                    continue
                else:
                    flag_1 = -1
                    flag_2 = -1



    if ( flag_1 == -1 and flag_2 == -1 ):
        print("invalid input.....enter just y(yes) or n(no). ")
        flag_1 = 0
        flag_2 = 1
        flag_3 = 1
    if ( flag_1 == 1 and flag_2 == 1 ):
        print("please enter one of 'quit,rock,paper,scissors' . ")
        flag_1 = 0
        flag_2 = 1
    if ( flag_1 == 1 and flag_2 == 0 ):
        print("it is not a logical input , it shoud not be a number . ")
        flag_1 = 0
        flag_2 = 1
        flag_3 = 0


####################################################### THIRD WAY #######################################################


win_me = 0
win_cpu = 0
flag_2=0
flag_1=0
cpu_choices_tuple = ("rock" , "paper" , "scissors")
while (True and flag_2==0 and flag_1==0) :
    inpt_number = input ( " if you want to play , enter number of wins for winner . and if you dont want, you can quit the game. : " )
    if not inpt_number.isdigit() :
        if  "quit" in inpt_number.lower():
            # flag_2=1
            break
        else :
            print( " you shoud have entered an integer number (in simple form , without '.' ) or quit the game . not anything else.")
            continue

    elif inpt_number.isdigit() :
        flag_1 = 1
        while (True and flag_2 == 0  and flag_1==1):
            from random import randint
            cpu_choice = cpu_choices_tuple[randint(0, 2)]

            my_choice = input("Enter your choice while the CPU has choosen its choice : ")
            my_choice_split = my_choice.lower().split(' ')
            if (not my_choice.isdigit()) and ("quit"  in my_choice.lower().split(' ')):
                flag_1=1
                flag_2=1
                break
            if (not my_choice.isdigit()) and ( "paper" not in my_choice_split) and ("scissors" not in my_choice_split) and ("rock" not in my_choice_split) :
                print("please enter one of 'quit,rock,paper,scissors'  ")
                continue

            if my_choice.isdigit():  ### the choise is not in the desired string (It is a number)
                print("it is not a logical input , it shoud not be a number")
                continue
            if (not my_choice.isdigit()) and ( ("paper"  in my_choice_split) or ("scissors"   in my_choice_split) or ("rock"   in my_choice_split)):
                if ( ("paper"  in my_choice_split) or ("scissors"   in my_choice_split) or ("rock"   in my_choice_split)) :
                    if "quit" in my_choice.lower().split(' ') :
                        flag_2=1
                        break
                    if "rock" in my_choice.lower().split(" ")  and cpu_choice == "scissors":
                        print("you have entered rock while the cpu had choosen {0}".format( cpu_choice) )
                        win_me += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if  "scissors" in my_choice.lower().split(" ") and cpu_choice == "paper" :
                        print("you have entered scissors while the cpu had choosen {0}".format(cpu_choice))
                        win_me += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)
                    if "paper" in my_choice.lower().split(" ") and cpu_choice == "rock":
                        print("you have entered paper while the cpu had choosen {0}".format(cpu_choice))
                        win_me += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)

                    # if (my_choice.lower() == "s" or my_choice.lower() == "scissors") and cpu_choice == "rock":
                    if "scissors" in my_choice.lower().split(" ") and cpu_choice == "rock":
                        print("you have entered scissors while the cpu had choosen {0}".format(cpu_choice))
                        win_cpu += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)

                    if "paper" in my_choice.lower().split(" ") and cpu_choice == "scissors":
                        print("you have entered paper while the cpu had choosen {0}".format(cpu_choice))
                        win_cpu += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)

                    if "rock" in my_choice.lower().split(" ") and cpu_choice == "paper":
                        print("you have entered rock while the cpu had choosen {0}".format(cpu_choice))
                        win_cpu += 1
                        print("you : ", win_me)
                        print("cpu : ", win_cpu)

                    if ("rock" in my_choice.lower().split(" ") and cpu_choice == "rock") or ("scissors" in my_choice.lower().split(" ") and cpu_choice == "scissors") or ("paper" in my_choice.lower().split(" ") and cpu_choice == "paper") :
                        print("you and cpu have entered the same case , so the match result doesnt change. you : {0}, cpu : {1}".format( win_me, win_cpu))
                    if win_me == int(inpt_number) or win_cpu == int(inpt_number):  #### there is a winner
                        if win_me > win_cpu:
                            print("Congratulations you won the game!")
                        else :
                            print("OH , The cpu won the game!")
                        while True:
                            inpt = input("Do you want to play again ? (yes/no) : ")
                            if inpt.lower() == "n" or inpt.lower() == "no":
                                flag_2 = 1
                                flag_1 = 1
                                win_me = 0
                                win_cpu = 0
                                break
                            elif inpt.lower() == "y" or inpt.lower() == "yes":
                                flag_2 = 0
                                flag_1 = 0
                                win_me = 0
                                win_cpu = 0
                                break
                            else:
                                print("please enter something valid")
                                continue


2