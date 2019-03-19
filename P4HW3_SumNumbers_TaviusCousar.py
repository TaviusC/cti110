# This program has a loop that requires a user to enter in
# a positive number which displays a list of even intergers
# to find their sum.
# 3/19/2019
# CTI-110 P4HW3 - Sum of Numbers
# Tavius Cousar

# The accumulator is set to 0.0.
# The while loop of repeat = '2' will allow the user
# to continue or end the loop.
# Describe how the program works.
# Set up a for loop to display and calculate the sum.
# Display the sum.
# Ask user to repeat the process.

#The accumulator is set to 0.0.
total = 0.0

# This will allow the user to continue or
# end the loop.
repeat = '2'

#Set up a while loop to be repeated.
while repeat == '2':

    # Clarify how the program works.
    print('This program calculates the sum of positive numbers')

    # The starting number will be 2.
    print('The starting number is 2')

    # The user enters an even interger.
    number = int(input('Enter your highest positive number: '))

    #Display the list of even intergers.
    for counter in range(2, number + 2, 2):
        total += counter
        print(counter)

    # Display the total.
    print('The total is', total)

    # Ask user if they want to repeat
    # the process.
    repeat = input('Repeat this process? ' +\
                   '(Enter 2 to continue or' +\
                   ' -2 to end) ')
                 
    
