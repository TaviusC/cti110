# This program will generate a random number
# for the user to guess.
# 4/1/2019
# CTI-110 P5HW1_RandomNumber
# Tavius Cousar

# Import random library function
# Define the main function
# Number = Random number within (1, 100) range
# Inform the user of the program
# Define guess(number) function
# Create if-else statement
# If the number is too high, try again
# If the number is too low, try again
# Else, Congradulations and restart of program
# Call the guess(number) function
# Call the main function

# Import the random library function.
import random
 
# Define the main function
def main():
    
    # Get a random number.
    number = random.randint(1, 100)
    
    # Inform the user of the program
    print('Welcome to the "Random Number Guessing Game".')
    print('Can you guess the random number that will be generated?')
    print()

    # The user will input their number
    def guess(number):
        guess_number = int(input('Enter in a number: '))

        # Create if-else statement for guesses.
        if guess_number > number:
            print('Too high, try again.') 
            guess(number)
        elif guess_number < number:
            print('Too low, try again.')
            guess(number)
        # A congrats and the game restarts.
        else:
            print('Congradulations, you guessed right!')
            main()
    # Call the guess(number) function.
    guess(number)
        
# Call the main function
main()
        
    
