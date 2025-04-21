# for i in range(1, 101):
#     if i % 5 == 0 and i % 3==0:
#         print("Hop-Wiz")
#     elif not i % 3 :
#         print("Hop")
#     elif not i % 5:
#         print("Wiz")
#     else:
#         print(i)


for i in range(1, 101):
    answer = "Hop-Wiz" if (not (i % 3) and not (i % 5)) else "Hop" if not (i % 3) else "Wiz" if not (i % 5) else i
    print(answer)



