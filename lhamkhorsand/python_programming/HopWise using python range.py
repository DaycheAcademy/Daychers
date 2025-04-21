# Using range operator
for i in range(1000002): print('HopWis' if i  in range(0,10000010, 21) else 'Hop' if i in range(0,10000010, 3) or i in range(0,10000010, 7)else 'Wis' if i in range(0,10000010, 7)else i)

# with range operator and without using if & else
for i in range(110): print("HopWis"*(i in range(0,110,21)) or "Hop"*(i in range(0,110,3)) or "Wis"*(i in range(0,110,7)) or i)