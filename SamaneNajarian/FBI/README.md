Overview:
This final project is a basic data science project that uses much of the knowledge gained so far. You will also be introduced to data visualization using python modules.
Description:
You are to analyze FBI crime statistics for 2016. The data consists of crime statistics for each city (and the District of Columbia) itemized by type of crime.
The data is in the json file FBI_CrimeData_2016.json. Once the data in this file is loaded into a variable, the resultant data structure is a list where each element is a dictionary. Each dictionary consists of the following key-value pairs;
Region:	The region in which the State is located. The values are Midwest, Northeast, South, and West.
State:	The State name including the District of Columbia. City:	The city in which the crimes occurred.
Population:	The city population.
Murder:	The number of murders that occurred in the city. Rape:	The number of rapes that occurred in the city.
Robbery:	The number of robberies that occurred in the city. Assault:	The number of assaults that occurred in the city. Burglary:	The number of burglaries that occurred in the city.
Theft:	The number of thefts, exclusive of vehicle, that occurred in the city. Vehicle_Theft:	The number of vehicle thefts that occurred in the city
For purposes of the project, the crimes murder through assault are considered violent crimes. The remaining three categories are considered non-violent crimes.
Objective:
From the crime statistics data, you are to produce the following output:
1.	A bar chart showing the number of “Murders by Region”.
2.	A bar chart showing the number of “Violent Crimes by Region”.
3.	A bar chart showing the number of “Non-violent Crimes by Region”.
4.	A report which is tabular list showing the total violent crimes for each State and the distance from the national mean.
