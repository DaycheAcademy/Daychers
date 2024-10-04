import matplotlib.pyplot as plt
import json

import shelves

with open('D:\\Dayche\\4-python\\recorse\\FBI_CrimeData_2016.json', 'r') as jsonFile:
    data = json.load(jsonFile)

regions = [item['Region'] for item in data]  # the horizontal axis values
# murder_counts = [item['Murder'] for item in data]  # the vertical axis values
# plt.bar(regions, murder_counts , color='b')  # define the barchart
# plt.xlabel('Regions')
# plt.ylabel('Number of Murders')
# plt.title('Number of Murders by Region')
# plt.yticks(list(range(0, int(max(murder_counts)) + 10, 10)))  # Set ticks at intervals of 10 for y_axis
# plt.tight_layout()
# plt.show()
# #
# print('\n', '\n', '\n', '*' * 50)
# =================================================================================================
# second question

for item in data:  # define two columns for data by sum of violent and not-violent crimes
    Violent_count = 0
    NonViolent_count = 0
    for key in {'Murder', 'Rape', 'Robbery', 'Assault'}:
        Violent_count += int(item[key])
    for key in {'Burglary', 'Theft', 'Vehicle_Theft'}:
        NonViolent_count += int(item[key])
    item['Violent'] = Violent_count
    item['NonViolent'] = NonViolent_count

Violent_counts = [item['Violent'] for item in data]  # create list of values that should make barchart
NonViolent_counts = [item['NonViolent'] for item in data]
# print(max(Violent_counts))
# print(max(NonViolent_counts))
# plt.bar(regions, Violent_counts, color='g')  # define the barchart  # my chart!
# plt.xlabel('Regions')
# plt.ylabel('Number of Violent crimes')
# plt.title('Number of Violent crimes by Region')
# plt.yticks(list(range(0, int(max(Violent_counts)) + 5000, 5000)))  # Set ticks at intervals of 10 for y_axis
# plt.tight_layout()
# plt.show()

# =================================================================================================
# 3th question
# plt.bar(regions, NonViolent_counts, color='y')  # define the barchart  # my chart!
# plt.xlabel('Regions')
# plt.ylabel('Number of NonViolent crimes')
# plt.title('Number of Non_Violent crimes by Region')
# plt.yticks(list(range(0, int(max(NonViolent_counts)) + 10000, 10000)))  # Set ticks at intervals of 10 for y_axis
# plt.tight_layout()
# plt.show()

# ==================================================================================================
# 4th question

import numpy as np

mean_national_violent = round(np.mean(Violent_counts), 2)
print(mean_national_violent)
report_file = []
for item in data:  # add new item to each dictionary
    item['DifferenceOfMean'] = round(mean_national_violent - item['Violent'] , 2)
    report_file.append(item['Region'])
    report_file.append(item['DifferenceOfMean'])
# print(report_file)
with open('report_file.json', 'w') as FBI_report:
    print(FBI_report, report_file)
#         print(FBI_report['DifferenceOfMean'])
#     json.dump(data, FBI_report, indent=4)  # Write with pretty-printing













