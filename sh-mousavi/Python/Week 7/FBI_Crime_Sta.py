import json
import pandas as pd
import matplotlib.pyplot as plt

with open('FBI_CrimeData_2016.json') as fcd:
    crime_list = json.load(fcd)


# Function to accumulate crimes by a given key (Region or State) and crime type
def accum_crime(key, crime, crimelist):
    result = {}
    for record in crimelist:
        entity = record[key]
        crime_count = int(record[crime])
        if entity in result:
            result[entity] += crime_count
        else:
            result[entity] = crime_count
    return result


# Function to accumulate violent crimes (Murder, Rape, Robbery, Assault)
def accum_violent_crime(key, crimelist):
    result = {}
    for record in crimelist:
        entity = record[key]
        violent_crime_count = (int(record["Murder"]) +
                               int(record["Rape"]) +
                               int(record["Robbery"]) +
                               int(record["Assault"]))
        if entity in result:
            result[entity] += violent_crime_count
        else:
            result[entity] = violent_crime_count
    return result


# Function to accumulate non-violent crimes (Burglary, Theft, Vehicle Theft)
def accum_nonviolent_crime(key, crimelist):
    result = {}
    for record in crimelist:
        entity = record[key]
        nonviolent_crime_count = (int(record["Burglary"]) +
                                  int(record["Theft"]) +
                                  int(record["Vehicle_Theft"]))
        if entity in result:
            result[entity] += nonviolent_crime_count
        else:
            result[entity] = nonviolent_crime_count
    return result


# Function to create bar charts from a crime dictionary
def plot_crime_bar_chart(crime_dict, title, xlabel, ylabel, color='blue'):
    # Convert the dictionary into a DataFrame for easier handling
    crime_df = pd.DataFrame(list(crime_dict.items()), columns=['Region', 'Incidence'])

    # Print the DataFrame for verification
    print(f"\n{title}:")
    print(crime_df)

    # Plot the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(crime_df['Region'], crime_df['Incidence'], color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Create the dictionary for "Murders by Region"
    murder_by_region = accum_crime("Region", "Murder", crime_list)

    # Create the dictionary for "Violent Crimes by Region"
    violent_by_region = accum_violent_crime("Region", crime_list)

    # Create the dictionary for "Non-violent Crimes by Region"
    nonviolent_by_region = accum_nonviolent_crime("Region", crime_list)

    # Print the resulting dictionaries
    print(f"Murders by Region: {murder_by_region}")
    print(f"\nViolent Crimes by Region: {violent_by_region}")
    print(f"\nNon-violent Crimes by Region: {nonviolent_by_region}")

    # Plotting "Murders by Region"
    plot_crime_bar_chart(murder_by_region, title="Murders by Region",
                                           xlabel="Region",
                                           ylabel="Number of Murders",
                                           color='red')

    # Plotting "Violent Crimes by Region"
    plot_crime_bar_chart(violent_by_region, title="Violent Crimes by Region",
                                            xlabel="Region",
                                            ylabel="Number of Violent Crimes",
                                            color='orange')

    # Plotting "Non-violent Crimes by Region"
    plot_crime_bar_chart(nonviolent_by_region, title="Non-violent Crimes by Region",
                                               xlabel="Region",
                                               ylabel="Number of Non-violent Crimes",
                                               color='green')

    # Calculate total violent crimes by State using accum_violent_crime function
    violent_by_state = accum_violent_crime("State", crime_list)

    # Calculate the national mean for violent crimes
    national_mean = sum(violent_by_state.values()) / len(violent_by_state)

    # Create a report showing total violent crimes and distance from the national mean
    report = []
    for state, total_crimes in violent_by_state.items():
        distance_from_mean = total_crimes - national_mean
        report.append((state, total_crimes, distance_from_mean))

    # Convert the report into a DataFrame for better display
    report_df = pd.DataFrame(report, columns=["State", "Crimes", "Distance from Mean"])

    # Print the tabular report
    print("\nTotal Violent Crimes by State and Distance from National Mean:")
    print(report_df.to_string(index=False,
                              formatters={"Crimes": "{: 12,.0f}".format,
                                          "Distance from Mean": "{: 24,.0f}".format}))
