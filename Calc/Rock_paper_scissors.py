import random

player_wins = 0
computer_wins = 0
options = ['rock', 'scissors', 'paper']

while True:
    user_choice = input('Type rock or paper or scissors or e to quit:').lower()
    if user_choice == 'e':
        print('You won', player_wins, 'times',
              ',computer won', computer_wins, ',times')
        break

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]

    if user_choice == 'rock' and computer_choice == 'scissors':
        print('You won!')
        player_wins += 1

    elif user_choice == 'rock' and computer_choice == 'paper':
        print('Computer won!')
        computer_wins += 1

    elif user_choice == 'rock' and computer_choice == 'rock':
        print('Draw!')

    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You won!')
        player_wins += 1

    elif user_choice == 'paper' and computer_choice == 'scissors':
        print('Computer won!')
        computer_wins += 1

    elif user_choice == 'paper' and computer_choice == 'paper':
        print('Draw!')

    elif user_choice == 'scissors' and computer_choice == 'rock':
        print('Computer won!')
        player_wins += 1

    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You won!')
        player_wins += 1

    elif user_choice == 'scissors' and computer_choice == 'scissors':
        print('Draw!')

    else:
        print('Error')
