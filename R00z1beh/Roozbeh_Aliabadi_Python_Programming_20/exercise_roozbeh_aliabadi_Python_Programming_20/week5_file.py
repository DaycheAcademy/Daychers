with open ("sample.csv","r") as csv_file :
    line_s = csv_file.readlines()
    print(line_s)

name = []
family = []
email = []
code = []

for item in line_s :
    # print(item.strip("\n").split(";")[0])
    if item != "\n" :
        email.append(item.strip("\n").split(";")[0])
        code.append(item.strip("\n").split(";")[1])
        name.append(item.strip("\n").split(";")[2])
        family.append(item.strip("\n").split(";")[3])

print(name,"\n")
print(family,"\n")
print(code,"\n")
print(email)



######################################################################################################################################################




### sample.csv


# laura@example.com;2070;Laura;Grey
# craig@example.com;4081;Craig;Johnson
# mary@example.com;9346;Mary;Jenkins
# jamie@example.com;5079;Jamie;Smith