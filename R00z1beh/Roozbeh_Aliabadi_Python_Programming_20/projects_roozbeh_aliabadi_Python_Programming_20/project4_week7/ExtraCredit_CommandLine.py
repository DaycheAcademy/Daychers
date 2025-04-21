#
# #################################################  ExtraCredit_CommandLine_week7_project4  ##################################################


def caesar_encrypt( plainText , shiftKey , inverse_alphabet_arg = 0) :
    # length = len(plainText)
    # alphabet = ""
    # ALPHABET = ''
    if inverse_alphabet_arg == 0 :
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ALPHABET = alphabet.upper()

    if inverse_alphabet_arg == 1 :
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        ALPHABET = alphabet.upper()

    empty_string = ""
    for letter in plainText :
        if (letter >= "a" and letter <= "z" and shiftKey > 0) :
            for ind , alpha in enumerate(alphabet, start=1) :
                if letter == alpha :
                    if shiftKey + ind <= 26:
                        new_index = shiftKey + ind - 1
                        empty_string += alphabet[new_index]
                    elif shiftKey + ind > 26:
                        new_index = (shiftKey + ind) % len(alphabet) - 1
                        empty_string += alphabet[new_index]


        elif ( letter >= "a" and letter <= "z" and shiftKey < 0 ) :   ###################### complete this  complete this
            alphabet_inverse = alphabet[::-1]
            # print("alphabet_inverse : ",alphabet_inverse)
            # shiftKey = -1 * shiftKey
            for ind , alpha in enumerate(alphabet_inverse, start=1) :
                if letter == alpha :
                    if (-1*shiftKey) + ind <= 26 :
                        new_index = (-1*shiftKey) + ind -1
                        # print("ind : ",ind)
                        # print("new_index : ",new_index)
                        empty_string += alphabet_inverse[new_index]
                    elif (-1*shiftKey) + ind > 26 :
                        new_index = ((-1*shiftKey) + ind) % len(alphabet_inverse) - 1
                        empty_string += alphabet_inverse[new_index]


        elif ( letter >= "A" and letter <= "Z" and shiftKey > 0 ) :              ### if "he?l l:o4%6"   ---->   "khhe?ol ol:ro4%6"
            for ind , alpha in enumerate(ALPHABET, start=1) :
                if letter == alpha :
                    if shiftKey + ind <= 26 :
                        new_index = shiftKey + ind -1
                        empty_string += ALPHABET[new_index]
                    elif shiftKey + ind > 26 :
                        new_index = (shiftKey + ind) % len(ALPHABET) -1
                        empty_string += ALPHABET[new_index]


        elif (letter >= "A" and letter <= "Z" and shiftKey < 0) :   ###################### complete this  complete this
            ALPHABET_INVERSE = ALPHABET[::-1]
            # shiftKey = -1 * shiftKey
            for ind, alpha in enumerate(ALPHABET_INVERSE, start=1):
                if letter == alpha:
                    if (-1*shiftKey) + ind <= 26:
                        new_index = (-1*shiftKey) + ind -1
                        empty_string += ALPHABET_INVERSE[new_index]
                    elif (-1*shiftKey) + ind > 26:
                        new_index = ((-1*shiftKey) + ind) % len(ALPHABET_INVERSE) - 1
                        empty_string += ALPHABET_INVERSE[new_index]

        else :
            empty_string += letter
    return empty_string

############################################################################################################
############################################################################################################
############################################################################################################

def caesar_decrypt(cipherText, shiftKey , inverse_alphabet_arg = 0 ) :
    # length = len(cipherText)
    # alphabet = ""
    # ALPHABET = ''
    if inverse_alphabet_arg == 0 :
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ALPHABET = alphabet.upper()

    if inverse_alphabet_arg == 1 :
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        ALPHABET = alphabet.upper()

    empty_string = ""
    for letter in cipherText :
        if (letter >= "a" and letter <= "z" and shiftKey > 0) :
            for ind , alpha in enumerate(alphabet, start=1) :
                if letter == alpha :
                    if shiftKey + ind <= 26:
                        new_index = -shiftKey + ind - 1
                        empty_string += alphabet[new_index]
                    elif shiftKey + ind > 26:
                        new_index = (-shiftKey + ind) % len(alphabet) - 1
                        empty_string += alphabet[new_index]


        elif ( letter >= "a" and letter <= "z" and shiftKey < 0 ) :   ###################### complete this  complete this
            alphabet_inverse = alphabet[::-1]
            # print("alphabet_inverse : ",alphabet_inverse)
            # shiftKey = -1 * shiftKey
            for ind , alpha in enumerate(alphabet_inverse, start=1) :
                if letter == alpha :
                    if (-1*shiftKey) + ind <= 26 :
                        new_index = (shiftKey) + ind - 1
                        # print("ind for",letter,"= ", ind)
                        # print("ind : ",ind)
                        # print("new_index : ",new_index)
                        empty_string += alphabet_inverse[new_index]
                    elif (-1*shiftKey) + ind > 26 :
                        new_index = ((shiftKey) + ind) % len(alphabet_inverse) - 1
                        empty_string += alphabet_inverse[new_index]



        elif ( letter >= "A" and letter <= "Z" and shiftKey > 0 ) :
            for ind , alpha in enumerate(ALPHABET, start=1) :
                if letter == alpha :
                    if -shiftKey + ind <= 26 :
                        new_index = -shiftKey + ind - 1
                        empty_string += ALPHABET[new_index]
                    elif -shiftKey + ind > 26 :
                        new_index = (-shiftKey + ind) % len(ALPHABET) - 1
                        empty_string += ALPHABET[new_index]


        elif (letter >= "A" and letter <= "Z" and shiftKey < 0) :
            ALPHABET_INVERSE = ALPHABET[::-1]
            # shiftKey = -1 * shiftKey
            for ind, alpha in enumerate(ALPHABET_INVERSE, start=1):
                if letter == alpha:
                    if (-1*shiftKey) + ind <= 26:
                        new_index = (shiftKey) + ind -1
                        empty_string += ALPHABET_INVERSE[new_index]
                    elif (-1*shiftKey) + ind > 26:
                        new_index = ((shiftKey) + ind) % len(ALPHABET_INVERSE) - 1
                        empty_string += ALPHABET_INVERSE[new_index]

        else :
            empty_string += letter
    return empty_string


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


