def factorial(n=0):
    pre=1
    for i in range(1, n+1):
        pre = i * pre
    print(pre)


factorial()