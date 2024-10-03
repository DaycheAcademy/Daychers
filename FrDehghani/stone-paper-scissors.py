import random
members = ('stone', 'paper', 'scissors')
mask = (('stone', 'paper'), ('paper', 'scissors'), ('scissors', 'stone'))
myScore = 0
yourScore = 0
for t in range(3):
    for r in range(100):
        you = input('Enter your choice:')
        if you in members:
            break
        else:
            print("invalid choice! Please be careful.")
    me = members[random.randint(0, 2)]
    print(f'my choice is:{me}')
    condition_met = False
    for (j, i) in mask:
        if me == j and you == i:
            yourScore += 1
            condition_met = True
            break
        elif me == i and you == j:
            myScore += 1
            condition_met = True
            break
    if not condition_met:
        print("there are not any winner")
if myScore > yourScore:
    print('hoo ray!**** i am final winner!')
else:
    print(":( you was final winner!")
