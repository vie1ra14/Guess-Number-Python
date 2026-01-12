import random


def checknumber(x):
    try:
        int(x)
        return True
    except ValueError or TypeError:
        return False
    
def selectdifficulty(difficulty):
    levels = {
        '1': ('Easy', 10),
        '2': ('Medium', 5),
        '3': ('Hard', 3)
    }

    return levels.get(difficulty, (None, None))


def checkluck(guessNumber, random_number):
    if guessNumber == random_number:
        return 0

    return -1 if guessNumber < random_number else 1

while True:
    randomNumber = random.randint(1, 100)
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100.')
    print('You have 5 chances to guess the correct number.\n')
    print('Please select the difficulty level:')
    print('1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n')
    guess = input('Enter your choice: ')

    level, levelInt = selectdifficulty(guess)
    if levelInt is None:
        print('Select a valid difficulty: [1, 2 or 3]')
        print('')
        print('')
        continue
    print('')
    print(f'Great! You have selected the {level} difficulty level.')
    print('Lets start the game!')

    attempts = 0
    for i in range(levelInt):
        
        guessNumber = input('Enter your guess: ')
        attempts += 1

        if not checknumber(guessNumber):
            print('Selecione um numero válido')
            continue
        result = checkluck(int(guessNumber), randomNumber)
        if result == 0:
            print(f'Congratulations! You guessed the correct number in {attempts} attempts!')
            break
        elif result == -1:
            print(f'Incorrect! The number is greater than {guessNumber}')
        else:
            print(f'Incorrect! The number is less than {guessNumber}')

    print('GAME OVER!')



