# CTI-110
# P3HW2 - MealTipTax
# Tavius Cousar
# 2/27/2019
#
# Enter the price of the meal
# Display tip choices
# Enter the tip choice
# Calculate the total price of meal (price of meal * tip + price)
# Calculate the sales tax (charge * 0.07)
# Calculate the total (charge + sales tax)
# if tip == '0.15', '0.18', or '0.2'
#   Display tip
#   Display tax
#   Display total
# else:
#   Display Error

# Enter the price of meal
price = float(input('Enter the price of the meal: '))

# Enter tip choices
print('You have three choices for tip percentages:')
print('15% - type: 0.15')
print('18% - type: 0.18')
print('20% - type: 0.2')
tip = float(input('Enter tip: '))

# Calculations
charge = price * tip + price
tax = float(0.07)
sales_tax = charge * tax
total = charge + sales_tax

# Display the tip, sales tax, and total
if tip == float('0.15'):
    print('Tip: ', tip)
    print('Sales Tax: ', format(sales_tax, '.2f'))
    print('Total: ', format(total, '.2f'))
elif tip == float('0.18'):
    print('Tip: ', tip)
    print('Sales Tax: ', format(sales_tax, '.2f'))
    print('Total: ', format(total, '.2f'))
elif tip == float('0.2'):
    print('Tip: ', tip)
    print('Sales Tax: ', format(sales_tax, '.2f'))
    print('Total: ', format(total, '.2f'))
else:
    print('Error')
    
