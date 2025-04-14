#### FIRST WAY


import time
import turtle


turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)


turtle.pensize(5)
turtle.color("violet")
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)




turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

turtle.forward(250)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

# body3 = turtle.Turtle()
turtle.forward(300)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(50)

turtle.hideturtle()
tehranTime = time.localtime()
turtle.penup()

while (True) :
    tehranTime = time.localtime()

    # print("{}-{}-{} \t {}:{}:{}".format(tehranTime.tm_mday, tehranTime.tm_mon, tehranTime.tm_year,
    #                                     tehranTime.tm_hour, tehranTime.tm_min, tehranTime.tm_sec))


    turtle.setpos(33, -35)
    turtle.color("orange")
    turtle.write( "{}-{}-{}".format(tehranTime.tm_mday, tehranTime.tm_mon, tehranTime.tm_year),font = ("Arial", 14, "normal" ) )
    turtle.color("white")
    turtle.setpos(25, -35)



    turtle.setpos(170, -35)
    turtle.color("blue")
    turtle.write("{}".format(tehranTime.tm_hour), font=("Arial", 14, "normal" ))
    if tehranTime.tm_min == 59 and tehranTime.tm_sec == 59 :
        turtle.setpos(165, -35)
        turtle.color("blue")
        turtle.write( "{}".format(tehranTime.tm_hour), font=("Arial", 14, "normal" ) )
        turtle.color("white")
        turtle.setpos(174, -29)
        turtle.dot(40)




    turtle.setpos(220, -35)
    turtle.color("blue")
    turtle.write("{}".format(tehranTime.tm_min), font=("Arial", 14, "normal" ))
    if tehranTime.tm_sec == 59 :
        turtle.setpos(220, -35)
        # turtle.goto((200, -35))
        turtle.color("blue")
        turtle.write("{}".format(tehranTime.tm_min), font=("Arial", 14, "normal" ))
        turtle.color("white")
        # turtle.goto((200, -35))
        turtle.setpos(225, -29)  #######
        turtle.dot(40)    #######




    turtle.setpos(265, -35)
    turtle.color("blue")
    turtle.delay(2)
    turtle.write("{}".format( tehranTime.tm_sec), font=("Arial", 14, "normal" ))
    turtle.color("white")
    turtle.setpos(274, -29)
    turtle.dot(40)    #######
    turtle.write("{}".format( tehranTime.tm_sec), font=("Arial", 14, "normal" ))



################################################################################################################################################################################


#### SECOND WAY


import time
import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)



def body () :
    turtle.pendown()
    turtle.setpos(0,0)
    turtle.pensize(5)
    turtle.color("violet")
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

    turtle.forward(250)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

    # body3 = turtle.Turtle()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.penup()








while (True) :

    tehranTime = time.localtime()
    body()


    # print("{}-{}-{} \t {}:{}:{}".format(tehranTime.tm_mday, tehranTime.tm_mon, tehranTime.tm_year,
    #                                     tehranTime.tm_hour, tehranTime.tm_min, tehranTime.tm_sec))


    turtle.setpos(33, -35)
    turtle.color("orange")
    turtle.write( "{}-{}-{}".format(tehranTime.tm_mday, tehranTime.tm_mon, tehranTime.tm_year),font = ("Arial", 14, "normal" ) )
    turtle.color("white")
    turtle.setpos(25, -35)



    turtle.setpos(170, -35)
    turtle.color("blue")
    turtle.write("{}".format(tehranTime.tm_hour), font=("Arial", 14, "normal" ))
    if tehranTime.tm_min == 59 and tehranTime.tm_sec == 59 :
        turtle.setpos(165, -35)
        turtle.color("blue")
        turtle.write( "{}".format(tehranTime.tm_hour), font=("Arial", 14, "normal" ) )
        turtle.color("white")
        turtle.setpos(174, -29)
        turtle.dot(40)




    turtle.setpos(220, -35)
    turtle.color("blue")
    turtle.write("{}".format(tehranTime.tm_min), font=("Arial", 14, "normal" ))
    if tehranTime.tm_sec == 59 :
        turtle.setpos(220, -35)
        turtle.color("blue")
        turtle.write("{}".format(tehranTime.tm_min), font=("Arial", 14, "normal" ))
        turtle.color("white")
        turtle.setpos(225, -29)  #######
        turtle.dot(40)    #######


    turtle.setpos(265, -35)
    turtle.color("blue")
    # turtle.delay(0)
    turtle.write("{}".format( tehranTime.tm_sec), font=("Arial", 14, "normal" ))
    turtle.color("white")
    turtle.setpos(274, -29)
    # turtle.dot(40)    #######
    turtle.write("{}".format( tehranTime.tm_sec), font=("Arial", 14, "normal" ))


    time.sleep(1)
    turtle.clear()
    # turtle.update()  ####



