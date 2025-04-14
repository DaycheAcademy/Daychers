# #################################################  week7_project4  ##################################################
# import math
# ############################################## TASK_1 , TASK_2 , TASK_3 , TASK_4


def caesar_encrypt( plainText , shiftKey , inverse_alphabet_arg = 0) :
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


        elif ( letter >= "a" and letter <= "z" and shiftKey < 0 ) :    
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


        elif (letter >= "A" and letter <= "Z" and shiftKey < 0) :
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



#### EXAMPLE :


s_in = "aNz :2?"

print( caesar_encrypt(s_in,3) )        ### dQc :2?
print( caesar_encrypt(s_in,28) )       ### cPb :2?
print( caesar_encrypt(s_in,3,1) )      ### xKw :2?
print( caesar_encrypt(s_in,28,1) )     ### yLx :2?

print( caesar_encrypt(s_in,-3) )       ### xKw :2?
print( caesar_encrypt(s_in,-28) )      ### yLx :2?
print( caesar_encrypt(s_in,-3,1) )     ### dQc :2?
print( caesar_encrypt(s_in,-28,1) )    ### cPb :2?



print("*"*25)

s_in = "he?L l:o4%6"
print( caesar_encrypt(s_in,3) )    ### kh?O o:r4%6

print("*"*25)

s_in = "zHoOr"
print( caesar_encrypt(s_in,28) )  ### bJqQt

print("*"*25)

s_in = "he?L l:o4%6"
print( caesar_encrypt(s_in,-3) )    ### eb?I i:l4%6

print("*"*25)

s_in = "zHoOr"
print( caesar_encrypt(s_in,-28) )   ### xFmMp

print("#"*50)


# ##########################################################################################################################################
# ##########################################################################################################################################
# ##########################################################################################################################################


def caesar_decrypt(cipherText, shiftKey , inverse_alphabet_arg = 0 ) :

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
            for ind , alpha in enumerate(alphabet_inverse, start=1) :
                if letter == alpha :
                    if (-1*shiftKey) + ind <= 26 :
                        new_index = (shiftKey) + ind - 1
                        empty_string += alphabet_inverse[new_index]
                    elif (-1*shiftKey) + ind > 26 :
                        new_index = ((shiftKey) + ind) % len(alphabet_inverse) - 1
                        empty_string += alphabet_inverse[new_index]


        elif ( letter >= "A" and letter <= "Z" and shiftKey > 0 ) :              ### if "he?l l:o4%6"   ---->   "khhe?ol ol:ro4%6"
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


#### EXAMPLE :

s_in = "kh?O o:r4%6"
print( caesar_decrypt(s_in,3) )    ### he?L l:o4%6

print("*"*25)

s_in = "bJqQt"
print( caesar_decrypt(s_in,28) )   ### zHoOr

print("*"*25)

s_in = "eb?I i:l4%6"
print( caesar_decrypt(s_in,-3) )   ### he?L l:o4%6

print("*"*25)

s_in = "xFmMp"
print( caesar_decrypt(s_in,-28) )   ### zHoOr

print("*"*25)




s_in = "dQc :2?"

print( caesar_decrypt( "dQc :2?" ,3) )      ### aNz :2?
print( caesar_decrypt( "cPb :2?" ,28) )     ### aNz :2?
print( caesar_decrypt( "xKw :2?" ,3,1) )    ### aNz :2?
print( caesar_decrypt( "yLx :2?" ,28,1) )   ### aNz :2?

print( caesar_decrypt( "xKw :2?" ,-3) )     ### aNz :2?
print( caesar_decrypt( "yLx :2?" ,-28) )    ### aNz :2?
print( caesar_decrypt( "dQc :2?" ,-3,1) )   ### aNz :2?
print( caesar_decrypt( "cPb :2?" ,-28,1) )  ### aNz :2?

##########################################################################################################################################
##########################################################################################################################################
###############################################################################################################################