import shelve
names = ['faide', 'ava', 'mira', 'deniz', 'paniz']
ages = [40, 4, 18, 30, 25]
cities = ['Tehran', 'shiraz', 'esfahan', 'kerman', 'zanjan']
# with shelve.open('myFriends', writeback=True) as shelve_file:
with (shelve.open('myFriends') as shelve_file):
    shelve_file['names'] = names
    shelve_file['ages'] = ages
    shelve_file['cities'] = cities
    print(shelve_file['cities'])
    # print(shelve_file)
    # print(type(shelve_file))
    # shelve_file['names'].append('shalile')
    tempList = shelve_file['names']
    tempList.append('shalile')
    shelve_file['names'] = tempList



    print('\n', '\n', '\n', '\n','*'*40)
    for item in shelve_file:
        print(item, '\t', shelve_file[item])

# ==============================================================
print('\n', '\n', '\n', '\n', "+"*40)
sampleDic = {'name': ['faide', 'ava', 'mira', 'deniz', 'paniz'],' age': [40, 4, 18, 30, 25] , 'cities': ['Tehran', 'shiraz', 'esfahan', 'kerman', 'zanjan']}
for i in sampleDic:
     print( i , ':', sampleDic[i])
