def alphabitRange():
    alphaList=['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x']
    for a in alphaList:
        yield a


if __name__=='__main__':
    for i in alphabitRange():
        print(i)
