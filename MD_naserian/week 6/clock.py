import turtle
import time
import datetime
import pytz


screen = turtle.Screen()
screen.setup(height=400, width=600)
now = datetime.datetime.now()
t = turtle.Turtle()

watch_on = True
while watch_on:

    #Moscow time

    time1 = datetime.datetime.now()
    hour = time1.hour
    min = time1.minute
    sec = int(time1.second)
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(-200,-50)
    turtle.clear()
    turtle.speed(0)
   
    #tehran time:

    now_utc = datetime.datetime.now(pytz.utc)
    tehran_time = now_utc.astimezone(pytz.timezone("Asia/Tehran"))
    hour_t = tehran_time.hour
    min_t = tehran_time.minute
    sec_t = tehran_time.second

   
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.goto(-200, 50)
    t.clear()
    

    if sec < 10:
        t.write(f"Tehran Time {hour_t}:{min_t}:0{sec_t} ",align="left", font=("Arial", 27, "bold"))
        turtle.write(f"Moscow Time {hour}:{min}:0{sec} ",align="left", font=("Arial", 25, "bold"))
    else:
        turtle.write(f"Moscow Time  {hour}:{min}:{sec} ",align="left", font=("Arial", 25, "bold"))
        t.write(f"Tehran Time {hour_t}:{min_t}:{sec_t} ",align="left", font=("Arial", 27, "bold"))
        
    
    time.sleep(1)
    



turtle.mainloop()

