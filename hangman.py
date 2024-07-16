import random

import hangmanart

display = []

count = 0

life = 7

word_list = ["crazy", "monkey", "dog"]

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

end_of_game = False

print(hangmanart.logo)

while not end_of_game:
    print(' '.join(display))
    guess = input("Enter a letter take a guess: ").lower()

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

    if "_" not in display:
        end_of_game = True
        print("You won")
