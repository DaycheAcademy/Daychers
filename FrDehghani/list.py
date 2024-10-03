fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(f'list of fruits is:{fruits}')
print(fruits.append('cherry'))
print(fruits.index('cherry'))
print(fruits.pop(5))
print(len(fruits))
print(fruits.copy())
# fruits3 = fruits.extend(['Pomegranate', 'grape'])
# print(f'a:{fruits}')
print("-"*10)
print(fruits.extend(['Pomegranate', 'grape']))

fruits2 = fruits.insert(5,'apple')
print(f'b:{fruits}')
print("-"*20)
d = list([1,2,5,3.7,8.2])

print(f'd:{d}')