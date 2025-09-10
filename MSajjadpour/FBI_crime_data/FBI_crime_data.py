import json
import matplotlib
import numpy

matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt

with open('FBI_CrimeData_2016.json', 'r') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

print("\nDataFrame info:")
print(df.info())

# Convert numeric columns from string to numeric
crime_types = ['Population', 'Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'Theft', 'Vehicle_Theft']
for col in crime_types:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate violent and non-violent crime totals
df['Violent_Crime'] = df['Murder'] + df['Rape'] + df['Robbery'] + df['Assault']
df['Nonviolent_Crime'] = df['Burglary'] + df['Theft'] + df['Vehicle_Theft']

# 1. Bar chart showing the number of "Murders by Region"
plt.figure(figsize=(12, 6))
murders_by_region = df.groupby('Region')['Murder'].sum().sort_values(ascending=False)
murders_by_region.plot(kind='bar', color='red', alpha=0.7)
plt.title('Murders by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Murders', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(murders_by_region):
    plt.text(i, v + max(murders_by_region) * 0.01, f'{v:,.0f}',
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# 2. Bar chart showing the number of "Violent Crimes by Region"
plt.figure(figsize=(12, 6))
violent_by_region = df.groupby('Region')['Violent_Crime'].sum().sort_values(ascending=False)
violent_by_region.plot(kind='bar', color='darkred', alpha=0.7)
plt.title('Violent Crimes by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Violent Crimes', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(violent_by_region):
    plt.text(i, v + max(violent_by_region) * 0.01, f'{v :,.0f}',
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# 3. Bar chart showing the number of "Non-violent Crimes by Region"
plt.figure(figsize=(12, 6))
nonviolent_by_region = df.groupby('Region')['Nonviolent_Crime'].sum().sort_values(ascending=False)
nonviolent_by_region.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Non-violent Crimes by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Non-violent Crimes', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(nonviolent_by_region):
    plt.text(i, v + max(nonviolent_by_region) * 0.01, f'{v:,.0f}',
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# 4. Report: Tabular list showing total violent crimes for each State and distance from national mean
# Calculate total violent crimes by state
state_violent = df.groupby('State')['Violent_Crime'].sum().reset_index()
state_violent.columns = ['State', 'Total_Violent_Crimes']

# Calculate national mean
national_mean = state_violent['Total_Violent_Crimes'].mean()

# Calculate distance from mean
state_violent['Distance_From_Mean'] = state_violent['Total_Violent_Crimes'] - national_mean
state_violent['Percent_From_Mean'] = (state_violent['Distance_From_Mean'] / national_mean) * 100

# Sort by total crimes (descending)
state_violent = state_violent.sort_values('Total_Violent_Crimes', ascending=False)

# Create formatted report for display
report = state_violent.copy()
report['Total_Violent_Crimes'] = report['Total_Violent_Crimes'].apply(lambda x: f'{x:,.0f}')
report['Distance_From_Mean'] = report['Distance_From_Mean'].apply(lambda x: f'{x:+,.0f}')
report['Percent_From_Mean'] = report['Percent_From_Mean'].apply(lambda x: f'{x:+.1f}%')

# Display the report
print("=" * 80)
print("VIOLENT CRIMES REPORT BY STATE")
print("=" * 80)
print(f"National Mean: {national_mean:,.0f} violent crimes")
print("=" * 80)
print(report.to_string(index=False))
print("=" * 80)

# Additional summary statistics
above_mean = len([x for x in state_violent['Distance_From_Mean'] if x > 0])
below_mean = len([x for x in state_violent['Distance_From_Mean'] if x < 0])

print("\nSUMMARY STATISTICS:")
print(f"Total states: {len(report)}")
print(f"States above national mean: {above_mean}")
print(f"States below national mean: {below_mean}")
print(f"Highest violent crimes: {state_violent['Total_Violent_Crimes'].max():,.0f}")
print(f"Lowest violent crimes: {state_violent['Total_Violent_Crimes'].min():,.0f}")

# Show detailed region summary
print("\n" + "=" * 60)
print("DETAILED REGION CRIME SUMMARY")
print("=" * 60)
region_summary = df.groupby('Region').agg({
    'Murder': 'sum',
    'Rape': 'sum',
    'Robbery': 'sum',
    'Assault': 'sum',
    'Violent_Crime': 'sum',
    'Burglary': 'sum',
    'Theft': 'sum',
    'Vehicle_Theft': 'sum',
    'Nonviolent_Crime': 'sum'
}).reset_index()

# Format the numbers for better readability
formatted_region_summary = region_summary.copy()
for col in region_summary.columns[1:]:
    formatted_region_summary[col] = formatted_region_summary[col].apply(lambda x: f'{x:,.0f}')

print(formatted_region_summary.to_string(index=False))

# Show top 5 cities with highest violent crime rates
print("\n" + "=" * 60)
print("TOP 5 CITIES WITH HIGHEST VIOLENT CRIME RATES (per 100,000 people)")
print("=" * 60)
df['Violent_Crime_Rate'] = (df['Violent_Crime'] / df['Population']) * 100000
top_cities = df.nlargest(5, 'Violent_Crime_Rate')[
    ['City', 'State', 'Violent_Crime_Rate', 'Violent_Crime', 'Population']]
top_cities['Violent_Crime_Rate'] = top_cities['Violent_Crime_Rate'].round(2)
top_cities['Population'] = top_cities['Population'].apply(lambda x: f'{x:,.0f}')
top_cities['Violent_Crime'] = top_cities['Violent_Crime'].apply(lambda x: f'{x:,.0f}')
print(top_cities.to_string(index=False))

# Read the Data
# df = pd.read_json("FBI_CrimeData_2016.json")
# df.info()

# print("=" * 60)
# # Display first few rows
# print(df.head())
#
# print("=" * 60)
# # Summary statistics for numerical columns
# print(df.describe())
#
# print("=" * 60)
# # Check unique states and regions
# print(df['Region'].unique())
# print(df['State'].nunique(), "states")
#
# print("=" * 60)
#
# crime_types = ['Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'Theft', 'Vehicle_Theft']
# describe = df.describe().T
# skew = df[crime_types].skew().to_frame(name='skew')
# kurt = df[crime_types].kurtosis().to_frame(name='kurtosis')
#
# total_describe = pd.concat([describe, skew, kurt], axis=1)
# print(total_describe)
# print("=" * 60)
#
#
# # Group by Region and sum murders
# murders_by_region = df.groupby('Region')['Murder'].sum()
# print(type(murders_by_region))
#
# plt.figure(figsize=(8, 5))
# plt.title("Murders by Region (2016)")
# plt.ylabel("Number of Murders")
# plt.xlabel("Region")
# plt.xticks(rotation=45)
# murders_by_region.plot(kind='bar')
# plt.show()
# # plt.savefig('test.png')
