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

# Floors boxes [x, y, width, height]
class Floors:
    def __init__(self):
        self.FloorsLocation = ([0, 393, 201, 20], [193, 400, 20, 20], [203, 414, 20, 20], [215, 423, 20, 20],
                               [230, 430, 135, 20], [358, 423, 20, 20], [373, 410, 20, 20], [383, 397, 20, 20],
                               [395, 393, 190, 20], [544, 369, 190, 30], [646, 345, 161, 30], [0, 0, 0, 0])
        self.image = pygame.Surface([width, height])
        self.image.get_rect()

    def draw(self):

        for i in xrange(0, 12):
            self.boxes = pygame.draw.rect(background, black, (self.FloorsLocation[i]))
            self.rect = pygame.Rect(self.boxes)

    def check_for_collisions(self, spriteRect):
        for i in xrange(0, 12):
            if check_collision(spriteRect, Rect(self.FloorsLocation[i])) == True:
                #print "Colliding with" + str(self.FloorsLocation[i])
                return True
        return False

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


    def Draw(self):
        DISPLAYSURF.blit(self.sprite, (self.xPosition, self.yPosition))
        #pygame.draw.rect(DISPLAYSURF, (255, 43, 55), self.rect)

    def Update(self):

        self.rect.x = self.xPosition
        self.rect.y = self.yPosition
        keys_pressed = pygame.key.get_pressed()

        if self.rect.x and self.xPosition > width:
            self.rect.x = width
            self.xPosition = width

        self.yPosition += 2

        collide = Floors.check_for_collisions(self.rect)
        if collide == True:
            self.yPosition = Floors.rect.top


        #pygame.draw.rect(background, white, (self.xPosition, self.yPosition, 35, 35))
        if keys_pressed[K_LEFT]:
                self.sprite = pygame.image.load('Slimeleft.png')
                self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
                self.xPosition -= 0.6

                collide = Floors.check_for_collisions(self.rect)
                if collide == True:
                    if self.xPosition < 0:
                        self.rect.left = Floors.rect.left


        elif keys_pressed[K_RIGHT]:

            self.sprite = pygame.image.load('Slimeright.fw.png')
            self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
            self.xPosition += 2

            collide = Floors.check_for_collisions(self.rect)
            if collide == True:
                if self.xPosition > 0:
                    self.rect.right = Floors.rect.left

        elif keys_pressed[K_UP]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (25, 25), )
            if self.jumpSpeed == 0:
                self.jumpSpeed = 10
            else:
                self.jumpSpeed -= 0.6
            self.yPosition -= self.jumpSpeed

            collide = Floors.check_for_collisions(self.rect)
            if collide == True:
                self.jumpSpeed = 0
                if self.yPosition < 0:
                    self.rect.bottom = Floors.rect.top


        elif keys_pressed[K_DOWN]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (25, 25), )
            self.yPosition += 2







#while self.boudarylocation == self.rect
            #if keys_pressed[K_SPACE]:
            #if pygame.key.set_repeat(1, 1):
            #   movey = -4
            #  sprite_state = 'JUMPING'

DOWN ='down'
direction=DOWN
velocity = 0
movex = 0
movey = 0
sprite_state = 'RESTING'
Slime = Slime()

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




            #if event.type==KEYUP:
            #   if event.key==K_SPACE:
            #      if movey >= 5:
            #         for x in range(5, 0, -1):
            #            spritey = +1



    '''spritey+=movey


    if (movey < 0 and sprite_state == 'JUMPING'):
        movey += 0.1
    elif(sprite_state == 'JUMPING' and movey >= 0 ):
        sprite_state = 'FALLING'

    if (sprite_state == 'FALLING'):
        movey += 0.1

    if(sprite_state == 'FALLING' and movey >= 4 ):  # hits a platform
        sprite_state = 'RESTING'
        movey = 0.0

    # movey - converge to 0
    print sprite_state
    print movey'''



    pygame.display.update()
    fpsClock.tick(FPS)