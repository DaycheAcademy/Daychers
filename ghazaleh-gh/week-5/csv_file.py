email, userId, password, firstName, lastName, department = ([] for i in range(6))
lists = [email, userId, password, firstName, lastName, department]
with open('csvfile.csv') as csvFile:
    row = csvFile.readline().strip('\n')
    row = csvFile.readline().strip('\n')

    while row:
        cell_list = row.split(',')
        print(cell_list)

        # email.append(cell_list[0])
        # userId.append(cell_list[1])
        # password.append(cell_list[2])
        # firstName.append(cell_list[3])
        # lastName.append(cell_list[4])
        # department.append(cell_list[5])

        for _list, item in zip(lists, cell_list):
            _list.append(item)

        row = csvFile.readline().strip('\n')

print("-"*200)
print(f'email: {email}\nuser-id: {userId}\npassword: {password}\nfirst-name: {firstName}\nlast-name: {lastName}\ndepartment: {department}')