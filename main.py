import pygame
import random
import math
import time

# importing data from config file
from config import *

# game starting
pygame.init()
# timer object for countdown
clock = pygame.time.Clock()
# screen size
screen = pygame.display.set_mode((1300, 900))

# starting position of player 1
player1X = 600
player1Y = 835

# starting position of player 2
player2X = 600
player2Y = 0

# changes in positions of players
player1X_change = 0
player1Y_change = 0
player2X_change = 0
player2Y_change = 0

# initialising the birds
birdImg = []
# birds X coordinate list
birdX = []
# birds Y coordinate list
birdY = []
birdY_change1 = []
birdX_change1 = []
birdY_change2 = []
birdX_change2 = []
# number of birds
no_of_birds = 3

i = 0
for i in range(no_of_birds):
    # loading bird image
    birdImg.append(pygame.image.load('Images/bird.png'))
    if i == 0:
        # coordinates of first bird
        birdX.append(20)
        birdY.append(264)
        birdX_change1.append(4)
        birdX_change2.append(4)
    if i == 1:
        # coordinates of second bird
        birdX.append(700)
        birdY.append(442)
        birdX_change1.append(9)
        birdX_change2.append(9)
    if i == 2:
        # coordinates of third bird
        birdX.append(300)
        birdY.append(609)
        birdX_change1.append(12)
        birdX_change2.append(12)

# initialising the hawks
hawkImg = []
# hawks X coordinate list
hawkX = []
# hawks Y coordinate list
hawkY = []
hawkY_change1 = []
hawkX_change1 = []
hawkY_change2 = []
hawkX_change2 = []
# number of hawks
no_of_hawks = 3

i = 0
for i in range(no_of_hawks):
    # loading image of hawk
    hawkImg.append(pygame.image.load('Images/hawk.png'))
    if i == 0:
        # coordinates of first hawk
        hawkX.append(500)
        hawkY.append(264)
        hawkX_change1.append(11)
        hawkX_change2.append(11)
    if i == 1:
        # coordinates of second hawk
        hawkX.append(8)
        hawkY.append(442)
        hawkX_change1.append(8)
        hawkX_change2.append(8)
    if i == 2:
        # coordinates of third hawk
        hawkX.append(1200)
        hawkY.append(609)
        hawkX_change1.append(4)
        hawkX_change2.append(4)


# print image of player1
def player1(x, y):
    screen.blit(player1Img, (x, y))


# print image of player2
def player2(x, y):
    screen.blit(player2Img, (x, y))


# print image of birds
def bird(x, y, i):
    screen.blit(birdImg[i], (x, y))


# print image of hawks
def hawk(x, y, i):
    screen.blit(hawkImg[i], (x, y))


# X coordinates of fixed obstacles
fixedobstaclesX = [
    150,
    450,
    750,
    1050,
    0,
    300,
    600,
    900,
    1200,
    150,
    450,
    750,
    1050,
    0,
    300,
    600,
    900,
    1200,
    ]

# Y coordinates of fixed obstacles
fixedobstaclesY = [
    134,
    134,
    134,
    134,
    306,
    306,
    306,
    306,
    306,
    478,
    478,
    478,
    478,
    650,
    650,
    650,
    650,
    650,
    ]


# print the images of fixed obstacles
def fixedObs():
    screen.blit(fixedImg, (150, 134))
    screen.blit(fixedImg, (450, 134))
    screen.blit(fixedImg, (750, 134))
    screen.blit(fixedImg, (1050, 134))
    screen.blit(fixedImg, (0, 306))
    screen.blit(fixedImg, (300, 306))
    screen.blit(fixedImg, (600, 306))
    screen.blit(fixedImg, (900, 306))
    screen.blit(fixedImg, (1200, 306))
    screen.blit(fixedImg, (150, 478))
    screen.blit(fixedImg, (450, 478))
    screen.blit(fixedImg, (750, 478))
    screen.blit(fixedImg, (1050, 478))
    screen.blit(fixedImg, (0, 650))
    screen.blit(fixedImg, (300, 650))
    screen.blit(fixedImg, (600, 650))
    screen.blit(fixedImg, (900, 650))
    screen.blit(fixedImg, (1200, 650))

# the line mark list to increase score
# for player 1
mark1 = [
    600,
    559,
    428,
    392,
    256,
    214,
    80,
    0,
    ]
# for player 2
mark2 = [
    204,
    270,
    396,
    460,
    588,
    656,
    785,
    900,
    ]
mark1pass = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    ]

mark2pass = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    ]


