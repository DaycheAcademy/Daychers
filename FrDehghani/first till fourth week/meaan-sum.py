sumofval = 0
cou = 0
while True:
    A = input('inter a number:')
    if not A.isdigit():
        continue
    else:
        sumofval = sumofval+int(A)
        cou = cou + 1
    break

if cou == 0:
    print('there are not any number for calculate mean')
else:
    print(sumofval/cou)
#++++++++++++++++++++++++++++++++++++++++++++++++++++
print("+"*40)
samplestring = '25,56,123564,-25,0.005,846,15'
num = ''
sumofnumeric = 0
for char in samplestring:
    if char in '0123456789.-':
        num += char
    else:
        sumofnumeric += float(num)
        num = ''
print(sumofnumeric+float(num))
#++++++++++++++++++++++++++++++++++++++++++++++++++++
print("+"*40)
# pythonic
print(sum(float(char) for char in samplestring.split(',')))

# print(sum(float(())))
