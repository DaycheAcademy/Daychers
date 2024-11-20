import random
playList=['stone', 'paper' ,'scissors','s','p','sc']
validPlayList=['stone', 'paper' ,'scissors','s','p','sc']
sumComp=0
sumOfMe=0


flag=True
inputValue= input("Pleas Type in a Value For the Winning Score : ")
while not inputValue.isdigit():
    inputValue = input("I need an integer value to carry on. Pleas inter an integer value :")

while  int(inputValue)>=1:
    selectValue= input("Pleas Select either 'stone', 'paper' or 'scissors' (or q for exit): ").split(" ")
    if selectValue=='q':
        print("Thank You For Playing")
        break
    if not any(sub in validPlayList for sub in selectValue):
        print("{} Is not a Valid Choice".format(selectValue))
        print("-" * 50)
    else:
        comchoice=random.choice(playList)
        if any(sub in comchoice for sub in ['scissors','sc']) and any(sub in selectValue for sub in ['paper','p']):
        # if comchoice=='scissors' and selectValue=='paper':
            sumComp+=1
        if any(sub in comchoice for sub in ['paper', 'p']) and any(sub in selectValue for sub in ['stone', 's']):
        # if comchoice=='paper' and selectValue=='stone':
            sumComp += 1
        if any(sub in comchoice for sub in ['stone', 's']) and any(sub in selectValue for sub in ['scissors', 'sc']):
        # if comchoice=='stone' and selectValue=='scissors':
            sumComp += 1
        if any(sub in selectValue for sub in ['scissors', 'sc']) and any(sub in comchoice for sub in ['paper', 'p']):
        # if selectValue=='scissors' and comchoice=='paper':
            sumOfMe+=1
        if any(sub in selectValue for sub in ['paper', 'p']) and any(sub in comchoice for sub in ['stone', 's']):
        # if selectValue=='paper' and comchoice=='stone':
            sumOfMe += 1
        if any(sub in selectValue for sub in ['stone', 's']) and any(sub in comchoice for sub in ['scissors', 'sc']):
        # if selectValue=='stone' and comchoice=='scissors':
            sumOfMe += 1
        # if any(sub in selectValue for sub in ['paper', 'p']) and any(sub in comchoice for sub in ['stone', 's']):
        if selectValue==comchoice:
            (inputValue)=int(inputValue)+1
        print("*" * 50)
        print("CopmSelected  : ", comchoice)

        print("Your Score : ",sumOfMe)
        print("Comp Score : ",sumComp)
        (inputValue) = int(inputValue) - 1
print("=" * 50)
if sumComp <= sumOfMe and selectValue != 'q':
    print("You Win")
if sumComp > sumOfMe and selectValue != 'q':
    print("You Lose")














    # flag = False







