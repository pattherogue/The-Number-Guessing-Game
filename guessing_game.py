# I should see some kind of text header, welcome or game intro message

# Random number should be chosen within range

# I should be continuously promptred for a guess until I get it right

# After an incorrect guess I should be told if my answer if higher or lower than the answer

# After the game ends I should be shown my number of attempts at guessing

# When game ends, an ending message is shown to player

import random
print(" Hi there! Welcome to the one and only Number Guessing Game!")

def begin_playing():
    num_range = random.randint(1, 10)
    guess_attempt = 0
    attempt_limit = 10

# Pick a number between 1 and 10
    while True:
        try:
            guess= int(input("Think of a number falling in the range of 1 to 10: "))
        except ValueError:
            print("Trying guessing with a number ONLY :)")
            continue
        if guess < 1:
            print("Sorry, guess cannot be less than 1. ") 
            continue
        if guess > 10:
            print("Sorry, guess cannot be greater than 10. ")
            continue
        if guess > num_range:
            guess_attempts += 1
            print("Go higher")
        if guess < num_range:
            guess_attempts += 1
            print("Go higher")
        if guess == num_range:
            guess_attempts += 1
            print("Yay, you got it! It took you {guess_attempt} tries.")
            break

begin_playing()

# It is higher!
# It is lower!

# You got it! It took you 2 tries

# Closing game, see you next time!

# You got it! It took you seven tries.
# Would you like to play again? [y]es/[n]o