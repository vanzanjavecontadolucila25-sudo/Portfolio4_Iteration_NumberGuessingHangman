##Read Me: In fulfillment for the subject BES 10a, this project is a Python-based Number Guessing Hangman game that applies Chapter 5 loop and iteration concepts. It features a  nested setup, using an outer definite "for" loop to cycle through game rounds and an inner indefinite "while" loop for active, turn-by-turn guessing. The game logic relies on basic loop patterns: a counter variable tracks mistakes , a boolean search flag verifies guesses, and an "if/elif" structure prints the text-based hangman drawings. Finally, "break" statements handle wins or losses , while a "continue" statement skips over lines starting with #, showing how simple control flow can build an interactive terminal application.

##This is the title section
print("===================NUMBER GUESSING HANGMAN==================")
print("Instructions: Guess one digit at a time. Type '#' to write a")
print("note, or 'done' to quit.")
# The list of secret numbers for each round
all_codes = [
    ['3', '7', '4'], 
    ['9', '1', '5'], 
    ['0', '8', '2'],
    ['6', '4', '8']
]

# Track if the player wants to keep playing the game
play_again = True


# Loop through each secret number list, one round at a time
for secret_code in all_codes:
    
    # Stop the game completely if the player chose to quit
    if play_again is False:
        break
        
    # Reset the guesses and mistakes at the start of every new round
    guessed_digits = ''     
    mistakes = 0     
    max_mistakes = 5        
    
    print()  # Prints a blank line for spacing
    print('============================================================')
    print('🆕 Starting a brand new round with a new hidden number!')
    print('============================================================')

    # Keep running the current round until it ends
    while True:
        
        # Print the hangman picture depending on how many mistakes were made
        print()  # Prints a blank line for spacing
        if mistakes == 0:
            print("   +---+")
            print("   |   |")
            print("       |")
            print("       |")
            print("       |")
            print("  =======")
        elif mistakes == 1:
            print("   +---+")
            print("   |   |")
            print("   O   |")
            print("       |")
            print("       |")
            print("  =======")
        elif mistakes == 2:
            print("   +---+")
            print("   |   |")
            print("   O   |")
            print("   |   |")
            print("       |")
            print("  =======")
        elif mistakes == 3:
            print("   +---+")
            print("   |   |")
            print("   O   |")
            print("  /|   |")
            print("       |")
            print("  =======")
        elif mistakes == 4:
            print("   +---+")
            print("   |   |")
            print("   O   |")
            print("  /|\\  |")
            print("       |")
            print("  =======")
        elif mistakes == 5:
            print("   +---+")
            print("   |   |")
            print("   O   |")
            print("  /|\\  |")
            print("  / \\  |")
            print("  =======")

        print('------------------------------------------------------------')
        print('Current Hidden Number:')
        code_cracked = True
        
        # Go through each digit of the secret number one by one
        for digit in secret_code:
            
            # Check if this specific digit was already guessed
            found_digit = False
            for correct in guessed_digits:
                if correct == digit:
                    found_digit = True
            
            # Show the digit if it was guessed, otherwise show a blank space
            if found_digit is True:
                print(digit)
            else:
                print('_')
                code_cracked = False  
                
        print('------------------------------------------------------------')
        
        # End the round if the player successfully guessed all the digits
        if code_cracked is True:
            print('🎉 Great job! You guessed the full number and won this round!')
            break  
            
        # End the round if the player runs out of guesses
        if mistakes == max_mistakes:
            print('🔒 Game Over! The hangman is fully drawn.')
            print('The correct number was:', secret_code)
            break  
            
        guess = input('Guess a digit: ')
        
        # Skip everything else and ask again if the line starts with '#'
        if len(guess) > 0 and guess[0] == '#':
            print('💭 Saved your note. Moving to the next turn.')
            continue  
            
        # Stop the whole game if the user types 'done'
        if guess == 'done':
            play_again = False
            break

        # Check if the player's guess matches any digit inside the secret number
        correct_guess = False
        for digit in secret_code:
            if guess == digit:
                correct_guess = True
                
        # Save correct guesses or add to the mistake count
        if correct_guess is True:
            print('✨ Nice! That digit is in the number.')
            guessed_digits = guessed_digits + guess
        else:
            print('❌ Wrong guess! An item is added to the hangman drawing.')
            # Add 1 to the total mistakes count
            mistakes = mistakes + 1
            
        print()  # Prints a blank line for spacing
        print('============================================================')

print()  # Prints a blank line for spacing
print('Game over! Thanks for playing!')



