import time
import random

def loading_animation():
    """
    load the animation
    """
    animation = '|/-\\'
    for _ in range(10):
        for c in animation:
            print(f'\rLoading {c}', end='')
            time.sleep(0.1)
        print('\n' * 100)

def intro():
    """
    Start the game
    """
    print('Welcome to the Guessing Game'.center(100, '-'))
    input('Press any key to continue --->')
    print('\n' * 100)
    loading_animation()
    display()

def display():
    com = random.randint(1, 50)
    print('You have only 5 chances to guess the number between 1 and 50.')
    for i in range(5):
        try:
            n = int(input('Enter your guess: '))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if n == com:
            print('Congratulations! You guessed it right.')
            break
        elif n < com:
            print("Too low.......")
        else:
            print("Too high.......")

        print(f'You have {4 - i} {"chance" if i < 4 else "chances"} left.\n')

    else:
        print(f'You lost! Better luck next time. The correct number was {com}.')

if __name__ == '__main__':
    print('\n' * 200)
    while True:
        intro()
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != 'yes':
            break
