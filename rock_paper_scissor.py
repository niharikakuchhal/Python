"""
    Rock,Paper & Scissor
"""
import os
import random 
import pygame
from PIL import Image

def game():
    pygame.init()
    pygame.mixer.init()

    choices = ['Rock','Paper','Scissors']
    print('0 - Rock, 1 - Paper, 2- Scissor')
    player = int(input("Enter the choice: "))
    com = random.randint(0,2)
    print(f'Computer choice : {choices[com]}')

    # Display pictures for choices
    display_choices(choices[player], choices[com])

    # Play sound effects
    win_sound = pygame.mixer.Sound('win.mp3')
    lose_sound = pygame.mixer.Sound('lose.mp3')
    tie_sound = pygame.mixer.Sound('tie.mp3')

    if (player == 0 and com == 1) or (player == 1 and com == 2) or (player == 2 and com == 0):
        lose_sound.play()
        return 'Computer Win' 
    elif (player == 1 and com == 0) or (player == 2 and com == 1) or (player == 0 and com == 2):
        win_sound.play()
        return 'Player Win'
    else:
        tie_sound.play()
        return "It's a tie"
    

def display_choices(player,com):
    img_folder = 'images/'
    images = {
        'Rock': 'rock.png',
        'Paper': 'paper.jpeg',
        'Scissors': 'scissor.png',
    }

    player_img_path = os.path.join(img_folder, images[player])
    com_img_path = os.path.join(img_folder, images[com])

    player_img = Image.open(player_img_path)
    com_img = Image.open(com_img_path)

    # Display images side by side
    img_width = player_img.width + com_img.width
    img_height = max(player_img.height, com_img.height)
    combined_img = Image.new('RGB', (img_width, img_height))
    combined_img.paste(player_img, (0, 0))
    combined_img.paste(com_img, (player_img.width, 0))

    combined_img.show()

if __name__ == '__main__':
    os.system('cls')
    print('Rock, Paper & Scissor')
    input('Press any key...')
    print('You have 3 chances...')
    for i in range(3):
        r = game()
        print(r)
        user = input('You want to replay (yes/no): ')
        if user == 'no':
            break

