import pandas as pd

data = pd.read_csv("../Data/openpowerlifting-2023-08-12-9f1b3427.csv")
# Filter data for "Event" is "SBD", "Equipment" is "Raw", and "Federation" is "IPF"
filtered_data = data.loc[(data["Event"] == "SBD") & (data["Equipment"] == "Raw") & (data["Federation"] == "IPF")]



# Separate data by gender and weight class

men_total_50kg = filtered_data[(filtered_data["Sex"] == "M") & (filtered_data["BodyweightKg"] >= 50) & (filtered_data["BodyweightKg"] <= 55)]["TotalKg"]
women_total_50kg = filtered_data[(filtered_data["Sex"] == "F") & (filtered_data["BodyweightKg"] >= 50) & (filtered_data["BodyweightKg"] <= 55)]["TotalKg"]

# Doing the same for the 100-105kg weight class

men_total_100kg = filtered_data[(filtered_data["Sex"] == "M") & (filtered_data["BodyweightKg"] >= 100) & (filtered_data["BodyweightKg"] <= 105)]["TotalKg"]
women_total_100kg = filtered_data[(filtered_data["Sex"] == "F") & (filtered_data["BodyweightKg"] >= 100) & (filtered_data["BodyweightKg"] <= 105)]["TotalKg"]

# Creating the data for the whole total

men_total = filtered_data[filtered_data['Sex'] == 'M']["TotalKg"]
women_total = filtered_data[filtered_data['Sex'] == 'F']["TotalKg"]

men_total = men_total.dropna()
women_total = women_total.dropna()

data_WPC = data[data['Federation'] == 'WPC']
men_total_WPC = data_WPC[data_WPC["Sex"] == "M"]["TotalKg"]
men_total_IPF = filtered_data[filtered_data["Sex"] == "M"]["TotalKg"]

men_bench = filtered_data[filtered_data["Sex"] == "M"]["Best3BenchKg"]
women_bench = filtered_data[filtered_data["Sex"] == "F"]["Best3BenchKg"]

men_bench = men_bench[men_bench >= 0]
women_bench = women_bench[women_bench >= 0]