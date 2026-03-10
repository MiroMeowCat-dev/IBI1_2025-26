# Set the initial number of infected students
# Set the growth rate over 24 hours
# Set the total class size
# Set the day counter
# While not all students are infected:
#     display the current day and number of infected students
#     calculate the number infected on the next day
#     increase the day counter
# After the loop, display the final day and total days taken
# Set the initial number of infected students
infected = 5

# Set the growth rate over 24 hours
growth_rate = 0.4

# Set the total class size
class_size = 91

# Set the day counter
day = 1

# While not all students are infected:
while infected < class_size:
    # display the current day and number of infected students
    print("Day", day, ":", infected, "students infected")
    
    # calculate the number infected on the next day
    infected = infected + infected * growth_rate
    
    # increase the day counter
    day = day + 1

# After the loop, display the final day and total days taken
print("Day", day, ":", infected, "students infected")
print("It took", day, "days to infect the whole class.")