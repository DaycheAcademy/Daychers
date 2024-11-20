def floatRange():
    firstNum=2.6
    while firstNum<=2.8:
        yield round(firstNum,2)
        firstNum+=0.01


if __name__ == '__main__':
    for _ in floatRange():
        print(_)
