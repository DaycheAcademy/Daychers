### ======================================================================================
print( "\n\n================================ EXCERCISE_1_W2 ================================")
### ======================================================================================

print("\n1_FIRST WAY : hopfiz in simplest way","#"*80) #################################

for number in range(1,101):
    if_statement_for = "hopfiz" if number%15==0 else "hope" if not number%3 else "fiz" if number%5==0 else str(number)
    print(if_statement_for)

print("\n2_SECOND WAY","#"*80) #################################

print(["hopfiz" if number%3==0 and number%5==0 else "hope" if not number%3 else "fiz" if number%5==0 else str(number) for number in range(1,101)])


### =========================================================================================
print( "\n\n================================ EXCERCISE_2_W2 ================================")
### =========================================================================================

print("\n1_FIRST WAY","#"*80) #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(-1,-len(str)-1,-1):
    print(str[i])

print("2_SECOND WAY","#"*80) #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print([ str[i] for i in range(-1,-len(str)-1,-1)])

print("3_THIRD WAY","#"*80) #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str[-1:0:-1]+str[0])

print("4_FOURTH WAY","#"*80) #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range (len(str)-1,-1,-1):
    print(str[i])

print("5_FIVTH WAY","#"*80) #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print([str[i] for i in range (len(str)-1,-1,-1)])

print("6_SIXTH WAY","#"*80) #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str[::-1])

### =========================================================================================
print( "\n\n================================ EXCERCISE_3_W2 ================================")
### =========================================================================================


print("\n1_FIEST WAY","#"*80) #################################

SUMM = 0
count = 0
for i in range(1,1001):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2 :
        count = count + 1
        SUMM =SUMM+i
        print(i)
else:
    print (" {0} ta adad aval darim ke sum of them is {1}".format(count,sum))

print("\n 2_SECOND WAY", "#" * 80)  #################################


SUMM = 0
count = 0
for i in range(1,1001):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k>2 :
        print(f"{i} is morakab")

else:
    count = count + 1
    SUMM = SUMM + i
    print (" {0} ta adad aval darim ke sum of them is {1}".format(count,SUMM))

### =========================================================================================
print( "\n\n================================ EXCERCISE_4_W2 ================================")
### =========================================================================================

print("\n 1_FIRST WAY", "#" * 80)  #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_even = str[0:26:2]
str_odd = str[1:26:2]
number_odd = range(1,27,2)
number_even = range(2,27,2)
for odd_char , even_char , odd_num , even_numb  in zip(str_even,str_odd,number_odd,number_even):
    print("{0}_{1} , {2}_{3}".format(odd_num,odd_char,even_numb,even_char))

print("\n 2_SECOND WAY", "#" * 80)  #################################

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for odd_char , even_char , odd_num , even_numb  in zip(str[0:26:2],str[1:26:2],range(1,27,2),range(2,27,2)):
    print("{0}_{1} , {2}_{3}".format(odd_num,odd_char,even_numb,even_char))


### =========================================================================================
print( "\n\n================================ EXCERCISE_5_W2 ================================")
### =========================================================================================

backwards_counter = range(10,-1,-1)
for backwards_index in backwards_counter:
    print(backwards_index)

### =========================================================================================
print( "\n\n================================ EXCERCISE_6_W2 ================================")
### =========================================================================================
#
while True :
    inp = input("Enter an Integer (Positive) : ")
    if inp.isdigit() :       #### float(inp) - int(float(inp))== 0
        print("thats OK")
        break
    else :
        continue

### =========================================================================================
print("\n\n================================ EXCERCISE_7_W2 ================================")
### =========================================================================================

print("\n 1_FIRST WAY", "#" * 80)  #################################

SUMM = 0
count = 0
while True :
    inp = input("Enter an Integer number  : ")
    if  inp.isdigit() :
        count = count + 1
        SUMM = SUMM + int(float(inp))
    elif ((inp.lower() == "q" or inp.lower() == "quit") and  count ==0):
        print("you have entered nothing or what you have entered are not integer numbers")
        break
    elif ((inp.lower() == "q" or inp.lower() == "quit") and count != 0):
        print("The mean of the numbers you have entered is : {0:<5.3f}".format(SUMM / count))
        break
    else :
        print("it is not an integer number, we will eliminate this, keep going.\n")
        continue


print("\n 2_SECOND WAY", "#" * 80)  #################################

