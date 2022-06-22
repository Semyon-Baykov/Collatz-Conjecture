import pygame
pygame.init()
clock = pygame.time.Clock()


# Fonts and colors
bColor = (44, 47, 51)
rColor = (230, 230, 230)

bfont = pygame.font.Font(None, 18)

if 'impact' in pygame.font.get_fonts(): sFont1 = pygame.font.SysFont('impact', 25)
else: sFont1 = pygame.font.SysFont('Arial', 28)

if 'comicsansms' in pygame.font.get_fonts(): sFont2 = pygame.font.SysFont('comicsansms', 18)
else: sFont2 = pygame.font.SysFont('Arial', 24)


# Vars used in game
numT = 'Type an integer'
num = 1
collided = False


# Screen
screen = pygame.display.set_mode((800, 1000))
pygame.display.set_caption('Collatz Conjecture')
screen.fill(bColor)


# Text setup
titleText = sFont1.render('Welcome to the Collatz Conjecture visualizer, input the starting number:', False, (255, 255, 255))
input_a = pygame.Rect((30, 80), (745, 40))


# Functions
def isNum(char):
    for i in range(48, 57):
        if char == i: return True
    for i in range(1073741913, 1073741922):
        if char == i: return True
    return False



pygame.display.flip()
while True:
    # Title
    screen.blit(titleText, (30, 42))
    # Input box
    pygame.draw.rect(screen, rColor, input_a)
    surf_a = sFont2.render(numT, False, (0, 0, 0))
    screen.blit(surf_a, (35, 85))


    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # BDOWN
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_a.collidepoint(event.pos):
                rColor = (210, 210, 230)
                numT = ''
                collided = True
            else:
                rColor = (230, 230, 230)
                collided = False
        # Type
        elif event.type == pygame.KEYDOWN:
            if collided:
                if event.key == pygame.K_BACKSPACE:
                    numT = ''
                else:
                    if isNum(event.key):
                        numT += event.unicode


        pygame.display.flip()
        clock.tick(60)