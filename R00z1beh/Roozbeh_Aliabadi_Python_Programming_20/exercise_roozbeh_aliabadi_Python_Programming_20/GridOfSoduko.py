

###########################################  FIRST WAY  ############################################


# import turtle
# import time
#
# # m * m ..... 9 * 9
# # n * n ..... 3 * 3
# # k * k ..... 1 * 1
# # each cell = 33 pixels
#
# m = 9
# n = 3
# pix = 33
#
# dis_horizental = 0
#
# turtle.hideturtle()
#
#
# # ‘fastest’ :  0
# # ‘fast’    :  10
# # ‘normal’  :  6
# # ‘slow’    :  3
# # ‘slowest’ :  1
# turtle.speed( 0 )
# turtle.tracer(7)
#
#
#
# for _ in range( m ) :
#     dis_horizental = dis_horizental +  pix
#     turtle.forward(dis_horizental)
#     turtle.right(90)
#     turtle.forward(m*pix)
#     turtle.right(90)
#     turtle.forward(dis_horizental)
#     turtle.right(90)
#     turtle.forward(m*pix)
#     turtle.right(90)
#
# for i in range( m ) :
#     if i%2 == 0 :
#         turtle.forward(m*pix)
#         turtle.right(90)
#         turtle.forward(pix)
#         turtle.right(90)
#     if i%2 != 0 :
#         turtle.forward(m*pix)
#         turtle.left(90)
#         turtle.forward(pix)
#         turtle.left(90)
#
# turtle.pensize(3)
#
# for i in range( n ) :
#     if i%2 == 0 :
#         turtle.forward(n*pix)
#         turtle.right(90)
#         turtle.forward(m*pix)
#         turtle.left(90)
#     if i%2 != 0 :
#         turtle.forward(n*pix)
#         turtle.left(90)
#         turtle.forward(m*pix)
#         turtle.right(90)
#
# for i in range(n-1):
#     if i % 2 == 0:
#         turtle.left(90)
#         turtle.forward(n*pix)
#         turtle.left(90)
#         turtle.forward(m*pix)
#         turtle.right(90)
#     if i % 2 != 0:
#         turtle.forward(n*pix)
#         turtle.right(90)
#         turtle.forward(m*pix)
#         turtle.left(90)
#         turtle.forward(n*pix)
#
#
# turtle.pensize(5)
#
# for i in range(4) :
#     turtle.left(90)
#     turtle.forward(m*pix)
#
#
#
# time.sleep(1)
# turtle.done()



###########################################  SECOND WAY  ############################################


# import turtle
# import time
#
# # m * m ..... 9 * 9
# # n * n ..... 3 * 3
# # k * k ..... 1 * 1
# # each cell = 33 pixels
#
# m = 9
# n = 3
# pix = 33
#
#
# dis_horizental = 0
#
# turtle.hideturtle()
#
#
# # ‘fastest’ :  0
# # ‘fast’    :  10
# # ‘normal’  :  6
# # ‘slow’    :  3
# # ‘slowest’ :  1
# turtle.speed( 0 )
#
# turtle.tracer(0)
#
#
# flag_m1 = 0
# flag_m2 = 0
# flag_n1 = 0
# flag_n2 = 0
# flag_k = 0
# count = 0
#
# while (True) :
#
#     if flag_m1 == 0 :
#         turtle.setx(dis_horizental)
#         turtle.sety(0)
#         dis_horizental += pix
#         turtle.forward(pix)
#         turtle.right(90)
#         turtle.forward(m * pix)
#         turtle.right(90)
#         turtle.forward(pix)
#         turtle.right(90)
#         turtle.forward(m * pix)
#         turtle.right(90)
#         count += 1
#         if count == m :
#             flag_m1 = 1
#             count = 1
#             dis_horizental = 0
#             turtle.setx(0)
#             turtle.sety(0)
#
#
#
#     if flag_m1 != 0 and flag_m2 == 0 :
#         turtle.sety( -1 * pix * count )
#         turtle.setx( m * pix )
#         turtle.sety( -1 * pix * count )
#         turtle.setx(0)
#         count += 1
#         if count == m :
#             flag_m2 = 1
#             count = 1
#             dis_horizental = 0
#             turtle.setx(0)
#             turtle.sety(0)
#             turtle.pensize(3)
#
#     if flag_m1 != 0 and flag_m2 != 0 and flag_n1 == 0 :
#         turtle.setx( n * pix * count )
#         turtle.sety( m * pix * (-1 ** count) )
#         turtle.setx(0)
#         turtle.sety(0)
#         count += 1
#         if count > 3 :
#             flag_n1 = 1
#             count = 1
#             dis_horizental = 0
#             turtle.setx(0)
#             turtle.sety(0)
#
#     if flag_m1 != 0 and flag_m2 != 0 and flag_n1 != 0 and flag_n2 == 0:
#         turtle.sety( -1 * count * pix * n )
#         turtle.setx( pix * m )
#         turtle.setx(0)
#         turtle.sety(0)
#         count += 1
#         if count > 2:
#             flag_n2 = 1
#             count = 0
#             dis_horizental = 0
#             turtle.setx(0)
#             turtle.sety(0)
#             turtle.pensize(5)
#
#     if flag_m1 * flag_m2 * flag_n1 * flag_n2 == 1:
#         turtle.forward( m * pix )
#         turtle.right(90)
#         count += 1
#         if count > 3:
#             break
#
#
# time.sleep(1)
# turtle.done()


