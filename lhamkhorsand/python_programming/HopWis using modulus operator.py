#
# # for i in range(100): print('HopWis') if i % 3 == 0 and i % 7 == 0 else print('Hop') if i % 3 == 0 or i % 7 == 0 else print( )
#
# Using modulus operator
for i in range(1000001): print('HopWis' if i % 3 == 0 and i % 7 == 0  else 'Hop' if i%3==0 else 'Wis' if i%7==0 else i)

# with modulus operator and without using if & else
for i in range(110): print('HopWis' *(i % 21==0)  or 'Hop' *(i%3==0) or 'Wis' * (i%7==0) or i)



