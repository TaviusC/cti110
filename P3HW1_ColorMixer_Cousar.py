# This program will recieve the input of two primary colors to mix
# 2/26/2019
# CTI-110 P3HW1 - Color Mixer
# Tavius Cousar
#
# Get the color of primary color 1
# Get the color of primary color 2
# Calculate the primary color mixtures to get secondary color
# if color1 != 'red', 'blue', or 'yellow' and color2 != 'red', 'blue', or 'yellow'
#   Display "Error"
# if color1 == 'red', 'blue', or 'yellow' and color2 == 'red', 'blue', or 'yellow'
#   Display "The color created is (mixture)."

# Get the primary colors
# Only red, blue, or yellow could be entered
color1 = input('Enter primary color 1: ')
color2 = input('Enter primary color 2: ')
if color1 == 'red' and color2 == 'red':
    print('The color created is red.')
elif color1 == 'red' and color2 == 'blue':
    print('The color created is purple.')
elif color1 == 'red' and color2 == 'yellow':
    print('The color created is orange.')
elif color1 == 'blue' and color2 == 'red':
    print('The color created is purple.')
elif color1 == 'blue' and color2 == 'blue':
    print('The color created is blue.')
elif color1 == 'blue' and color2 == 'yellow':
    print('The color created is green.')
elif color1 == 'yellow' and color2 == 'red':
    print('The color created is orange.')
elif color1 == 'yellow' and color2 == 'blue':
    print('The color created is green.')
elif color1 == 'yellow' and color2 == 'yellow':
    print('The color created is yellow.')
else:
    print("Error")



