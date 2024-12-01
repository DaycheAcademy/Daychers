import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('FBI_CrimeData_2016.json')

# First subplot: Number of murders by region
region_murders = df.groupby('Region')['Murder'].sum()

# Create subplots with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Number of murders by region (row 1, col 1)
axes[0, 0].bar(region_murders.index, region_murders.values, color=['red', 'green', 'blue', 'yellow'])
axes[0, 0].set_title("Number of Murders by Region")
axes[0, 0].set_xlabel("Region")
axes[0, 0].set_ylabel("Murders")
for i, value in enumerate(region_murders.values):
    axes[0, 0].text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Plot 2: Violent crimes by region (row 2, col 1)
violent_Crimes_by_Region = df.groupby('Region')[['Assault', 'Murder', 'Robbery', 'Rape']].sum().reset_index()
violent_Crimes_by_Region['sumOf_Violent_Crime'] = violent_Crimes_by_Region[['Assault', 'Murder', 'Robbery', 'Rape']].sum(axis=1)
axes[1, 0].bar(violent_Crimes_by_Region['Region'], violent_Crimes_by_Region['sumOf_Violent_Crime'], color=['red', 'green', 'blue', 'yellow'])
axes[1, 0].set_title("Number of Violent Crimes by Region")
axes[1, 0].set_xlabel("Region")
axes[1, 0].set_ylabel("Violent Crimes")
for i, value in enumerate(violent_Crimes_by_Region['sumOf_Violent_Crime']):
    axes[1, 0].text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Plot 3: Nonviolent crimes by region (row 1, col 2)
nonviolent_Crimes_by_Region = df.groupby('Region')[['Burglary', 'Theft', 'Vehicle_Theft']].sum().reset_index()
nonviolent_Crimes_by_Region['sumOf_nonViolent_Crime'] = nonviolent_Crimes_by_Region[['Burglary', 'Theft', 'Vehicle_Theft']].sum(axis=1)
axes[0, 1].bar(nonviolent_Crimes_by_Region['Region'], nonviolent_Crimes_by_Region['sumOf_nonViolent_Crime'], color=['red', 'green', 'blue', 'yellow'])
axes[0, 1].set_title("Number of Nonviolent Crimes by Region")
axes[0, 1].set_xlabel("Region")
axes[0, 1].set_ylabel("Nonviolent Crimes")
for i, value in enumerate(nonviolent_Crimes_by_Region['sumOf_nonViolent_Crime']):
    axes[0, 1].text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Plot 4: National average violent crimes by state (row 2, col 2)
National_AVG_violent_Crimes_by_State = df.groupby('State')[['Assault', 'Murder', 'Robbery', 'Rape']].sum().reset_index()
National_AVG_violent_Crimes_by_State['sumOf_Violent_Crime_State'] = National_AVG_violent_Crimes_by_State[['Assault', 'Murder', 'Robbery', 'Rape']].sum(axis=1)
mean_violent_crime = violent_Crimes_by_Region['sumOf_Violent_Crime'].sum() / len(National_AVG_violent_Crimes_by_State['State'])
National_AVG_violent_Crimes_by_State['distance from mean'] = National_AVG_violent_Crimes_by_State['sumOf_Violent_Crime_State'] - mean_violent_crime

data_to_display = National_AVG_violent_Crimes_by_State.head(20)

axes[1, 1].axis('tight')
axes[1, 1].axis('off')
table = axes[1, 1].table(
    cellText=data_to_display[['State', 'sumOf_Violent_Crime_State', 'distance from mean']].values,
    colLabels=['State', 'Sum of Violent Crimes', 'Distance from Mean'],
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(8)
table.auto_set_column_width([0, 1, 2])

for i, key in enumerate(table.get_celld().keys()):
    cell = table[key]
    if i == 0:
        continue
    cell.set_height(0.05)
ll
table.auto_set_column_width([0, 1, 2])

plt.tight_layout()
plt.show()

