import matplotlib.pyplot as plt

# Step 1: Store the heart rate data in a list
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
# Step 2: Calculate and print the number of patients and mean heart rate
num_patients=len(heart_rates)
mean_heart_rate=sum(heart_rates)/num_patients
print(f"Number of patients: {num_patients}")
print(f"Mean heart rate: {mean_heart_rate:.2f} bpm")
# Step 3: Count heart rate categories
low_count=0
normal_count=0
high_count=0
for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif 60 <= rate <= 120:
        normal_count += 1
    else:
        high_count += 1 
print(f"\nLow heart rate patients:{low_count}")
print(f"Normal heart rate patients:{normal_count}")
print(f"High heart rate patients:{high_count}")
# Step 4: Identify the largest category
categories = {
    "Low": low_count,
    "Normal": normal_count,
    "High": high_count
}
largest_category=max(categories, key=categories.get)
print(f"\nThe category with the largest number of patients is: {largest_category}")
# Step 5: Create a pie chart
labels=list(categories.keys())
sizes=list(categories.values())
            
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Distribution of Heart Rate Categories")
plt.show() 
