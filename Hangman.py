import random
from hangman_words import word_list

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = [r'''+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

def play_game():
    lives = 6
    wrong_guesses = 0
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = "_" * word_length
    correct_letters = []
    used_letters = []

    print("=*" * 25)
    print(logo)
    print("=*" * 25)
    print(f"The word has {word_length} letters.")
    print("Word to guess: " + display)

    game_over = False

    while not game_over:
        print(f"\nLives left: {lives}/6")
        print(f"Wrong guesses: {wrong_guesses}")
        print(f"Used letters: {', '.join(used_letters)}")

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
            elif guess in used_letters:
                print(f"You've already used '{guess}'. Try another!")
            else:
                break

        used_letters.append(guess)
        new_display = ""

        for letter in chosen_word:
            if letter == guess or letter in correct_letters:
                new_display += letter
            else:
                new_display += "_"

        if guess in chosen_word:
            correct_letters.append(guess)
        else:
            lives -= 1
            wrong_guesses += 1
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        print("Word to guess: " + new_display)
        print(stages[lives])
        display = new_display

        if "_" not in display:
            print(f"\n************** YOU WIN **************")
            print(f"The word is '{chosen_word}'!")
            game_over = True

        elif lives == 0:
            print(f"\n************** YOU LOSE **************")
            print(f"The word was '{chosen_word}'.")
            game_over = True

    # Restart prompt
    restart = input("\nDo you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if restart == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
play_game()
