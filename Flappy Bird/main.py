import random
import sys
import pygame
from pygame.locals import * #import basic pygames


#global variables used in the entire game
fps = 60
screenwidth = 400
screenheight = 800
screen = pygame.display.set_mode((screenwidth, screenheight))
ground = screenheight*0.8
game_sprites = {}
game_sounds = {}
player = 'assets/Sprites/bluebird-midflap.png'
background =  'assets/Sprites/background-day.png'
pipe = 'assets/Sprites/pipe-green.png'

#the real game coding starts from here

if __name__ == "__main__":
    pygame.init() #initializing pygame 
    fpslock = pygame.time.Clock
    pygame.display.set_caption('Flappy Bird With Mr.Junki')

#loading the score

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
