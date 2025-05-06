def facto_alt(n):
    pre , curr= 1 , 1
    if n==0:
        return 1
    else:
        for _  in range(n):
            pre, curr= pre*curr, curr+1
        return pre
print(facto_alt(1))
