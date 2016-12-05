import pygame, sys, time, os
from pygame.locals import *


pygame.init()

black = (0, 0, 0)
FPS=90
fpsClock=pygame.time.Clock()

# Display window
width=816
height=437
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Slime Evo')
background=pygame.image.load ('Black & White Level Design.png')
collide = False

global splitstate
splitstate = 0
print splitstate
global slime1
slime1 = pygame.image.load('Slimeleft.png')
global slime2
slime2 = pygame.image.load('Slimeleft.png')
# Floors boxes
class Floors:
    def __init__(self):
        self.FloorsLocation = ([0, 375, 81, 62], [0, 0, 40, 400], [35, 125, 407, 42], [81, 0, 416, 84], [483, 84, 14, 138], [81, 208, 405, 14], [81, 210, 14, 123],
            [81, 319, 347, 14], [123, 375, 41, 62], [207, 375, 41, 62], [289, 375, 42, 62], [497, 0, 319, 14], [497, 194, 70, 28], [552, 219, 15, 114], [567, 319, 180, 14],
            [137, 263, 374, 15], [470, 275, 41, 102], [372, 375, 181, 62], [540, 388, 27, 49], [560, 416, 170, 21], [719, 388, 98, 49], [733, 375, 83, 18], [788, 55, 29, 350],
            [539, 55, 42, 98], [622, 55, 14, 90], [678, 55, 13, 90], [733, 55, 14, 90], [580, 139, 220, 14], [608, 150, 200, 128])

    def Draw(self):
        for i in xrange(0, 29):
            self.boxes = pygame.draw.rect(background, black,(self.FloorsLocation[i]))

            self.rect = pygame.Rect(self.boxes)

    def check_for_collisions(self, spriteRect):
        for i in xrange(0, 29):
            if check_collision(spriteRect, Rect(self.FloorsLocation[i])) == True:
                print "Colliding with" + str(self.FloorsLocation[i])
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
        self.xPosition = 45
        self.yPosition = 10
        self.rect = self.sprite.get_rect()
        self.spawn = False
        # compare lime to floor[i]

    def Split(self):
        # Split state 0 = Has not split/is one whole slime. Split state 1 = Has split and cannot split further currently.
        speed = 0.5
        # Returns information on whether or not the user has split yet
    # Changes the split_state appropriately.

    def set_split_state(self):
        Splitstate = 0
        if self.get_split_state() == 0:
            slime2.xP = slime2.xP - slime1.xP * speed
            slime2.yP = slime2.yP - slime1.yP * speed
            Splistate = 1
        else:
            Splistate = 0

    def get_split_state(self):
        return splitstate

    def Draw(self):
        DISPLAYSURF.blit(self.sprite, (self.xPosition, self.yPosition))
        pygame.draw.rect(DISPLAYSURF, (255, 43, 55), self.rect)

    def Update(self):

        self.rect.x = self.xPosition
        self.rect.y = self.yPosition


        keys_pressed = pygame.key.get_pressed()
        # pygame.draw.rect(background, white, (self.xPosition, self.yPosition, 35, 35))
        if keys_pressed[K_LEFT]:
            self.sprite = pygame.image.load('Slimeleft.png')
            self.sprite = pygame.transform.scale(self.sprite, (35, 35), )
            self.xPosition -= 2
        elif keys_pressed[K_RIGHT]:
            self.sprite = pygame.image.load('Slimeright.fw.png')
            self.sprite = pygame.transform.scale(self.sprite, (35, 35), )
            self.xPosition += 2
        elif keys_pressed[K_UP]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
            self.yPosition -= 2
        elif keys_pressed[K_DOWN]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
            self.yPosition += 2
        else:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (30, 30), )
        if keys_pressed[K_i]:
            if self.spawn:
                Slime2.xPosition = 5000
                Slime2.yPosition = 5000
                self.spawn = False
            else:
                Slime2.xPosition = self.xPosition
                Slime2.yPosition = self.yPosition
                self.spawn = True
                # Slime.set_split_state()
                # print Slime.get_split_state()

        class Slime2(pygame.sprite.Sprite):
            def __init__(self):
                self.sprite2 = pygame.image.load('SlimeR.png')
                self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
                self.xPosition = Slime.xPosition
                self.yPosition = Slime.yPosition
                self.rect = self.sprite2.get_rect()

            def Draw(self):
                DISPLAYSURF.blit(self.sprite2, (self.xPosition, self.yPosition))

            def Update(self):
                keys_pressed = pygame.key.get_pressed()
                # pygame.draw.rect(background, white, (self.xPosition, self.yPosition, 35, 35))
                if keys_pressed[K_a]:
                    self.sprite2 = pygame.image.load('Slimeleft.png')
                    self.sprite2 = pygame.transform.scale(self.sprite2, (35, 35), )
                    self.xPosition -= 2
                elif keys_pressed[K_d]:
                    self.sprite2 = pygame.image.load('Slimeright.fw.png')
                    self.sprite2 = pygame.transform.scale(self.sprite2, (35, 35), )
                    self.xPosition += 2
                elif keys_pressed[K_w]:
                    self.sprite2 = pygame.image.load('SlimeR.png')
                    self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
                    self.yPosition -= 2
                elif keys_pressed[K_s]:
                    self.sprite2 = pygame.image.load('SlimeR.png')
                    self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
                    self.yPosition += 2
                else:
                    self.sprite2 = pygame.image.load('SlimeR.png')
                    self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )


                collide = Floors.check_for_collisions(self.rect)
                if collide == True:
                    self.xPosition += 4
                    if self.xPosition < 0:
                        self.rect.left = Floors.rect.left

            collide = Floors.check_for_collisions(self.rect)
            if collide == True:
                self.xPosition -= 4
                if self.xPosition > 0:
                    self.rect.right = Floors.rect.left

            collide = Floors.check_for_collisions(self.rect)
            if collide == True:
                self.yPosition += 4
                if self.yPosition < 0:
                    self.rect.top = Floors.rect.bottom

        if keys_pressed[K_i]:
            if self.spawn:
                Slime2.xPosition = 5000
                Slime2.yPosition = 5000
                self.spawn = False
            else:
                Slime2.xPosition = self.xPosition
                Slime2.yPosition = self.yPosition
                self.spawn = True

            if Floors.check_for_collisions(self.rect) == True:
                self.yPosition -= 4
                if self.yPosition > 0:
                    self.rect.bottom = Floors.rect.top

