def odds():
    num=1
    while True:
        yield num
        num += 2


def pi_1(n):
    seri = 0
    odd=odds()
    for i in range(n//2):
        seri += 4/next(odd)
        yield seri
        seri -= 4/next(odd)
        yield seri

def star():
    a = 2
    while True:
        b= a+1
        c= a+2
        a *= b
        a *= c
        yield a
        a=c



def pi_2():
    seri=3
    num=2
    Generator=star()
    for i in range(100):
        seri += 4 /next(Generator)
        yield seri
        seri -= 4 /next(Generator)
        yield seri



if __name__ == "__main__":
    for item in pi_1(100):
        print(item)

    print('='*50)

    for item in pi_2():
        print(item)




