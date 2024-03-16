import random


def executioner():
    words = ['line', 'word', 'plane', 'wing', 'python']
    word = random.choice(words)
    print('You have only 5 guesses!')
    guesses = ''
    user_tries = 6

    while user_tries > 0:
        print('The word is', len(word), 'characters long')
        for element in word:
            if (element in guesses):
                print(element, end=' ')
            else:
                print('_', end=' ')

        guess = input('Guess the letter:')
        guesses += guess

        if guess not in word:
            user_tries -= 1
            print("You're dead!")

        if (set(word) <= set(guesses)):
            print("You won!", word, 'was the word')
            break
        elif user_tries == 0:
            print("Your tries ended")


executioner()
