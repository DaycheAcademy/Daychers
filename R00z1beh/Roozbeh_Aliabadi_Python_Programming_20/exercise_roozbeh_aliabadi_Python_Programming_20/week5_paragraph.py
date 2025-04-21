###########################################################    1    ##########################################################

# my_paragraph ="Here, for the Aston, the      (empty) maintenance list was instantiated with the first statement. An element was added to it with the append function , being a dictionary containing the details of that first maintenance event. " ### 35
my_paragraph = "     I am Ana .   ... I am from Guatemala.I am 20 years,old.My brother,Pedro is here too. Pedro is 19 years old. We both study English at CCC. We are Spanish.Pedro and I have black hair and black eyes.We are not tall,and we are not thin.We are average in height and weight"
### too 18 + eyes 23 + 16 = 57


# Task 1: Count the number of words in the paragraph.

WordSet = set()
print( my_paragraph   )
my_paragraph += " "
first_level = 0
second_level = 0
cntrl_p = 0
cntrl_n = 0
cnt = 0
for indx,scaner in enumerate( my_paragraph , 0 ) :
    # print(scaner)
    if  ( ( (ord(scaner.lower()) >= 97 and ord(scaner.lower()) <= 122) ) or ( ( ord(scaner.lower()) >= 48 and ord(scaner.lower()) <= 57) )  ) :
        cntrl_p += 1
        if cntrl_p == 1 :
             first_level = indx
    if  not ( ( (ord(scaner.lower()) >= 97 and ord(scaner.lower()) <= 122) ) or ( ( ord(scaner.lower()) >= 48 and ord(scaner.lower()) <= 57) ) ) and cntrl_p != 0 :
        cntrl_n += 1
        if cntrl_n == 1 :
            second_level = indx
            cnt += 1
            WordSet.add( my_paragraph.lower() [ first_level:second_level ] )
            cntrl_p = 0
            cntrl_n = 0

print( "\nThere are {0} words in the paragraph ".format(cnt) )


print("*"*80)


### TASK 2
print( WordSet )
print( len(WordSet) )


print("*"*80)


### TASK 3
ref_tobe = {"am" , "is" , "are" ,"was" ,"were"}
print( ref_tobe.intersection(WordSet) )


print("*"*80)


### TASK_4
dict_tobe = dict()
for i in ref_tobe.intersection(WordSet) :
    for i in my_paragraph.lower() :
        if i not in  dict_tobe  :
            dict_tobe[i] = 0
        if i in dict_tobe  :
            dict_tobe[i] += 1
print( dict_tobe )



print("*"*80)
print("\n\n")

###########################################################    2    ##########################################################
print("#"*200)

# my_paragraph ="     Here, for the Aston, the      (empty) maintenance list was instantiated with the first statement. An element was added to it with the append function , being a dictionary containing the details of that first maintenance event. " ### 35
my_paragraph = "     I am Ana.I am from Guatemala.I am 20 years,old.My brother,Pedro is here too. Pedro is 19 years old. We both study English at CCC. We are Spanish.Pedro and I have black hair and black eyes.We are not tall,and we are not thin.We are average in height and weight"
# ### too 18 + eyes 23 + 16 = 57

# # Task 1: Count the number of words in the paragraph.
print( "0_MAIN :"+my_paragraph)
my_paragraph_new = my_paragraph.strip(".").strip(" ").strip("!")
my_paragraph_new  += " "

word_set = set()
first_level = 0
cnt=0
for indx,scaner in enumerate(my_paragraph_new,0) :
    if scaner == "," or scaner == " " or scaner == "." :    ### if scaner == "," or scaner == " " or scaner == "." :
        my_paragraph_new = my_paragraph_new.replace(scaner," ")

my_paragraph_new_2_list = my_paragraph_new.split(" ")

number_of_words = len( my_paragraph_new_2_list)-my_paragraph_new_2_list.count("")

first_level = 0
for indx,scaner in enumerate(my_paragraph_new,0) :
    if scaner == " " :
        word_set.add( my_paragraph_new[first_level:indx].lower() )
        first_level = indx + 1

print( "There are {0} words in the paragraph ".format(number_of_words) )


print("*"*80)


### TASK_2
word_set.remove("")
print(word_set)
print( len( word_set ) )


print("*"*80)


### TASK_3
ref_tobe_verbs = {"am" , "is" , "are" ,"was" ,"were"}
print( ref_tobe_verbs.intersection(word_set) )

count = 0
for i in my_paragraph_new_2_list :
    if i.lower() in ref_tobe_verbs :
        count += 1
print( count )


print("*"*80)


### TASK_4
tobe_number_dict = dict()
for i in my_paragraph_new_2_list :
    # print(i)
    if i in ref_tobe_verbs :
        if i not in tobe_number_dict :
            tobe_number_dict[i] = 0
        tobe_number_dict[i] += 1
print( tobe_number_dict )

print("*"*80)

print("\n\n")
##########################################################   3   #######################################################
print("#"*200)

# my_paragraph ="     Here, for the Aston, the (empty) maintenance list was instantiated with the first statement. An element was added to it with the append function , being a dictionary containing the details of that first maintenance event.     "### 35
my_paragraph = " ....I am     Ana.I am from Guatemala.I am 20 years,old.My brother,Pedro is here too. Pedro is 19 years old. We both study English at CCC. We are Spanish.Pedro and I have black hair and black eyes.We are not tall,and we are not thin.We are average in height and weight"
# ### too 18 + eyes 23 + 16 = 57

# Task 1: Count the number of words in the paragraph.
print( "0_MAIN :"+my_paragraph)

for indx,scaner in enumerate( my_paragraph , 0 ) :
    if not ( ( (ord(scaner.lower()) >= 97 and ord(scaner.lower()) <= 122) ) or ( ( ord(scaner.lower()) >= 48 and ord(scaner.lower()) <= 57) ) ) :
        my_paragraph = my_paragraph.replace( scaner , " " )
print( my_paragraph )
my_paragraph_list = my_paragraph.split(" ")
number_of_words = len( my_paragraph_list ) - my_paragraph_list.count("")
print( "There are {0} words in this paragraph".format(number_of_words) )


print("*"*80)


### TASK_2
set_of_words = set()
for indx in my_paragraph_list :
    set_of_words.add ( indx.lower() )
set_of_words.remove("")
print(set_of_words)
print( len( set_of_words ) )


print("*"*80)


### TASK_3
tobe_verbs = {"am" , "is" , "are" ,"was" ,"were"}
print( tobe_verbs.intersection(set_of_words) )
count = 0
for i in my_paragraph_list :
    if i.lower() in  tobe_verbs :
        count += 1
print( count )


print("*"*80)


### TASK_4
tobe_numbers_dict = dict()
for i in my_paragraph_list :
    if i in tobe_verbs :
        if i not in tobe_numbers_dict :
            tobe_numbers_dict[i] = 0
        tobe_numbers_dict[i] += 1
print( tobe_numbers_dict )




