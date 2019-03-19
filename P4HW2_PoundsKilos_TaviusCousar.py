# This program displays a table of pounds and their equivalent kilograms
# from 100 through 300.
# 3/19/2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Tavius Cousar

# Create a table of Pounds to Kilograms
# Create for loop with a range form 100 to 300 with a step value of 10
# Calculate the pounds to kilograms using formula kg = lb/2.2046
# Display the number of pounds and their equivalent kilograms

# Create table heading
print()
print('Pounds\tKilograms')
print('-----------------')

# Print the pounds to kilogram conversion
for number in range(100, 310, 10):
    # Calulate number of kilograms for number of pounds
    kilo = number/2.2046
    print(number, '\t' , format(kilo, '.2f'))
