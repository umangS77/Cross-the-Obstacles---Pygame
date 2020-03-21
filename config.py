import pygame
import random
pygame.init()
# image for fixed obstacles
fixedImg = pygame.image.load('Images/fixed.png')
# image for background
background = pygame.image.load('Images/back.jpg')
# images for players
player1Img = pygame.image.load('Images/player1Img.png')
player2Img = pygame.image.load('Images/player2Img.png')
# caption for the game
pygame.display.set_caption("Cross the Obstacles")
# setting the fonts
font = pygame.font.Font('Charnego.otf', 50)
font2 = pygame.font.Font('Charnego.otf', 100)
# final messages
cong = "CONGRATULATIONS"
fin = "FINAL SCORES:"
# time for which game will run
time = 305
start = time
