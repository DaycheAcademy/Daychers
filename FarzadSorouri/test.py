import pandas as pd
import matplotlib.pyplot as plt
#from ydata_profiling import ProfileReport
df = pd.read_json('FBI_CrimeData_2016.json')
print (df)

print('_' * 40)
# profile = ProfileReport(df, title='FBI Crime Data 2016', explorative=True)
# profile.to_file('FBI_CrimeData_2016.html')

# aggregation on region to find distribution of murders in each region

murdrer_fre_by_regions = df.groupby('Region')['Murder'].sum().reset_index()
print('murder frequency according to each region \n' , murdrer_fre_by_regions)

print('_' * 40)

# aggregation on region to find distribution of total violent crime in each region

violent_crime_by_regions = df.groupby('Region')[['Assault', 'Murder', 'Robbery', 'Rape']].sum().reset_index()
violent_crime_by_regions['Total_Violent_Crime'] = violent_crime_by_regions[['Assault', 'Murder', 'Robbery', 'Rape']].sum(axis=1)
print('total violent crime by regions \n' , violent_crime_by_regions)

print('_' * 40)

# aggregation on states to find distribution of total violent crime in each state

violent_crime_by_states = df.groupby('State')[['Assault', 'Murder', 'Robbery', 'Rape']].sum().reset_index()
violent_crime_by_states['Total_Violent_Crime'] = violent_crime_by_states[['Assault', 'Murder', 'Robbery', 'Rape']].sum(axis=1)


# aggregation on region to find distribution of total nonviolent crime in each region

nonviolent_crime_by_regions = df.groupby('Region')[['Burglary', 'Theft' , 'Vehicle_Theft']].sum().reset_index()
nonviolent_crime_by_regions['Total_Nonviolent_Crime'] = nonviolent_crime_by_regions[['Burglary', 'Theft', 'Vehicle_Theft']].sum(axis=1)
print('total nonviolent crime frequency by regions \n ' , nonviolent_crime_by_regions)

print('_' * 40)

# Bar chart for each region and murder frequency
plt.figure(figsize=(10,6))
plt.bar(murdrer_fre_by_regions['Region'], murdrer_fre_by_regions['Murder'])
plt.title('Murder Rate by Region')
plt.xlabel('Region')
plt.ylabel('Murder Rate')
plt.show()

# Bar chart for each region and total violent crime frequency
plt.figure(figsize=(10,6))
plt.bar(violent_crime_by_regions['Region'], violent_crime_by_regions['Total_Violent_Crime'])
plt.title('Total Violent Crime Rate by Region')
plt.xlabel('Region')
plt.ylabel('Total Violent Crime Rate')
plt.show()

# Bar chart for each region and total nonviolent crime frequency
plt.figure(figsize=(10,6))
plt.bar(nonviolent_crime_by_regions['Region'], nonviolent_crime_by_regions['Total_Nonviolent_Crime'])
plt.title('Total Nonviolent Crime Rate by Region')
plt.xlabel('Region')
plt.ylabel('Total Nonviolent Crime Rate')
plt.show()

mean_violent_crime = violent_crime_by_regions['Total_Violent_Crime'].sum()/ len(violent_crime_by_states['State'])
print('mean violent crime is : ',mean_violent_crime)

print ('_' * 40)

violent_crime_by_states['distance from mean'] = violent_crime_by_states['Total_Violent_Crime'] - mean_violent_crime
violent_crime_by_states = violent_crime_by_states.drop(['Assault', 'Murder', 'Robbery', 'Rape'], axis = 1)
print('total violent crime by States \n' , violent_crime_by_states)
#================================================================

