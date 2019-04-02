# This program allows the user to play Rock, Paper, Scissors
# with the computer
# 4/2/2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Tavius Cousar

# Import random function
# Define main function
# Get number from user
# Display choices amd restart
# Call the guess(number function)
# Call the main function

# Import random library function.
import random

# Define main function.
def main():

    # Get a random number.
    number = random.randint(1, 3)

    # Describe the program to the user.
    print('Welcome! lets play Rock, Paper, Scissors!')
    
    # Define guess(number) function.
    def guess(number):
        
        # Define the variables.
        rock = 1
        paper = 2
        scissors = 3

        # Get the number from the user.
        choice = int(input('Type in either (1) for rock,' +\
                           '(2) for paper, or (3) for scissors' +\
                           ' and press enter: '))

        # If the user chose rock, display:
        if choice == 1 and number == 2:
            print(number)
            print('Paper wraps rock.')
            print()
            main()

        elif choice == 1 and number == 3:
            print(number)
            print('Rock smashes the scissors.')
            print()
            main()
            
        # If the user chose paper, display:
        elif choice == 2 and number == 1:
            print(number)
            print('Paper wraps rock.')
            print()
            main()

        elif choice == 2 and number == 3:
            print(number)
            print('Scissors cuts paper.')
            print()
            main()

        #If the user chose scissors, display:
        elif choice == 3 and number == 1:
            print(number)
            print('Rock smashes the scissors.')
            print()
            main()

        elif choice == 3 and number == 2:
            print(number)
            print('Scissors cuts paper.')
            print()
            main()

        else:
            print(number)
            print('Both players made the same choice.')
            print()
            main()
                
    # Call the guess(number) function    
    guess(number)

# Call the main function    
main()    
