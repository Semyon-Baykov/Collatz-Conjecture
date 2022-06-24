from math import sqrt
import random
import sys
import pygame
pygame.init()
clock = pygame.time.Clock()


# Fonts and colors
bColor = (44, 47, 51)
blColor = (114, 137, 218)
rColor = (230, 230, 230)
gColor = (255, 255, 255)

bfont = pygame.font.Font(None, 18)

if 'impact' in pygame.font.get_fonts(): sFont1 = pygame.font.SysFont('impact', 25)
else: sFont1 = pygame.font.SysFont('Arial', 28)

if 'comicsansms' in pygame.font.get_fonts(): sFont2 = pygame.font.SysFont('comicsansms', 18)
else: sFont2 = pygame.font.SysFont('Arial', 24)


# Vars used in game
numT = 'Type a positive integer...'
num = 1
collided = False
wrongNum1 = False


# Screen
screen = pygame.display.set_mode((800, 875))
pygame.display.set_caption('Collatz Conjecture')
screen.fill(bColor)


# Text setup
input_a = pygame.Rect((30, 30), (745, 40))
mButton = pygame.Rect((675, 30), (100, 40))
gRect = pygame.Rect((45, 80), (705, 705))
opt1 = pygame.Rect((50, 720), (100, 40))


# Functions
# Check if the pressed button is a number
def isNum(char):
    for i in range(48, 57):
        if char == i: return True
    for i in range(1073741913, 1073741922):
        if char == i: return True
    return False

# Take int and distribute accordingly
def startCalc(num):
    # List the conjecture
    numList = [num]
    c = 0
    while num != 1:
        c += 1
        if num % 2 == 0:
            num = int(num / 2)
            numList.append(num)
        else:
            num = 3 * num + 1
            numList.append(num)
    # Find stats
    primeList = list()
    for i in numList:
        primeList.append(bool(isPrime(i)))

# Check if prime
def isPrime(num):
    if num == 1: return True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True



pygame.display.flip()
while True:
    # Input box
    pygame.draw.rect(screen, rColor, input_a)
    screen.blit((sFont2.render(numT, False, (0, 0, 0))), (35, 35))
    # Main Button
    pygame.draw.rect(screen, blColor, mButton)
    screen.blit((sFont2.render('Enter', False, (0, 0, 0))), (704, 35))
    # Graph
    pygame.draw.rect(screen, gColor, gRect)
    # Option buttons
    pygame.draw.rect(screen, blColor, opt1)


    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # BDOWN
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Input
            if input_a.collidepoint(event.pos):
                rColor = (210, 210, 230)
                numT = ''
                collided = True
            else:
                rColor = (230, 230, 230)
                collided = False
            # Button
            if mButton.collidepoint(event.pos):
                blColor = (124, 137, 228)
                if numT == 'Type a positive integer...' or numT == '':
                    numT = random.randint(1, sys.maxsize)
                startCalc(numT)
            else:
                blColor = (114, 137, 218)
        # Type
        elif event.type == pygame.KEYDOWN:
            if collided:
                if event.key == pygame.K_BACKSPACE:
                    numT = numT[:-1]
                else:
                    if isNum(event.key):
                        numT += event.unicode

        # Misc events
        if wrongNum1: screen.blit((sFont2.render('< Please type an integer first!', False, (200, 0, 0))), (169, 135))
        else: screen.blit((sFont2.render('', False, (200, 0, 0))), (169, 135))

        # Clock
        pygame.display.flip()
        clock.tick(60)