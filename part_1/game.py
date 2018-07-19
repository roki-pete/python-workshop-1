import random

words = ['piano',
         'violin',
         'guitar',
         'flute',
         'drums']

random_index = random.randint(0, len(words) - 1)
current_word = words[random_index]


guessed_word = ['_'] * len(current_word)


guessed_letters = []

guessing = True

while guessing:
    print("".join(guessed_word))

    if guessed_letters:
        print('Guessed letters:', ", ".join(guessed_letters))

    letter_guess = input('Guess a letter? ')[0]
    if letter_guess:
        for count, letter in enumerate(current_word):
            if letter == letter_guess:
                guessed_word[count] = letter

        if "_" not in guessed_word:
            guessing = False
            print("You guessed the word \"{}\" correctly!".format(
                current_word))

        guessed_letters.append(letter_guess)
