
def decimal_generator(start, end, step):
    pre=start
    while pre < end:
        yield pre
        pre += step


for number in decimal_generator(2.3, 3.78, 0.01):
    print(number)