
print("="*50)  ################################ FIRST WAY


for i in range(1,101) :
    print( ["hopfiz"  if (i in range(0, 101, 3*5)) else  "fiz"  if (i in range(0, 101, 5)) else "hop" if(i in range(0, 101, 3)) else i] )


print("="*50)  ################################ SECOND WAY


for number in range(1,101) :
    if_statement_for = "hopfiz" if number in range(0, 101, 3*5) else "hope" if number in range(0, 101, 3) else "fiz" if number in range(0, 101, 5) else str(number)
    print(if_statement_for)


print("="*50)  ################################ THIRD WAY


for number in range(1,101) :
    if number % 15 == 0 :
        print("hopfiz")
    elif number % 5 == 0 :
        print("fiz")
    elif number % 3 == 0 :
        print("hop")
    else :
        print(number)



print("="*50)  ################################ FOURTH WAY


print(["hopfiz" if number%3==0 and number%5==0 else "hope" if not number%3 else "fiz" if number%5==0 else str(number) for number in range(1,101)])


