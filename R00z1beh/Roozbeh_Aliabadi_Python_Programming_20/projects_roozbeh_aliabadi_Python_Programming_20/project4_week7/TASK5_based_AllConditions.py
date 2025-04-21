def caesar_decrypt(cipherText, shiftKey, inverse_alphabet_arg=0):
    # length = len(cipherText)
    if inverse_alphabet_arg == 0:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ALPHABET = alphabet.upper()

    if inverse_alphabet_arg == 1:
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        ALPHABET = alphabet.upper()

    empty_string = ""
    for letter in cipherText:
        if (letter >= "a" and letter <= "z" and shiftKey > 0):
            for ind, alpha in enumerate(alphabet, start=1):
                if letter == alpha:
                    if shiftKey + ind <= 26:
                        new_index = -shiftKey + ind - 1
                        empty_string += alphabet[new_index]
                    elif shiftKey + ind > 26:
                        new_index = (-shiftKey + ind) % len(alphabet) - 1
                        empty_string += alphabet[new_index]


        elif (letter >= "a" and letter <= "z" and shiftKey < 0):  ###################### complete this  complete this
            alphabet_inverse = alphabet[::-1]
            # print("alphabet_inverse : ",alphabet_inverse)
            # shiftKey = -1 * shiftKey
            for ind, alpha in enumerate(alphabet_inverse, start=1):
                if letter == alpha:
                    if (-1 * shiftKey) + ind <= 26:
                        new_index = (shiftKey) + ind - 1
                        # print("ind for",letter,"= ", ind)
                        # print("ind : ",ind)
                        # print("new_index : ",new_index)
                        empty_string += alphabet_inverse[new_index]
                    elif (-1 * shiftKey) + ind > 26:
                        new_index = ((shiftKey) + ind) % len(alphabet_inverse) - 1
                        empty_string += alphabet_inverse[new_index]


        elif (letter >= "A" and letter <= "Z" and shiftKey > 0):  ### if "he?l l:o4%6"   ---->   "khhe?ol ol:ro4%6"
            for ind, alpha in enumerate(ALPHABET, start=1):
                if letter == alpha:
                    if -shiftKey + ind <= 26:
                        new_index = -shiftKey + ind - 1
                        empty_string += ALPHABET[new_index]
                    elif -shiftKey + ind > 26:
                        new_index = (-shiftKey + ind) % len(ALPHABET) - 1
                        empty_string += ALPHABET[new_index]


        elif (letter >= "A" and letter <= "Z" and shiftKey < 0):
            ALPHABET_INVERSE = ALPHABET[::-1]
            # shiftKey = -1 * shiftKey
            for ind, alpha in enumerate(ALPHABET_INVERSE, start=1):
                if letter == alpha:
                    if (-1 * shiftKey) + ind <= 26:
                        new_index = (shiftKey) + ind - 1
                        empty_string += ALPHABET_INVERSE[new_index]
                    elif (-1 * shiftKey) + ind > 26:
                        new_index = ((shiftKey) + ind) % len(ALPHABET_INVERSE) - 1
                        empty_string += ALPHABET_INVERSE[new_index]

        else:
            empty_string += letter
    return empty_string



################################################################################33

### EXAMPLE :

s_in = "hVWG wGhVS pSGH qCADIHSF sLSFQWGS w vOJS eJSF sLDSFWSBQSR 2"


for Shift_Key in range(1, 27):
    print(caesar_decrypt(s_in, Shift_Key, inverse_alphabet_arg=0))
    # print(caesar_decrypt(s_in, -1*Shift_Key, inverse_alphabet_arg=1))          ### Repetitive and removable
    # print(caesar_decrypt(s_in, -1*Shift_Key, inverse_alphabet_arg=0))          ### Repetitive and removable
    print(caesar_decrypt(s_in, Shift_Key, inverse_alphabet_arg=1))
    print("-" * 60)
