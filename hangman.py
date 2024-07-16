import random
import hangman_wordlist_ru
import hangmanart
import hangman_wordlist

display = []

history_guess = []

life = 7

end_of_game = False

print(hangmanart.logo + '\n\n\n')
lang = 0
while lang != 1 or lang != 2:
    lang = int(input("To play in English press: 1 \nTo play in Russian press: 2\n2"))
    if lang == 1:
        chosen_word = random.choice(hangman_wordlist.word_list)
        word_length = len(chosen_word)
        for _ in range(word_length):
            display += "_"
        while not end_of_game:
            print(' '.join(display))
            guess = input("\n\nEnter a letter take a guess: ").lower()

            if guess in history_guess:
                print(f"You already tried {guess}")
            else:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter

                if guess not in chosen_word:
                    print(f'\'{guess.capitalize()}\' Is not in the word')
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
            history_guess.append(guess)
    elif lang == 2:
        chosen_word = random.choice(hangman_wordlist_ru.word_list)
        word_length = len(chosen_word)
        for _ in range(word_length):
            display += "_"
        while not end_of_game:
            print(' '.join(display))
            guess = input("\n\nУгадай букву: ").lower()

            if guess in history_guess:
                print(f"Вы уже пробовали {guess}")
            else:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter

                if guess not in chosen_word:
                    print(f'\'{guess.capitalize()}\' не в слове')
                    life -= 1
                    print(hangmanart.stages[life])

                if life == 0:
                    end_of_game = True
                    print("Вы проиграли")
                    print(f"Избранное слово {chosen_word}")

                if "_" not in display:
                    end_of_game = True
                    print(''.join(display))
                    print("Вы победили")
            history_guess.append(guess)