# collision detection for player1
def isCollision1(obstacleXX, obstacleYY, playerX, playerY):
    x1 = playerX + 32 - obstacleXX - 16
    y1 = playerY + 32 - obstacleYY - 16
    distance = math.sqrt(x1 * x1 + y1 * y1)
    if distance < 45:
        return True
    else:
        return False


# collision detection for player2
def isCollision2(obstacleXX, obstacleYY, playerX, playerY):
    x1 = playerX + 32 - obstacleXX - 16
    y1 = playerY + 32 - obstacleYY - 16
    distance = math.sqrt(x1 * x1 + y1 * y1)
    if distance < 45:
        return True
    else:
        return False


# collision of player1 with fixed obstacles
def isCollision1m(obstacleXX, obstacleYY, playerX, playerY):
    x1 = playerX + 32 - obstacleXX - 48
    y1 = playerY + 32 - obstacleYY - 48
    distance = math.sqrt(x1 * x1 + y1 * y1)
    if distance < 60:
        return True
    else:
        return False


# collision of player2 with fixed obstacles
def isCollision2m(obstacleXX, obstacleYY, playerX, playerY):
    x1 = playerX + 32 - obstacleXX - 48
    y1 = playerY + 32 - obstacleYY - 48
    distance = math.sqrt(x1 * x1 + y1 * y1)
    if distance < 60:
        return True
    else:
        return False


# score of player1
score1 = 0
# score of player2
score2 = 0


# function to display score of player1
def scoreDisplay1(s, l):
    score = font.render('PLAYER 1: ' + str(s), True, (0, 0, 0))
    screen.blit(score, (50, 840))
    score = font.render('LEVEL: ' + str(l), True, (0, 0, 0))
    screen.blit(score, (1050, 840))


# function to display score of player2
def scoreDisplay2(s, l):
    score = font.render('PLAYER 2: ' + str(s), True, (0, 0, 0))
    screen.blit(score, (50, 5))
    score = font.render('LEVEL: ' + str(l), True, (0, 0, 0))
    screen.blit(score, (1050, 5))


# running variable to keep running game
running = True

flag = 1

# current level of player1
player1_level = 1
# current level of player2
player2_level = 1

# speed of player1
speed1 = 0
# speed of player2
speed2 = 0

# score of player1
score1 = 0
# score of player2
score2 = 0

