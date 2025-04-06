import time, turtle


write_date = turtle.Turtle()
write_date.hideturtle()
write_sec = turtle.Turtle()
write_sec.hideturtle()
write_min = turtle.Turtle()
write_min.hideturtle()
write_hour = turtle.Turtle()
write_hour.hideturtle()


now = time.localtime()
date = f'{now.tm_year} / {now.tm_mon} / {now.tm_mday}'
write_date.teleport(write_date.pos()[0] - 20, write_date.pos()[1] -50)
write_date.write(date, font=('Arial', 15, 'bold'))


write_hour.teleport(write_hour.pos()[1] - 100)
write_min.teleport(write_min.pos()[1])
write_sec.teleport(write_min.pos()[1]  + 100)


while(True):
    write_sec.clear()
    write_hour.write(time.strftime('%H:'), font=('Arial', 50, 'bold'))
    write_min.write(time.strftime('%M:'), font=('Arial', 50, 'bold'))
    write_sec.write(time.strftime('%S'), font=('Arial', 50, 'bold'))

    if time.strftime('%S') == '00':
        write_min.clear()
        write_min.write(time.strftime('%M:'), font=('Arial', 50, 'bold'))

    if time.strftime('%M') == '00':
        write_hour.clear()
        write_sec.write(time.strftime('%S'), font=('Arial', 50, 'bold'))

    # print(time.strftime('%H : %M : %S'))

    time.sleep(1 - time.time()%1)

