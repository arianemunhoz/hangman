import random
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
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

lives = 6
wrong_guesses = 0

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print("=*" * 25)
print(logo)
print("=*" * 25)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(f"A palavra tem {word_length} letras.")
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
used_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"Vidas restantes: {lives}/6")
    print(f"Tentativas erradas: {wrong_guesses}")
    print(f"Letras já usadas: {', '.join(used_letters)}")
    
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, insira uma única letra válida.")
        else:
            break

    if guess in used_letters:
        print(f"You've already used this letter {used_letters}. Try another!")
        continue
    else:
        used_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        wrong_guesses += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"Vidas restantes: {lives}/6")

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\nThe word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print(f"****************************YOU WIN****************************\nThe word is {chosen_word}!")

    print(stages[lives])

    if game_over:
        restart = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
        if restart == 'y':
            # Reinicia as variáveis
            lives = 6
            wrong_guesses = 0
            chosen_word = random.choice(word_list)
            display = "_" * len(chosen_word)
            correct_letters = []
            used_letters = []
            game_over = False
        else:
            print("Thanks for playing! Goodbye!")
            break  # Sai do jogo
