def Factorail(num):
    totalamount =1
    if num == 0:
        return 0
    else:
     while num>0:

            totalamount*=num
            num-=1
    return totalamount



if __name__ == "__main__":
    flag=True
    while flag:
        number = int(input("Pleade Insert Number For Calculate Factorial : "))
        if type(number==int):

            print(Factorail(number))
        else: flag=False