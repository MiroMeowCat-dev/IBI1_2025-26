import matplotlib.pyplot as plt
# Step 1: Store the population data in a dictionary
population_data = {
    "UK": {"2010": 66.7, "2020": 69.2},
    "China": {"2010": 1426.0, "2020": 1410.0},
    "Italy": {"2010": 59.4, "2020": 58.9},
    "Brazil": {"2010": 208.6, "2020": 212.0},
    "USA": {"2010": 331.6, "2020": 340.1}
}

# Step 2: Calculate percentage population changes
population_changes = {}
for country,data in population_data.items():
    pop_2010 = data["2010"]
    pop_2020 = data["2020"]
    percent_change = ((pop_2020 - pop_2010) / pop_2010) * 100
    population_changes[country] = percent_change
# Step 3: Print the percentage change for each countryprint("Percentage population changes from 2010 to 2020:")
for country, change in population_changes.items():
    print(f"{country}: {change:.2f}%")

# Step 4: Sort changes from largest increase to largest decrease
sorted_changes = sorted(population_changes.items(), key=lambda x:x[1], reverse=True)
print("\nPopulation changes in descending order:")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")
# Step 5: Identify the largest increase and largest decrease
largest_increase_country = sorted_changes[0][0]
largest_decrease_country = sorted_changes[-1][0]

print(f"\nCountry with the largest increase: {largest_increase_country}")
print(f"Country with the largest decrease: {largest_decrease_country}")
# Step 6: Create a bar chart
countries = list(population_changes.keys())
changes = list(population_changes.values())

plt.bar(countries, changes)
plt.title("Population Change by Country (2020 to 2024)")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
colors = ['green' if x > 0 else 'red' for x in changes]
plt.bar(countries, changes, color=colors)
plt.show()