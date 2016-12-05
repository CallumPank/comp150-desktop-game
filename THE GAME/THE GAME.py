import pygame, sys, time, os
from pygame.locals import *


pygame.init()

black = (0, 0, 0)
alpha = ()
FPS = 90
fpsClock = pygame.time.Clock()

# Display window
width = 807
height = 489
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Slime Evo')
background = pygame.image.load ('Bridge.png')
collide = False

# Collision rectangles class
class Floors:
    def __init__(self):
        #[x, y, width, height] for rectangles
        self.FloorsLocation = ([0, 393, 201, 20], [193, 400, 20, 20], [203, 414, 20, 20], [215, 423, 20, 20],
                               [230, 430, 135, 20], [358, 423, 20, 20], [373, 410, 20, 20], [383, 397, 20, 20],
                               [395, 393, 190, 20], [544, 369, 190, 30], [646, 345, 161, 30], [0, 280, 0, 0])
        self.image = pygame.Surface([width, height])
        self.image.get_rect()

    def draw(self):
        # Draw the rectangles
        for i in xrange(0, 12):
            self.boxes = pygame.draw.rect(DISPLAYSURF, black, (self.FloorsLocation[i]))
            self.rect = pygame.Rect(self.boxes)

    #Check for collision between rectangles and sprite
    def check_for_collisions(self, spriteRect):
        for i in xrange(0, 12):
            if check_collision(spriteRect, Rect(self.FloorsLocation[i])) == True:
                return True
        return False

#Defines check_collision
def check_collision(collider, colliding):
    return collider.colliderect(colliding)

Floors = Floors()

# Sprite class
class Slime(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.image.load('SlimeR.png')
        self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
        self.xPosition = 25
        self.yPosition = 350
        self.jumpSpeed = 0
        self.rect = self.sprite.get_rect()

# Keeps sprite in window by not allowing the spite to pass the x, y values of the window
    def outOFbounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > height:
            self.rect.bottom = height

    # Draw the sprite
    def Draw(self):
        DISPLAYSURF.blit(self.sprite, (self.xPosition, self.yPosition))

    def Update(self):
        # Defines what key pressed and current location of sprite
        self.rect.x = self.xPosition
        self.rect.y = self.yPosition
        keys_pressed = pygame.key.get_pressed()

        # Gravity
        self.yPosition += 5

        # Checks for collision
        collide = Floors.check_for_collisions(self.rect)
        if collide == True:
            self.yPosition = Floors.rect.top

        # Defines what happens when the arrow keys are pressed
        if keys_pressed[K_LEFT]:
                self.sprite = pygame.image.load('Slimeleft.png')
                self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
                self.xPosition -= 2

        elif keys_pressed[K_RIGHT]:

            self.sprite = pygame.image.load('Slimeright.fw.png')
            self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
            self.xPosition += 2

        elif keys_pressed[K_UP]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
            if self.jumpSpeed == 0:
                self.jumpSpeed = 10
            else:
                self.jumpSpeed -= 0.6
            self.yPosition -= self.jumpSpeed

Slime = Slime()

# Game loop
while True:
    Floors.draw()
    DISPLAYSURF.blit(background, (0, 0))
    Slime.outOFbounds()
    Slime.Draw()
    Slime.Update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()