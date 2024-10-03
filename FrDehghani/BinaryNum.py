with open('BinaryNum.txt', 'bw') as biFile:
    biFile.write(bytes(range(17)))

with open('BinaryNum.txt', 'br') as biFile:
    print(biFile.read())

# with open('test.txt', 'bw') as testFile:
#     a = bytes(7)
#     testFile.write(a)
# with open('test.txt', 'br') as testFile:
#     # a = hex(8)
#     print(testFile.read())
