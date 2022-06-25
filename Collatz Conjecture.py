from math import sqrt
import random
import sys
import pygame
pygame.init()
clock = pygame.time.Clock()


# Fonts and colors
bColor = (44, 47, 51)
blColor1 = (114, 137, 218)
blColor2 = (114, 137, 218)
blColor3 = (114, 137, 218)
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
col_inp = False


# Screen
screen = pygame.display.set_mode((800, 875))
pygame.display.set_caption('Collatz Conjecture')
screen.fill(bColor)


# Text setup
input_a = pygame.Rect((30, 30), (745, 40))
mButton = pygame.Rect((675, 30), (100, 40))
gRect = pygame.Rect((45, 80), (705, 705))
opt1 = pygame.Rect((50, 795), (100, 40))
opt2 = pygame.Rect((180, 795), (100, 40))


# Functions
# Check if the pressed button is a number
def isNum(char):
    for i in range(47, 58):
        if char == i: return True
    for i in range(1073741913, 1073741923):
        if char == i: return True
    return False

# Take int and distribute accordingly
def startCalc(num):
    # List the conjecture
    numList = [num]
    oddList = list()
    evenList = list()
    c = 0
    while num != 1:
        c += 1
        if num % 2 == 0:
            num = int(num / 2)
            numList.append(num)
            evenList.append(num)
        else:
            num = 3 * num + 1
            numList.append(num)
            oddList.append(num)
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
    pygame.draw.rect(screen, blColor1, mButton)
    screen.blit((sFont1.render('Enter', False, (0, 0, 0))), (700, 33))
    # Graph
    pygame.draw.rect(screen, gColor, gRect)
    # Option buttons
    pygame.draw.rect(screen, blColor2, opt1)
    screen.blit((sFont2.render('Prime #s', False, (0, 0, 0))), (60, 800))
    pygame.draw.rect(screen, blColor3, opt2)
    screen.blit((sFont2.render('Option 2', False, (0, 0, 0))), (190, 800))
    screen.blit((sFont2.render('Drag over a portion of the graph to zoom in', False, (100, 100, 100))), (300, 800))


    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # BDOWN
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Input
            if input_a.collidepoint(event.pos):
                col_inp = True
                rColor = (210, 210, 230)
                if numT == 'Type a positive integer...': numT = ''
            else:
                col_inp = False
                rColor = (230, 230, 230)
            # Enter button
            if mButton.collidepoint(event.pos):
                blColor1 = (124, 137, 228)
                if numT == 'Type a positive integer...' or numT == '':
                    numT = random.randint(1, sys.maxsize)
                startCalc(int(numT))
            else:
                blColor1 = (114, 137, 218)
            # Option 1
            if opt1.collidepoint(event.pos):
                blColor2 = (200, 97, 118)
            else:
                blColor2 = (124, 137, 228)
            # Option 2
            if opt2.collidepoint(event.pos):
                blColor3 = (200, 97, 118)
            else:
                blColor3 = (114, 137, 218)
        # Type
        elif event.type == pygame.KEYDOWN:
            if col_inp:
                if event.key == pygame.K_BACKSPACE:
                    numT = numT[:-1]
                else:
                    if isNum(event.key):
                        numT += event.unicode

        # Clock
        pygame.display.flip()
        clock.tick(60)