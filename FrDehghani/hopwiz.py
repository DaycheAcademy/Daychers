# for i in range(100):
#    if i % 21==0:
#        print('hopwiz')
#    else:
#         if i % 7==0:
#             print('wiz')
#         else:
#             if i % 3==0:
#                 print('hop')
#             else:
#                 print(f'{i}')
# =================================================================
print(not 1)
print("--"*100)
# @Dr.Shokri
for i in range(100):
    ply = 'hopwiz' if not i % 21 else 'hop' if not i % 3 else 'wiz' if not i % 7 else str(i)
    print(ply)

# =================================================================
print("--"*100)
# pythonic
for i in range(100):
    if i in range(0, 100, 21):
        print('hopwiz')
    else:
        if i in range(0, 100, 7):
            print('wiz')
        else:
            if i in range(0, 100, 3):
                print('hop')
            else:
                print(f'{i}')
# =================================================================
print("--"*100)
# @Dr.Shokri  + pythonic
for i in range(100):
    print('hopwiz' if i in range(0, 100, 21) else 'hop' if i in range(0, 100, 3) else 'wiz' if i in range(0, 100, 7)
          else str(i))