def caesar_crack( cipherText ) :
    alphabet_ ="abcdefghijklmnopqrstuvwxyz"
    dict_for_max = {}
    list_of_tuple_inverse = []
    for i in cipherText :
        if i not in dict_for_max :
            dict_for_max[i] = 1
        dict_for_max[i] += 1
    list_of_tuples = dict_for_max.items()
    for i,j in list_of_tuples :
        list_of_tuple_inverse .append( (j,i) )
    list_of_tuple_inverse.sort()

    for ind , i in enumerate(alphabet_,start=1) :
        if i == list_of_tuple_inverse[-1][1].lower() :
            indx_number = ind
    shift_value = indx_number - 5
    return caesar_decrypt( cipherText , shift_value , inverse_alphabet_arg = 0 )


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

def crack_CaesarCipher ( a_text ) :
    for i in range(1,26) :
        print( "shift {0} , normal alphabet : {1}".format(i,caesar_decrypt ( a_text , shiftKey = i ,inverse_alphabet_arg = 0 )) )
        print( "shift {0} , normal alphabet : {1}".format(-1*i,caesar_decrypt ( a_text , shiftKey = -1*i ,inverse_alphabet_arg = 0 )) )
        print("shift {0} , normal inverse alphabet : {1}".format(i, caesar_decrypt(a_text, shiftKey=i, inverse_alphabet_arg=1)))
        print("shift {0} , normal inverse alphabet : {1}".format(-1 * i, caesar_decrypt(a_text, shiftKey=-1 * i,inverse_alphabet_arg=1)))
        print("---------------------------------------------------------------------------")

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

not_suitable = 0
a_text_flag = 0
en_de_cryption_flag = 0
shift_flag = 0
alphabet_flag = 0
allow = 0

while (True) :

    if a_text_flag == 0 :
        a_text = input("* Enter a string : ")
        if a_text == "q" :
            break
        else :
            a_text_flag = 1
    ###############################################################
    if en_de_cryption_flag == 0 :
        en_de_cryption = input("1_encryption , 2_decruption :")
        if en_de_cryption_flag == "q" :
            break
        elif  en_de_cryption=="1" or en_de_cryption=="2" :
            en_de_cryption_flag = 1
            shift_flag = 0
            alphabet_flag = 0
        else :
            print("! Just 1 or 2....Nothing else !")
            shift_flag = -1
            alphabet_flag = -1
    ###############################################################
    if shift_flag == 0 :
        shift = input("* Enter value shift : ")
        if shift == "q":
            break
        elif shift.strip("-").strip("+").isdigit() :
            shift_flag = 1
            alphabet_flag = 0
        else :
            print("! Enter an integer number !")
            alphabet_flag = -1
    ###############################################################
    if alphabet_flag == 0 :
        alphabet = input("1_normal , 2_inverse : ")
        if alphabet == "q" :
            break
        elif  alphabet=="1" or alphabet=="2" :
            alphabet_flag = 1
            allow = 1
        else :
            print("Just 1 or 2....Nothing else")
            allow = 0

    if alphabet_flag == 1 and a_text_flag == 1 and shift_flag == 1 and en_de_cryption_flag == 1 and allow == 1 :
        if en_de_cryption == "1" and not_suitable == 0 :
            print("* Result : ",caesar_encrypt( a_text, int(shift) , inverse_alphabet_arg = int(alphabet)-1 ) )
            # print( "* caesar_crack encryption based letter 'e' : ",caesar_crack(a_text))

            quit_again = input("again==(a)   or    quit==(q) ?")
            if quit_again == "a":
                print("*" * 100)
                a_text_flag = 0
                en_de_cryption_flag = 0
                shift_flag = 0
                alphabet_flag = 0
                allow = 0
            elif quit_again == "q":
                break
            else:
                print("! Enter suitable input !")
                not_suitable = 1

        if en_de_cryption == "2" and not_suitable == 0 :
            print("* Result : ",caesar_decrypt(a_text, int(shift), inverse_alphabet_arg=int(alphabet) - 1))
            print("#" * 50)
            print("* caesar_crack encryption based letter 'e' : ", caesar_crack(a_text))
            print("#"*50)
            print("* caesar_crack encryption all conditions : \n")
            # print("#" * 50)
            print( crack_CaesarCipher(a_text) )

            quit_again = input("again==(a)   or    quit==(q) ?")
            if quit_again == "a":
                print("*" * 100)
                a_text_flag = 0
                en_de_cryption_flag = 0
                shift_flag = 0
                alphabet_flag = 0
                allow = 0
                not_suitable = 0
            elif quit_again == "q":
                break
            else:
                print("! Enter suitable input !")
                not_suitable = 1

        if not_suitable == 1 :
            quit_again = input("again==(a)   or    quit==(q) ?")
            if quit_again == "a":
                print("*" * 100)
                a_text_flag = 0
                en_de_cryption_flag = 0
                shift_flag = 0
                alphabet_flag = 0
                allow = 0
                not_suitable = 0
            elif quit_again == "q":
                break
            else:
                print("! Enter suitable input !")
                not_suitable = 1