###########################################  THIRD WAY  ############################################


import turtle
import time


# m * m ..... 9 * 9
# n * n ..... 3 * 3
# k * k ..... 1 * 1
# each cell = 33 pixels

m = 9
n = 3
pix = 35

dis_horizental = 0

turtle.hideturtle()

# ‘fastest’ :  0
# ‘fast’    :  10
# ‘normal’  :  6
# ‘slow’    :  3
# ‘slowest’ :  1
turtle.speed(8)
turtle.tracer(8)


flag_m1 = 0
flag_m2 = 0
flag_n1 = 0
flag_n2 = 0
flag_k = 0
count = 0
count_a = 0
count_b = 1


while (True):

    if flag_m1 == 0:
        turtle.color("purple")    ### violet   Lime   purple
        turtle.setx(dis_horizental)
        turtle.sety(0)
        dis_horizental += pix
        turtle.forward(pix)
        turtle.right(90)
        turtle.forward(m * pix)
        turtle.right(90)
        turtle.forward(pix)
        turtle.right(90)
        turtle.forward(m * pix)
        turtle.right(90)
        count += 1
        if count == m:
            flag_m1 = 1
            count = 1
            dis_horizental = 0
            turtle.setx(0)
            turtle.sety(0)


    if flag_m1 != 0 and flag_m2 == 0:
        turtle.sety(-1 * pix * count)
        turtle.setx(m * pix)
        turtle.sety(-1 * pix * count)
        turtle.setx(0)
        count += 1
        if count == m:
            flag_m2 = 1
            count = 1
            dis_horizental = 0
            turtle.setx(0)
            turtle.sety(0)
            turtle.pensize(3)


    if flag_m1 != 0 and flag_m2 != 0 and flag_n1 == 0 :
        turtle.color("orange")
        count_a += 1
        turtle.setpos( 0 , -1 * count_b * n * pix )
        turtle.pendown()
        turtle.forward(count_a * n * pix)
        turtle.left(90)
        turtle.forward(n * pix)
        turtle.right(90)
        turtle.penup()


        if count_a == 3  and count_b < 3 :
            count_b += 1
            count_a = 0
        if count_a == 3  and count_b == 3 :
            flag_n1 = 1
            turtle.setpos(0, 0)
            turtle.pendown()
            turtle.pensize(5)
            count = 0


    if flag_m1 * flag_m2 * flag_n1  == 1 :
        turtle.color("silver")     ### Lime   Cyan  Lime  yellow
        turtle.forward(m * pix)
        turtle.right(90)
        count += 1
        if count > 4:
            turtle.setpos(0,0)
            break




time.sleep(1)
turtle.done()