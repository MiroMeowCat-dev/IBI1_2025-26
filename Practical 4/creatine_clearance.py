# Store age, weight, gender, and creatinine concentration
# Check whether age is valid
# Check whether weight is valid
# Check whether creatinine concentration is valid
# Check whether gender is valid
# If any value is invalid, print an error message
# Otherwise, calculate creatinine clearance
# If gender is female, multiply by 0.85
# Print the final creatinine clearance
# Store age, weight, gender, and creatinine concentration
age = 25
weight = 60
gender = "female"
Cr = 80

# Check whether age is valid
if age >= 100:
    print("Error: age needs corrected")

# Check whether weight is valid
elif weight <= 20 or weight >= 80:
    print("Error: weight needs corrected")

# Check whether creatinine concentration is valid
elif Cr <= 0 or Cr >= 100:
    print("Error: creatinine concentration needs corrected")

# Check whether gender is valid
elif gender != "male" and gender != "female":
    print("Error: gender needs corrected")

# Otherwise, calculate creatinine clearance
else:
    CrCl = ((140 - age) * weight) / (72 * Cr)

    # If gender is female, multiply by 0.85
    if gender == "female":
        CrCl = CrCl * 0.85

    # Print the final creatinine clearance
    print("CrCl =", CrCl)