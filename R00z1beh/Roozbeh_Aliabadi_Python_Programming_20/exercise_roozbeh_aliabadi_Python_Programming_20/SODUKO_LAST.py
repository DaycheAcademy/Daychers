#############################################  WEEK6 _ making Soduko solved   #############################################

import time
start = time.time()




import random



intrfc_list = list()
two_dim_list_local = list()
ref = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 }
m = 9
n = 3
get_out_1 = 0
get_out_2 = 0
exception_set_row = set()
exception_set_col = set()
exception_set_sqr = set()
union_sqr_row_col = set()

list_number_in_row = list()
list_number_in_column = list()
list_number_in_square = list()

set_number_in_row = set()
set_number_in_column = set()
set_number_in_square = set()





def making_two_dim_list () :
    for i in range( 0 , m ) :
        List = list()
        for j in range( 0 , m ) :
            List.append( 0 )
        two_dim_list_local.append( List )
    return two_dim_list_local






def square_points_maker ( LengthPoint , WidthPoint ) :
    L = []
    W = []
    if (LengthPoint % 3 == 0) :
        L = list ( range ( LengthPoint , LengthPoint + 3 ) )
    if (LengthPoint % 3 == 1) :
        L = list ( range ( LengthPoint - 1 , LengthPoint + 2 ) )
    if (LengthPoint % 3 == 2) :
        L = list ( range ( LengthPoint - 2 , LengthPoint + 1 ) )
    if (WidthPoint % 3 == 0):
        W = list( range ( WidthPoint , WidthPoint + 3 ) )
    if (WidthPoint % 3 == 1):
        W = list( range ( WidthPoint - 1 , WidthPoint + 2 ) )
    if (WidthPoint % 3 == 2):
        W = list( range ( WidthPoint - 2 , WidthPoint + 1 ) )
    return L , W



def storing_square ( LIST_in , LengthPoint , WidthPoint ) :
    lst_sqr = []
    L , W = square_points_maker( LengthPoint , WidthPoint )
    for i in L :
        for j in W :
            lst_sqr.append( LIST_in[i][j] )
    return lst_sqr






def storing_column ( LIST_in , col ) :
    lst_row = []
    for i in range( 0 , m) :
        lst_row.append(LIST_in[i][col])
    return lst_row
    # return exception_set_col



def storing_row ( LIST_in , row ) :
    lst_col = []
    for j in range( 0 , m) :
        lst_col.append(LIST_in[row][j])
    return lst_col




def show ( LIST ) :
    for i in range( 0 , m ) :
        print(LIST[i],'\n')




def row_checker ( List_in , row_number , numb ) :
    for j in range (0,m) :
        if List_in[row_number][j] == numb :
            return -1
    return 1


def column_checker ( List_in , column_number , numb ) :
    for i in range (0,m) :
        if List_in[i][column_number] == numb :
            return -1
    return 1


def square_checker ( List_in , row_number , column_number , numb ) :
    L, W = square_points_maker(row_number, column_number )
    for i in L :
        for j in W :
            if List_in[i][j] == numb :
                return -1
    return 1


def row_zero_checker(LIST_in, row):
    count = 0
    for j in range(0, m):
        if LIST_in[row][j] == 0:
            count += 1
    return count


def zero_checker(LIST_in):
    count = 0
    for i in range(0, m):
        for j in range(0, m):
            if LIST_in[i][j] == 0:
                count += 1
    if count != 0:
        return -1
    if count == 0:
        return 1




# *************************************************************************************************************



x=0
two_dim_list = making_two_dim_list()
i = 0
j = -1
empty_list_numbers = 0
r_c = set_number_in_row.union(set_number_in_column)
r_c_s = r_c.union(set_number_in_square)
active_modify_1 = 0
active_modify_no_1 = 0

