import pygame, sys
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
global splitstate
splitstate = 0
print splitstate
global slime1
slime1 = pygame.image.load('Slimeleft.png')
global slime2
slime2 = pygame.image.load('Slimeleft.png')
collide = False

# Floors boxes [x, y, width, height]
class Floors:
    def __init__(self):
        self.FloorsLocation = ([0, 393, 201, 20], [193, 400, 20, 20], [203, 414, 20, 20], [215, 423, 20, 20],
                               [230, 430, 135, 20], [358, 423, 20, 20], [373, 410, 20, 20], [383, 397, 20, 20],
                               [395, 393, 190, 20], [544, 369, 190, 30], [646, 345, 161, 30], [0, 345, 160, 20])
        self.image = pygame.Surface([width, height])
        self.image.get_rect()

    def draw(self):

        for i in range(0, 12):
            self.boxes = pygame.draw.rect(DISPLAYSURF, black, (self.FloorsLocation[i]))
            self.rect = pygame.Rect(self.boxes)

    # This code checks for a collision between the player and the walls/floors.
    def check_for_collisions(self, spriteRect):
        for i in xrange(0, 12):
            if check_collision(spriteRect, Rect(self.FloorsLocation[i])) == True:
                print "Colliding with" + str(self.FloorsLocation[i])
                return True
        return False

#This code creates the check for a collision between the player and the walls/floors
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
        self.spawn = False

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




    def Update(self):

        self.rect.x = self.xPosition
        self.rect.y = self.yPosition


        if self.rect.x and self.xPosition > width:
            self.rect.x = width
            self.xPosition = width

        self.yPosition += 3

        collide = Floors.check_for_collisions(self.rect)
        if collide == True:
            self.yPosition = Floors.rect.top

    def Draw(self):
        DISPLAYSURF.blit(self.sprite, (self.xPosition, self.yPosition))
        # pygame.draw.rect(DISPLAYSURF, (255, 43, 55), self.rect)
        keys_pressed = pygame.key.get_pressed()
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
                    self.yPosition = 0

        elif keys_pressed[K_i]:
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
        self.jumpSpeed = 0
        self.rect = self.sprite2.get_rect()
    def Draw(self):
        DISPLAYSURF.blit(self.sprite2, (self.xPosition, self.yPosition))
    def Update(self):
        keys_pressed = pygame.key.get_pressed()
        # pygame.draw.rect(background, white, (self.xPosition, self.yPosition, 35, 35))
        self.rect.x = self.xPosition
        self.rect.y = self.yPosition

        if self.rect.x and self.xPosition > width:
            self.rect.x = width
            self.xPosition = width

        self.yPosition += 3

        collide = Floors.check_for_collisions(self.rect)
        if collide == True:
            self.yPosition = Floors.rect.top
        if keys_pressed[K_a]:
            self.sprite2 = pygame.image.load('Slimeleft.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
            self.xPosition -= 2
        elif keys_pressed[K_d]:
            self.sprite2 = pygame.image.load('Slimeright.fw.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (30, 30), )
            self.xPosition += 2
        elif keys_pressed[K_w]:
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
                    self.rect.bottom = Floors.rect.topw
        elif keys_pressed[K_s]:
            self.sprite2 = pygame.image.load('SlimeR.png')
            self.sprite2 = pygame.transform.scale(self.sprite2, (25, 25), )
            self.yPosition += 2
        else:
            self.sprite2 = pygame.image.load('SlimeR.png')
            self.sprite2 = pygame.transform.scale(self.sprite2,(25,25), )

        def outOFbounds(self):
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > width:
                self.rect.right = width
            elif self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > height:
                self.rect.bottom = height

velocity = 0
movex = 0
movey = 0
sprite_state = 'RESTING'
Slime = Slime()
Slime2 = Slime2()

while True:

    Floors.draw()
    DISPLAYSURF.blit(background, (0, 0))
    Slime.outOFbounds()
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
