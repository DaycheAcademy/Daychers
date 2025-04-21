
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


        elif ( letter >= "A" and letter <= "Z" and shiftKey > 0 ) :
            for ind , alpha in enumerate(ALPHABET, start=1) :
                if letter == alpha :
                    if shiftKey + ind <= 26 :
                        new_index = shiftKey + ind -1
                        empty_string += ALPHABET[new_index]
                    elif shiftKey + ind > 26 :
                        new_index = (shiftKey + ind) % len(ALPHABET) -1
                        empty_string += ALPHABET[new_index]

        else :
            empty_string += letter
    return empty_string

#############################################################################################################

def caesar_decrypt(cipherText, shiftKey , inverse_alphabet_arg = 0 ) :
    # length = len(cipherText)
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


        elif ( letter >= "a" and letter <= "z" and shiftKey < 0 ) :
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


#############################################################################################################

alphabet = "abcdefghijklmnopqrstuvwxyz"

var_row_a_string = list()
var_col_key = list()

#############################################################################################################

def making_two_dim_list () :
    two_dim_list = list()
    for i in range( 0 , 26 ) :
        List = list()
        for j in range( 0 , 26 ) :
            List.append( 0 )
        two_dim_list.append( List )
    return two_dim_list

#############################################################################################################

def show ( LIST ) :
    for i in range( 0 , 26) :
        print(LIST[i],'\n')

#############################################################################################################

def make_schedule_small( list ) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, 26):
        if i == 0:
            alphabet = caesar_encrypt(alphabet, 0)
        else:
            alphabet = caesar_encrypt(alphabet, 1)
        for j in range(0, 26):
            list[i][j] = alphabet[j]
    return list

#############################################################################################################

def make_schedule_capital( list ) :
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, 26) :
        if i == 0 :
            alphabet = caesar_encrypt(alphabet, 0)
        else :
            alphabet = caesar_encrypt(alphabet, 1)
        for j in range(0, 26) :
            list[i][j] = alphabet[j]
    return list


############################################## Main body for encryption ##############################################


print("\n\n"+"_encryption_"*13+"\n\n")

LIST = making_two_dim_list()

schedule_small = make_schedule_small(  LIST  )

show ( schedule_small )
print("\n")





a_string = "attackatdawn {2}"     ### by user
mainkey = "lemon"                 ### by user





k = -1
row_a_string=""
col_key=""
for i in range( 0,len(a_string) ) :
    if a_string[i] >= "a" and a_string[i] <= "z" :
        k += 1

        row_a_string += a_string[i]
        if k==len(mainkey) :
            k = 0
        col_key += mainkey[k]
    else:
        col_key += a_string[i]
        row_a_string += a_string[i]

print("1_row(a_text by user) : ",row_a_string)
print("2_key (by user) : " , mainkey)
# print("* col(__key_) : ",col_key)


print("\n")


for  i in  row_a_string :
    for ind,j in enumerate( alphabet, start = 0 ) :
        if i == j :
            var_row_a_string.append(ind)
    if i not in alphabet :
        var_row_a_string.append(i)
for  i in  col_key :
    for ind,j in enumerate( alphabet, start = 0 ) :
        if i == j :
            var_col_key.append(ind)
    if i not in alphabet :
        var_col_key.append(i)

# print("var_row_a_string : ",var_row_a_string)
# print("var_col_key      : ",var_col_key)


encrypted_text = ""
for i,j in zip(var_row_a_string,var_col_key) :
    if type(i) != int :
        encrypted_text += i
    elif type(i) == int :
        encrypted_text += schedule_small[i][j]

print("\n")

print("result : ",encrypted_text)


############################################## Main body for decryption ##############################################


print("\n","*"*160)
print("\n\n"+"_decryption_"*13+"\n\n")

schedule_small = make_schedule_small(  LIST  )

show ( schedule_small )
print("\n")


result = "lxfopvefrnhr {2} s"     ### recieved message from server
key_for_decryption = "lemon"


k = -1
row_a_string=""
col_key=""
for i in range( 0,len(result) ) :
    if result[i] >= "a" and result[i] <= "z" :
        k += 1
        row_a_string += result[i]
        if k==len(key_for_decryption) :
            k = 0
        col_key += key_for_decryption[k]
    else:
        col_key += result[i]
        row_a_string += result[i]

print("1_Recieved message (result _ by user) : ",row_a_string)
print("2_key ( by user) : ", key_for_decryption )
# print("*col(__key_) : ",col_key)


print("\n")

var_col_key =[]

for i in col_key :
    if i not in alphabet:
        var_col_key.append(i)
    else :
        for ind, j in enumerate(alphabet, start=0):
            if i == j:
                var_col_key.append(ind)


# print("var_col_key_numbers    : ",var_col_key)


var_row_result =[]
for  i in  result :
    if i not in alphabet:
        var_row_result.append(i)
    for ind,j in enumerate( alphabet, start = 0 ) :
        if i == j :
            var_row_result.append(ind)

# print("var_row_result_numbers : " ,var_row_result )

print("\n")
# print("result = ",result)


message  = ""

for ind_j , j in enumerate( var_col_key,start = 0 ) :

    if type(j) == type(369) :
        s = schedule_small[:][j]

    if result[ind_j] not in alphabet :

        message += result[ind_j]
    if result[ind_j] in alphabet :

        for ind_i , i in enumerate(s, start=0):
            if i == result[ind_j] :

                message += schedule_small[ind_i][0]

print("Main Message : ",message)