while(get_out_1 == 0) :

    if active_modify_1 == 1 :
        j = -2
        i = 0
        active_modify_1 = 0

    if active_modify_no_1 == 1 :
        j = 6   ### 7
        active_modify_no_1 = 0


    j+=1
    if j > 8 :
        i+=1
        j=0


    if list(ref.difference(r_c_s)) != [] :
        x = random.choice( list(ref.difference(r_c_s)) )
        if row_checker(two_dim_list, i, x) == 1 and column_checker(two_dim_list, j, x) == 1 and square_checker(two_dim_list,i, j,x) == 1 :
            two_dim_list[i][j] = x



    list_number_in_row = storing_row(two_dim_list, i)

    if j != 8:
        list_number_in_column = storing_column(two_dim_list, j + 1)
    if j == 8:
        list_number_in_column = storing_column(two_dim_list, 0)
        list_number_in_row = list()

    list_number_in_square = storing_square(two_dim_list, i, j)

    set_number_in_row = set(list_number_in_row)
    set_number_in_column = set(list_number_in_column)
    set_number_in_square = set(list_number_in_square)

    if (j == 0 or j == 2 or j == 5):
        list_number_in_square = storing_square(two_dim_list, i, j + 1)
        set_number_in_square = set(list_number_in_square)

    if j == 8 and i != 8:
        list_number_in_square = storing_square(two_dim_list, i + 1, 0)
        set_number_in_square = set(list_number_in_square)
    if j == 8 and i == 8:
        list_number_in_square = storing_square(two_dim_list, i, 0)
        set_number_in_square = set(list_number_in_square)

    if (i == 2 and j == 8 ) or (i == 5 and j == 8) :
        set_number_in_square = set()


    ### NEW
    # if j == 8 :
    #     if zero_checker_per_row(i,two_dim_list) == -1 :
    #         two_dim_list[i] = [0,0,0,0,0,0,0,0,0]
    #         i -= 1
    ### NEW


    r_c = set_number_in_row.union(set_number_in_column)
    r_c_s = r_c.union(set_number_in_square)
    print("now === >    ", "row : ", i, ", column : ", j , "\n")
    show(two_dim_list)
    print( "set_number_in_row  for next step : ",set_number_in_row )
    print( "set_number_in_column  for next step : ",set_number_in_column)
    print( "set_number_in_square  for next step : ", set_number_in_square )
    print( "these numbers are allowed  for next step : ",list(ref.difference(r_c_s)) )

    if len( list(ref.difference(r_c_s)) ) == 0 and row_zero_checker(two_dim_list,i)>=1 : ### or len( list(ref.difference(r_c_s)) )==0 :
        ### empty_list_numbers += 1
        ### if empty_list_numbers == 2 :

        if i == 1 :
            active_modify_1 = 1
            two_dim_list[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]  ###     i = 1
            i -= 1
            two_dim_list[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]  ###     i = 0


        if i > 1 :
            two_dim_list[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]  ### i = 4
            i -= 1
            two_dim_list[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]  ### i = 3
            i -= 1                                         ### i = 2
            active_modify_no_1 = 1



        print("{0} th row should be filled again ".format(i+2))

        ###****************************************************************
    print("#" * 70)

    if zero_checker( two_dim_list ) == 1 :
        break




finish = time.time()
print(f"It took  {finish - start}  seconds")
print("#" * 70)

# *************************************************************************************************************



print("\nNow , we have :\n")
show(two_dim_list)



################################  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID
################################  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID
################################  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID
################################  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID
################################  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID  GRID



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
        turtle.color("Lime")     ### Lime   Cyan  silver  yellow
        turtle.forward(m * pix)
        turtle.right(90)
        count += 1
        if count > 4:
            turtle.setpos(0,0)
            break


################################  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION
################################  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION
################################  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION
################################  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION
################################  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION  TRANSMISSION


turtle.penup()

x_step = pix/3
y_step = 0
for i in range(m) :
    y_step -= pix

    for j in range(m) :
        # x_step += pix/3
        turtle.setpos( x_step , y_step )
        turtle.color("blue")
        turtle.write( two_dim_list[i][j],font=('arial',15,'bold'))    ### turtle.write('Hello!', font=('arial',50,'bold'), align='center')
        x_step += pix
    x_step = pix / 3
time.sleep(1)
turtle.done()





