import random
import sys
import pygame
from pygame.locals import*  # import basic pygames



# global variables used in the entire game
fps = 60
screenwidth = 400
screenheight = 800
screen = pygame.display.set_mode((screenwidth, screenheight))
ground = screenheight*0.8
game_sprites = {}
game_sounds = {}
player = 'assets/Sprites/bluebird-midflap.png'
background = 'assets/Sprites/background-day.png'
pipe = 'assets/Sprites/pipe-green.png'

def welcomeScreen():

    #IT WIll Show Welcome Screen TO user to make the game more interactive and interesting
    playerx = int(screenwidth/5)
    playery = int(screenheight - game_sprites['player'].get_height())/2
    messagex = int(screenwidth - game_sprites['message'].get_width())/2
    messagey = int(screenheight * 0.13)
    basex = 0
    playbutton = pygame.Rect(108,222,68,65)
    while True:
        for event in pygame.event.get():
             #If user clicks on Cross or presses the Escape button Close the Game
            if event.type== QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            
            #This will make the cursor to arrow again if we move out our cursor from playbutton
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if pygame.mouse.get_pos()[0] > playbutton[0]  and pygame.mouse.get_pos()[0] < playbutton[0] + playbutton[2]:
                if pygame.mouse.get_pos()[1] > playbutton[1]  and pygame.mouse.get_pos()[1] < playbutton[1] + playbutton[3]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else :
                screen.blit(game_sprites['background'],(0,0))
                screen.blit(game_sprites['player'],(playerx,playery))
                screen.blit(game_sprites['message'],(messagex,messagey))
                screen.blit(game_sprites['base'],(basex,ground))
                pygame.display.update()
                FPSCLOCK.tick(fps)

# the real game coding starts from here

if __name__ == "__main__":
    pygame.init()  # initializing pygame
    fpslock = pygame.time.Clock
    pygame.display.set_caption('Flappy Bird With Mr.Junki')

# loading the score

    game_sprites['numbers'] = (
        pygame.image.load('assets/Sprites/0.png').convert_alpha(),
        pygame.image.load('assets/Sprites/1.png').convert_alpha(),
        pygame.image.load('assets/Sprites/2.png').convert_alpha(),
        pygame.image.load('assets/Sprites/3.png').convert_alpha(),
        pygame.image.load('assets/Sprites/4.png').convert_alpha(),
        pygame.image.load('assets/Sprites/5.png').convert_alpha(),
        pygame.image.load('assets/Sprites/6.png').convert_alpha(),
        pygame.image.load('assets/Sprites/7.png').convert_alpha(),
        pygame.image.load('assets/Sprites/8.png').convert_alpha(),
        pygame.image.load('assets/Sprites/9.png').convert_alpha(),
    )
    game_sprites['background'] = pygame.image.load(background).convert_alpha
    game_sprites['player'] = pygame.image.load(player).convert_alpha
    game_sprites['message'] = pygame.image.load(
        'assets/Sprites/message.png').convert_alpha
    game_sprites['base'] = pygame.image.load(
        'assets/Sprites/base.png').convert_alpha
    game_sprites['pipe'] = (pygame.transform.rotate(pygame.image.load(
        pipe).convert_alpha(), 180), pygame.image.load(pipe).convert_alpha())

    #game sound system

    game_sounds['die'] = pygame.mixer.Sound('assets/Audio/die.wav')
    game_sounds['hit'] = pygame.mixer.Sound('assets/Audio/hit.wav')
    game_sounds['point'] = pygame.mixer.Sound('assets/Audio/point.wav')
    game_sounds['swoosh'] = pygame.mixer.Sound('assets/Audio/swoosh.wav')
    game_sounds['wing'] = pygame.mixer.Sound('assets/Audio/wing.wav')

while True:
    welcomeScreen() # Start Screen for the user
    mainGame()

