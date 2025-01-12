
name=[]
age=[]
gender=[]
state=[]
salary=[]
with open ('sample_data.csv') as csv_file:
    # text=csv_file.read()
    # print(text)
    line= csv_file.readline()
    for line in csv_file:
        words=line.split(',')
        name.append(words[1])
        age.append(words[2])
        gender.append(words[3])
        state.append(words[4])
        salary.append(words[5].strip('\n'))
print('='*50)
print(f"name_list:{name}")
print(f"age_list:{age}")
print(f"gender_list:{gender}")
print(f"state_list:{state}")
print(f"salary_list:{salary}")

