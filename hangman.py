import random

import hangmanart

import hangman_wordlist

display = []

count = 0

life = 7

chosen_word = random.choice(hangman_wordlist.word_list)

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

end_of_game = False

print(hangmanart.logo + '\n\n\n')

while not end_of_game:
    print(' '.join(display))
    guess = input("\n\nEnter a letter take a guess: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        life -= 1
        print(hangmanart.stages[life])

    if life == 0:
        end_of_game = True
        print("You lost")
        print(f"The word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print(''.join(display))
        print("You won")