# # write the code to iterate in dictionary
# import json
#
# # Load JSON file into a list (assuming the file is named 'crime_data.json')
# with open('FBI_CrimeData_2016.json') as f:
#     crime_list = json.load(f)
#
# # Initialize regular dictionaries to store aggregated data by region
# murder_by_region = {}
# violent_by_region = {}
# nonviolent_by_region = {}
# violent_by_state = {}
# states = []
# # Iterate over the crime_list to populate the dictionaries
# for crime in crime_list:
#     region = crime['Region']
#     state = crime['State']
#     if crime['State'] not in states:
#         states.append(crime['State'])
#
#
#     # Initialize the region if it's not already in the dictionary
#     if region not in murder_by_region:
#         murder_by_region[region] = 0
#     if region not in violent_by_region:
#         violent_by_region[region] = 0
#     if region not in nonviolent_by_region:
#         nonviolent_by_region[region] = 0
#     if state not in violent_by_state:
#         violent_by_state[state] = 0
#
#         # Accumulate data for violent_by_state (violent crimes: Murder, Rape, Robbery, Assault)
#     violent_by_state[state] += (
#     int(crime['Murder']) + int(crime['Rape']) + int(crime['Robbery']) + int(crime['Assault'])
#     )
#
#     # Accumulate data for murder_by_region (converting string to integer)
#     murder_by_region[region] += int(crime['Murder'])
#
#     # Accumulate data for violent_by_region (violent crimes: Murder, Rape, Robbery, Assault)
#     violent_by_region[region] += (
#             int(crime['Murder']) + int(crime['Rape']) + int(crime['Robbery']) + int(crime['Assault'])
#     )
#
#     # Accumulate data for nonviolent_by_region (nonviolent crimes: Burglary, Theft, Vehicle_Theft)
#     nonviolent_by_region[region] += (
#             int(crime['Burglary']) + int(crime['Theft']) + int(crime['Vehicle_Theft'])
#     )
#
# # Print the resultant dictionaries
# print("Murder by Region:", murder_by_region)
# print("Violent Crimes by Region:", violent_by_region)
# print("Nonviolent Crimes by Region:", nonviolent_by_region)
# print('_' * 40)
#
# import matplotlib.pyplot as plt
#
# # Create lists for regions and corresponding values
# regions = list(murder_by_region.keys())
#
# # Murder data
# murder_values = list(murder_by_region.values())
#
# # Violent crime data
# violent_values = list(violent_by_region.values())
#
# # Nonviolent crime data
# nonviolent_values = list(nonviolent_by_region.values())
#
# # Plotting Murder by Region
# plt.figure(figsize=(10, 6))
# plt.bar(regions, murder_values, color='red')
# plt.title('Murder Rate by Region')
# plt.xlabel('Region')
# plt.ylabel('Number of Murders')
# plt.xticks(rotation=45)  # Rotate x labels for better readability
# plt.tight_layout()  # Adjust layout for better fit
# plt.show()
#
# # Plotting Violent Crimes by Region
# plt.figure(figsize=(10, 6))
# plt.bar(regions, violent_values, color='blue')
# plt.title('Total Violent Crimes by Region')
# plt.xlabel('Region')
# plt.ylabel('Number of Violent Crimes')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
# # Plotting Nonviolent Crimes by Region
# plt.figure(figsize=(10, 6))
# plt.bar(regions, nonviolent_values, color='green')
# plt.title('Total Nonviolent Crimes by Region')
# plt.xlabel('Region')
# plt.ylabel('Number of Nonviolent Crimes')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
# total_violent_crime = 0
# for key, value in violent_by_region.items():
#     total_violent_crime += value
#
# #print(f"Total violent crimes: {total_violent_crime}")
# mean_total_violent_crime = total_violent_crime / len(states)
# print('National average violent crime : ' , mean_total_violent_crime)
#
# # Print the tabular result for violent crimes by state
# print("\nViolent Crimes by State (Tabular):")
# print(f"{'State':<25}{'Violent Crimes':<25}{'distance from mean':>25}")
# print("-" * 80)
#
# # Display the state-wise violent crimes
# total_violent_crime = 0
# for state, violent_crime in violent_by_state.items():
#     print(f"{state:<25}{violent_crime:<25}{violent_crime - mean_total_violent_crime:>15}")
#     total_violent_crime += violent_crime
#
# # Print total violent crimes across all states
# print("-" * 30)
# print(f"{'Total':<15}{total_violent_crime:>15}")