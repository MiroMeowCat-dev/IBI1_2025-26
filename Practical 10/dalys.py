import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/36135/Desktop/IBI1/IBI1_2025-26/Practical 10")

# Check directory
print(os.getcwd())
print(os.listdir())

# Read csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Inspect dataframe
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())

# Show the 3rd and 4th columns for the first 10 rows
first_10_year_dalys = dalys_data.iloc[0:10, 2:4]
print(first_10_year_dalys)

max_year_first10 = first_10_year_dalys.loc[first_10_year_dalys["DALYs"].idxmax(), "Year"]
print("Year with max DALYs in first 10 rows:", max_year_first10) 
# The year with the maximum DALYs in the first 10 Afghanistan rows is 1998.

# Show all years for Zimbabwe using Boolean selection
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)
first_year_zimbabwe = zimbabwe_years.iloc[0]
last_year_zimbabwe = zimbabwe_years.iloc[-1]
# Zimbabwe data are recorded from 1990 to 2019.

# Get 2019 data
print(first_year_zimbabwe)
print(last_year_zimbabwe)
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
print(recent_data)

# Find max and min DALYs countries in 2019
max_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row = recent_data.loc[recent_data["DALYs"].idxmin()]
print(max_row)
print(min_row)
max_country = max_row["Entity"]
min_country = min_row["Entity"]
print("Max country in 2019:", max_country)
print("Min country in 2019:", min_country)

# In 2019, the country with the maximum DALYs is Lesotho.
# In 2019, the country with the minimum DALYs is Singapore.

# Plot DALYs over time for one country
country_data = dalys_data.loc[dalys_data["Entity"] == max_country, ["Year", "DALYs"]]

plt.figure(figsize=(10, 5))
plt.plot(country_data["Year"], country_data["DALYs"], 'b+')
plt.xticks(country_data["Year"], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {max_country}")
plt.tight_layout()
plt.show()

# Additional question: distribution of DALYs in 2019
distribution_2019 = dalys_data.loc[dalys_data["Year"] == 2019, "DALYs"]

plt.figure(figsize=(8, 5))
plt.hist(distribution_2019, bins=30)
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across countries in 2019")
plt.tight_layout()
plt.show()