SUMM = 0
count = 0
while True :
    inp = input("Enter an Integer number  : ")
    if ( inp != "q" and inp != "quit" and inp.isdigit() ) :
        count = count + 1
        SUMM = SUMM + float(inp)
    if ( inp != "q" and inp != "quit" and not inp.isdigit() ) :
         print("it is not an integer number, we will eliminate this, keep going.\n")
         continue
    if ( (inp == "q" or inp == "quit") and  count ==0 ):
        print( "you have entered nothing or what you have entered are not integer numbers" )
        break
    if ( (inp == "q" or inp == "quit") and count !=0 ):
        print( "The mean of the numbers you have entered is : {0:<5.3f}".format(SUMM/count) )
        break


print("\n 3_THIRD WAY", "#" * 80)  #################################
  ####### try,exception
SUMM = 0
count = 0
while True :
    inp = input("Enter an Integer number  : ")
    if (inp != "q" and inp != "quit"):
        inp_float = float(inp)
        inp_integer = int(inp_float)
        if (inp_float - inp_integer) == 0 :
            count = count + 1
            SUMM = SUMM + int(float(inp))
        else :
            print("it is not an integer number, we will eliminate this, keep going.\n")
            continue
    if ((inp == "q" or inp == "quit") and  count ==0):
        print( "you have entered nothing or what you have entered are not integer numbers" )
        break
    if ((inp == "q" or inp == "quit") and count !=0):
        print( "The mean of the numbers you have entered is : {0:<5.3f}".format(SUMM/count) )
        break




### =========================================================================================
print("\n\n================================ EXCERCISE_8_W2 ================================")
### =========================================================================================


print("\n 1_FIRST WAY", "#" * 80)  #################################



string = "76,876532,9.365,0,-234,6,87586,987,-0.23,14252635352635526,6454737364654,-0.375"
first_level = 0
SUMM=0
cnt=1
print( "We have : ",string )
for indx,scaner in enumerate(string,0) :
    if scaner == "," :
        SUMM = SUMM + float( string[first_level:indx] )
        cnt = cnt + 1   ####################
        first_level = indx+1
    if len(string)==indx+1 :
        SUMM = SUMM + float( string[first_level::])
print( "There are {0} numbers in the string, sum of them is {1} and the mean of them is {2}".format(cnt,SUMM,SUMM/cnt) )


print("\n 2_SECOND WAY", "#" * 80)  #################################


string = "76,876532,9.365,0,-234,6,87586,987,-0.23,14252635352635526,6454737364654,-0.375"
initial_string = ""
SUMM = 0
print( "We have : ",string )
for i in string :
    if i not in "," :
        initial_string = initial_string + i
    elif i in "," :
        SUMM = SUMM + float(initial_string)
        initial_string = ""
print(" sum of numbers is {0}".format( SUMM+float(initial_string) ) )


print("\n 3_THIRD WAY", "#" * 80)  #################################



string = "76,876532,9.365,0,-234,6,87586,987,-0.23,14252635352635526,6454737364654,-0.375"
print( "We have : ",string )
initial_string = ""
SUMM = 0
for i in string :
    if i in "0123456789-." :
        initial_string = initial_string + i
    else:
        SUMM = SUMM + float(initial_string)
        initial_string = ""
print(" sum of numbers is {0}".format( SUMM+float(initial_string) ) )


print("\n 4_FOURTH WAY", "#" * 80)  #################################


string = "76,876532,9.365,0,-234,6,87586,987,-0.23,14252635352635526,6454737364654,-0.375"
print( "We have : ",string )
initial_string = ""
SUMM = 0
if string[-1] != ",":
    string += ","
for i in string :
    if i in "0123456789-." :
        initial_string = initial_string + i
    else:
        SUMM = SUMM + float(initial_string)
        initial_string = ""
print(" sum of numbers is {0}".format(SUMM) )


print("\n 5_FIFTH WAY", "#" * 80)  #################################


string = "76,876532,9.365,0,-234,6,87586,987,-0.23,14252635352635526,6454737364654,-0.375"
print( "We have : ",string )
str_numbs = string.split(",")
count = len(str_numbs)
SUMM=0
for numb in str_numbs :
    SUMM = SUMM + float(numb)
print("There are {0} numbers in the string, sum of them is {1} and the mean of them is {2}".format(count,SUMM,SUMM/count))


print("\n6_SIXTH WAY", "#" * 80)  #################################


my_string = "76,876532,9.365,0,-234,6,87586,987,-0.23,14252635352635526,6454737364654,-0.375"
print( "We have : ",my_string )
print( sum( [float(x) for x in my_string.split(',')] ) )
