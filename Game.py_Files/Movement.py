import pygame
import random


# Initialise pygame and create window
from Setting import Width, Height, FPS, BLACK

pygame.init()
pygame.mixer.init()
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Slime EVO")
Clock = pygame.time.Clock()

# Game Loop
Running = True
while Running:
    # Keep loop running at the right speed
    Clock.tick(FPS)
    # Process Input (Events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            Running = False

    # Update
    all.sprites.update()

    #Draw / Render
    Screen.fill(BLACK)
    all.sprites.draw(Screen)
    # After It has drawn everything, flips the display
    pygame.display.flip()

pygame.quit()