class Slime2(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite2 = pygame.image.load('SlimeR.png')
        self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
        self.xPosition = Slime.xPosition
        self.yPosition = Slime.yPosition
        self.rect = self.sprite2.get_rect()
    def Draw(self):
        DISPLAYSURF.blit(self.sprite2, (self.xPosition, self.yPosition))
    def Update(self):
        keys_pressed = pygame.key.get_pressed()
        # pygame.draw.rect(background, white, (self.xPosition, self.yPosition, 35, 35))
        if keys_pressed[K_a]:
            self.sprite2 = pygame.image.load('Slimeleft.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (35, 35), )
            self.xPosition -= 2
        elif keys_pressed[K_d]:
            self.sprite2 = pygame.image.load('Slimeright.fw.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (35, 35), )
            self.xPosition += 2
        elif keys_pressed[K_w]:
            self.sprite2 = pygame.image.load('SlimeR.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
            self.yPosition -= 2
        elif keys_pressed[K_s]:
            self.sprite2 = pygame.image.load('SlimeR.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
            self.yPosition += 2
        else:
            self.sprite2 = pygame.image.load('SlimeR.png')
            self.sprite2 = pygame.transform.scale(self.sprite2,(30,30), )

Slime = Slime()
Slime2 = Slime2()
Floors = Floors()

while True:
    DISPLAYSURF.blit(background,(0,0))
    Floors.Draw()
    Slime.Draw()
    Slime.Update()
    Slime2.Draw()
    Slime2.Update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)