# game starts
while running:

    # to check if user has quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # fill screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (235, 237, 42), (0, 835, 1300, 65))
    pygame.draw.rect(screen, (235, 237, 42), (0, 0, 1300, 65))
    scoreDisplay1(score1, player1_level)
    scoreDisplay2(score2, player2_level)
    fixedObs()

    # player 1 plays the game
    if flag == 1:
        for i in range(no_of_birds):
            birdX[i] = birdX[i] + birdX_change1[i] + speed1
            if birdX[i] >= 1270:
                birdX[i] = 0
    else:

        for i in range(no_of_birds):
            birdX[i] = birdX[i] + birdX_change2[i] + speed2
            if birdX[i] >= 1270:
                birdX[i] = 0

    for i in range(no_of_hawks):
        hawkX[i] += hawkX_change1[i]
        if hawkX[i] >= 1270:
            hawkX[i] = 0
        bird(birdX[i], birdY[i], i)
        hawk(hawkX[i], hawkY[i], i)

    if flag == 1:

        score = font.render('START', True, (0, 0, 0))
        screen.blit(score, (580, 840))

        score = font.render('END', True, (0, 0, 0))
        screen.blit(score, (580, 5))

        player1(player1X, player1Y)

        # check keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1Y_change = -3.0

                i = 0
                for i in range(7):
                    if mark1pass[i] == 0:
                        if player1Y < mark1[i]:
                            if player1Y > mark1[i+1]:
                                score1 += 5
                                mark1pass[i] = 1
                                if i % 2 == 1:
                                    score1 += 5

            if event.key == pygame.K_DOWN:
                player1Y_change = 3.0
            if event.key == pygame.K_LEFT:
                player1X_change = -3.0
            if event.key == pygame.K_RIGHT:
                player1X_change = 3.0

        if event.type == pygame.KEYUP:
            player1X_change = 0
            player1Y_change = 0

        # new position of player 1
        player1X += player1X_change
        player1Y += player1Y_change

        if player1X <= 0:
            player1X = 0
        if player1X >= 1270:
            player1X = 1270

        i = 0
        for i in range(3):
            bx = birdX[i]
            by = birdY[i]
            hx = hawkX[i]
            hy = hawkY[i]
            pl = player1X
            py = player1Y

            collisionb = isCollision1(bx, by, pl, py)
            collisionh = isCollision1(hx, hy, pl, py)

            if collisionb or collisionh:
                flag = -1
                player1X = 600
                player1Y = 835
                j = 0
                for j in range(7):
                    mark1pass[j] = 0
                break

        i = 0
        for i in range(18):
            pl = player1X
            py = player1Y
            fx = fixedobstaclesX[i]
            fy = fixedobstaclesY[i]
            collisionm = isCollision1m(fx, fy, pl, py)
            if collisionm:
                flag = -1
                player1X = 600
                player1Y = 835
                j = 0
                for j in range(7):
                    mark1pass[j] = 0
                break

        # level up for player1
        if player1Y <= 25:
            player1_level += 1
            score1 += 50
            speed1 += 3
            flag = -1

            j = 0
            for j in range(7):
                mark1pass[j] = 0

            player1X = 600
            player1Y = 835

        player1(player1X, player1Y)

    # player 2 plays the game
    if flag == -1:

        score = font.render('END', True, (0, 0, 0))
        screen.blit(score, (580, 840))

        score = font.render('START', True, (0, 0, 0))
        screen.blit(score, (580, 5))

        player2(player2X, player2Y)

        # check key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player2Y_change = -3.0
            if event.key == pygame.K_s:
                player2Y_change = 3.0

                i = 0
                for i in range(7):
                    if mark2pass[i] == 0:
                        if player2Y > mark2[i]:
                            if player2Y < mark2[i + 1]:
                                mark2pass[i] = 1
                                score2 += 5
                                if i % 2 == 1:
                                    score2 += 5

            if event.key == pygame.K_a:
                player2X_change = -3.0
            if event.key == pygame.K_d:
                player2X_change = 3.0

        if event.type == pygame.KEYUP:
            player2X_change = 0
            player2Y_change = 0

        # new position of player 2
        player2X += player2X_change
        player2Y += player2Y_change

        if player2X <= 0:
            player2X = 0
        if player2X >= 1270:
            player2X = 1270

        i = 0
        for i in range(3):
            bx = birdX[i]
            by = birdY[i]
            hx = hawkX[i]
            hy = hawkY[i]
            pl = player2X
            py = player2Y

            collisionb = isCollision1(bx, by, pl, py)
            collisionh = isCollision1(hx, hy, pl, py)

            if collisionb or collisionh:
                flag = 1
                player2X = 600
                player2Y = 0

                j = 0
                for j in range(7):
                    mark2pass[j] = 0
                break

        i = 0
        for i in range(18):
            pl = player2X
            py = player2Y
            fx = fixedobstaclesX[i]
            fy = fixedobstaclesY[i]
            collisionm = isCollision1m(fx, fy, pl, py)
            if collisionm:
                flag = 1
                player2X = 600
                player2Y = 0

                j = 0
                for j in range(7):
                    mark2pass[j] = 0
                break

        # level up for player 2
        if player2Y >= 835:
            player2_level += 1
            score2 += 50
            speed2 += 3
            flag = 1

            player2X = 600
            player2Y = 0

            j = 0
            for j in range(7):
                mark2pass[j] = 0

        player2(player2X, player2Y)

    # countdown
    start -= 0.18
    # end the game if time is over
    if start <= 0:
        break

    if not running:
        break

    # print the time remaining
    score = font.render('Time left: ' + str(int(start / 10)), True, (0,
                        0, 0))
    screen.blit(score, (13, 62))

    clock.tick(100)
    pygame.display.update()

# time over
# decide winner of the game
winner = 1
if score2 > score1:
    winner = 2
elif score1 == score2:
    if player2_level > player1_level:
        winner = 2

while running:

    # quit if user closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # fill the screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # print the winner, if any
    if (score1 != score2 or player1_level != player2_level):
        score = font2.render(cong, True, (103, 16, 143))
        screen.blit(score, (335, 150))
        score = font2.render('PLAYER ' + str(winner) + ' WON !!', True,
                             (103, 16, 143))
        screen.blit(score, (375, 250))
    # else print MATCH TIED
    else:
        score = font2.render("MATCH TIED", True, (103, 16, 143))
        screen.blit(score, (450, 250))

    # print final scores of both players
    score = font.render(fin, True, (0, 0, 0))
    screen.blit(score, (525, 410))

    # final score of player1
    score = font.render('PLAYER 1: ' + str(score1), True, (0, 0, 0))
    screen.blit(score, (525, 485))

    # final score of player2
    score = font.render('PLAYER 2: ' + str(score2), True, (0, 0, 0))
    screen.blit(score, (525, 550))

    pygame.display.update()
# game ends
