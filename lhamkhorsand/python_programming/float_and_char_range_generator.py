def customized_flt_range():
    strt , end = 2.3 , 3.78
    while strt < end:
        yield strt
        strt+= 0.01

for flt in customized_flt_range():
    print(flt)

print('------------------------')


def char_gnrtr():
    strt , end = 'c' , 'x'
    while strt < end :
        yield strt
        strt = chr(ord(strt)+1)


for chrx in char_gnrtr() :
    print(chrx)



