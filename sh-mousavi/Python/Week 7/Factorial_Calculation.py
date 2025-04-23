
def factorial1(n):
    fac_cal = 1
    for num in range(n):
        fac_cal *= (num+1)
    return fac_cal

def factorial2(n):
    previous, current = 1, 1
    for _ in range(n):
        yield current
        previous, current = current, previous * (current+1)



if __name__ == '__main__':
    print(factorial1(5))

    print('=' * 50)
    for num in factorial2(5):
        print(num)
