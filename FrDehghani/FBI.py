import matplotlib.pyplot as plt
import json

with open('D:\\Dayche\\4-python\\recorse\\FBI_CrimeData_2016.json', 'r') as jsonFile:
    data = json.load(jsonFile)

regions = [item['Region'] for item in data]  # the horizontal axis values
murder_counts = [item['Murder'] for item in data]  # the vertical axis values

plt.bar(regions, murder_counts)  # define the barchart
plt.xlabel('Regions')
plt.ylabel('Number of Murders')
plt.title('Number of Murders by Region')
plt.yticks(list(range(0, int(max(murder_counts)) + 10, 10)))  # Set ticks at intervals of 10 for y_axis
plt.tight_layout()
plt.show()
