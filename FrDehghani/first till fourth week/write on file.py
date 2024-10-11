with open('binaryFile.txt', 'bw') as fid_bi:
    fid_bi.write(bytes(range(17)))

# معادل باینری 7 دسیمال یا 7 هگز صدا داره در ویندوز

with open('binaryFile.txt', 'br') as fid_bi:
    for i in fid_bi:
        print(i)