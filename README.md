# Noob-to-Pro-journey
#Guess the number game 
   # Import the random module to generate random numbers
    import random

# Define the main function for the Number Guessing Game


    def number_guessing_game():
    # Print a welcome message
       print("Welcome to the Number Guessing Game!")
    
    # Initialize a variable to control whether the user wants to play again
    play_again = "yes"
    
    # Start a loop that allows the user to play multiple times
    while play_again.lower() == "yes":
        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        
        # Initialize a variable to count the number of attempts
        attempts = 0
        
        # Initialize a variable to store the user's guess
        guess = None
        
        # Print instructions for the user
        print("I'm thinking of a number between 1 and 100.")
        
        # Start a loop that continues until the user guesses the correct number
        while guess != number_to_guess:
            try:
                # Ask the user to input their guess and convert it to an integer
                guess = int(input("Take a guess: "))
                
                # Increment the number of attempts
                attempts += 1
                
                # Check if the guess is too low
                if guess < number_to_guess:
                    print("Too low! Try again.")
                
                # Check if the guess is too high
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                
                # If the guess is correct, congratulate the user
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
            
            # Handle invalid input (e.g., if the user enters a non-number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
    
    # Print a goodbye message when the user decides to stop playing
    print("Thanks for playing!")

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the game
    number_guessing_game()
