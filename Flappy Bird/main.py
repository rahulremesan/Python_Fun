import random
import sys
import pygame
from pygame.locals import * #import basic pygames


#global variables used in the entire game
fps = 60
screenwidth = 300
screenheight = 500
screen = pygame.display.set_mode((screenwidth, screenheight))
ground = screenheight*0.8
game_sprites = {}
game_sounds = {}
player = '../assets/bluebird-midflap.png'
background =  '../assets/background-day.png'
pipe = '../assets/pipe-green.png'

