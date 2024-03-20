import pygame

# define background color
background_color = (0,0,255)

# define screen size
screen = pygame.display.set_mode((800, 600))

# set the caption / title
pygame.display.set_caption("Battleship AI")

# fill the screen with bgc
screen.fill(background_color)

# update display using flip
pygame.display.flip()

# variable to keep game / window open / running
running = True

# loop game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.init()