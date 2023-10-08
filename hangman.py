import random
import title_art
import hangman_art  #TODO may need some different versions of ASCII art depending on difficulty level

# prints title
print(title_art.title)

# retrieves word list from csv file
with open('hangman.csv', 'r') as csv_file:
    word_list = [word.lower() for word in csv_file.read().splitlines()]  #TODO change CSV file to comma separated

# initialises variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display_guess = ["_" for _ in chosen_word] # initialises with underscores
lives = 6 #TODO add other options for lives numbers based on difficulty levels
#TODO variable called 'guessed letter' so if you guess the same letter the programme tells you to try again

# game loop starts
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #TODO add a check to see if user has provided single letter, or greater than 1 length
    #TODO if input greater than one length, then assume they are guessing whole word

    # check guess letter
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display_guess[pos] = letter

    # if guess not a letter in the chosen word, lives reduce by 1
    if guess not in chosen_word:
        lives -= 1
        # TODO clear the screen between guesses?

    # if lives reach 0 then game over and you lose
    if lives == 0:
        end_of_game = True
        print(f'Game over - you lose! The word was: {chosen_word}.')
    else:
        print(' '.join(display_guess))

    # check if user has got all the letters
    if "_" not in display_guess:
        end_of_game = True
        print('You won!')

    # print the hangman stage art based on remaining lives
    print(hangman_art.stages[lives])
