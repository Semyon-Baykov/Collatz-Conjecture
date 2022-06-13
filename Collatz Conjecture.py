import pygame
pygame.init()

bColor = (44, 47, 51)
screen = pygame.display.set_mode((800, 1000))

font1 = pygame.font.SysFont('Arial', 24)
font2 = pygame.font.SysFont('Arial', 10)

titleText = font1.render('Welcome to the Collatz Conjecture visualizer, input the starting number:', False, (255, 255, 255))

pygame.display.set_caption('Collatz Conjecture')
screen.fill(bColor)

pygame.display.flip()
while True:
    screen.blit(titleText, (30, 42))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        pygame.display.update()