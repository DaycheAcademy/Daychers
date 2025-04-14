

# ####################################################  EXE_1 (Factorial)


def fctrl(n) :
    a,b = 1,1
    for i in range(1,n+1) :
        a = a*i
    print(a)


fctrl(7)





print("#"*100)##########################################  EXE_2  ( new_range_float by generators )





def new_range_float(start,end,step) :
    if (start < end and step <= end-start) :
        x = (end-start)/step
        for i in range(0,int(x)+1) :
            # print(i)
            # yield start + (step * i)
            yield round( start+(step * i) , ndigits=2)
    elif( start >= end or step > end-start) :
        print("ERROR")


for i in new_range_float( 2.3 , 3.78 , 0.01 ) :
    print(i)





print("#"*100)##########################################  EXE_3 (range_alphabet by generators)





def range_alphabet (start , end , step) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ind, i in enumerate(alphabet, start=1):
        if i == start:
            ind_start = ind
        if i == end:
            ind_end = ind
    if (ind_start < ind_end and step <= ind_end - ind_start):
        alphabet_limited = alphabet[ind_start-1:ind_end-1:step]
        for i in alphabet_limited :
            yield i
    else :
        print("ERROR")


for i in range_alphabet("c","f",2) :
    print(i)













