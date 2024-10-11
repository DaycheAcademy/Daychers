fid = open('../projects/sample.txt')
print(fid)  # fid is a file handler it can wrap file for read & write
# ================================
print('='*40)
for line in fid:
    print(line)
fid.close() # end of file handler in first line


# ================================
print('='*40)
with open('../projects/sample.txt') as file_id:    # open and close file by with as context manager
    for line in file_id:
        print(line)

    # line = file_id.readline().strip('\n')  # read just 1 line
    # while line:
    #     print(line)
    #     line = file_id.readline().strip('\n')   # ????????
    for x in file_id:
        line = file_id.readline().strip('\n')
        print(line)

# ================================
    print('*'*40)
    lines = file_id.readlines()  # read all lines in the file return list
    print(lines)

    # txt = file_id.read()      # read character by character and return string
    # print(txt)




