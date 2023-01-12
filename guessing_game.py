# I should see some kind of text header, welcome or game intro message
import random
print(" Hi there! Welcome to the one and only Number Guessing Game!")
high_score = 100

# Random number should be chosen within range
def begin_playing():
    num_range = random.randint(1, 10)
    guess_attempt = 0
    attempt_limit = 7
    
# I should be continuously promptred for a guess until I get it right
    while True:
            try:
                guess_attempt += 1
                attempt_limit -= 1
                guess= int(input("Think of a number falling in the range of 1 to 10: "))
            except ValueError:
                print("Trying guessing with a number ONLY. ")
                continue
            # After an incorrect guess I should be told if my answer if higher or lower than the answer
            if guess > 10 or guess < 1:
                print(" Range has to be from 1 to 10. Try again! ")
                attempt_limit += 1
                continue
            if attempt_limit == 0 and guess != num_range:
                print (" Sorry, you lost. Feel free to try again trmo! ")
            if guess > num_range:
                print(" Try lower like the sea ")
                continue
            if guess < num_range:
                print(" Try higher like the sky ")
                continue
            else:
                # After the game ends I should be shown my number of attempts at guessing
                # When game ends, an ending message is shown to player
                print("Yay, you got it! It took you {} tries.").format(guess_attempt)
                break

begin_playing()












# Pick a number between 1 and 10
  
# It is higher!
# It is lower!

# You got it! It took you 2 tries

# Closing game, see you next time!

# You got it! It took you seven tries.
# Would you like to play again? [y]es/[n]o

# EXTRA CREDIT

# Player should be told to try again if guess is out of range

# Prompted if player would like to play again after win

# Beginning of each game -- shown current highest score 

# Random number is generated when player plays again

def end_game():
    guess_attempt = 0
    attempt_limit = 7
    while True:
        try_again=input("Would you like to play again? ")