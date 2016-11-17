import pygame, sys, time
from pygame.locals import *
from pygame.transform import scale

pygame.init()

white = (255, 255, 255)
FPS=90
fpsClock=pygame.time.Clock()

# Display window
width=807
height=489
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('Slime Evo background.png')

# Boundary boxes
floor1 = pygame.draw.rect(background, white,(0, 395, 210, 20))
floor2 = pygame.draw.rect(background, white,(200, 412, 20, 20))
floor3 = pygame.draw.rect(background, white,(210, 420, 20, 20))
floor4 = pygame.draw.rect(background, white,(222, 425, 20, 20))
floor5 = pygame.draw.rect(background, white,(230, 431, 130, 20))
floor6 = pygame.draw.rect(background, white,(355, 425, 20, 20))
floor7 = pygame.draw.rect(background, white,(365, 420, 20, 20))
floor8 = pygame.draw.rect(background, white,(375, 412, 20, 20))
floor9 = pygame.draw.rect(background, white,(385, 395, 170, 20))
floor10 = pygame.draw.rect(background, white,(545, 369, 130, 35))
floor11 = pygame.draw.rect(background, white,(648, 344, 159, 35))

wall1 = pygame.draw.rect(background, white,(0, 0, 10, 400))
wall2 = pygame.draw.rect(background, white,(799, 0, 10, 370))

#Sprite class
class Slime:
    def __init__(self):
        self.sprite = pygame.image.load('SlimeR.png')
        self.sprite = pygame.transform.scale(self.sprite, (35, 35), )
        self.spritex = 10
        self.spritey = 360

    def Draw(self):
        DISPLAYSURF.blit(self.sprite, (self.spritex, self.spritey))

    def Update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.sprite = pygame.image.load('Slimeleft.png')
            self.sprite = pygame.transform.scale(self.sprite, (40, 40), )
            self.spritex -= 5

        if keys_pressed[K_RIGHT]:
            self.sprite = pygame.image.load('Slimeright.fw.png')
            self.sprite = pygame.transform.scale(self.sprite, (40, 40), )
            self.spritex += 5

        if keys_pressed[K_UP]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (35, 35), )
            self.spritey -= 5

        if keys_pressed[K_DOWN]:
            self.sprite = pygame.image.load('SlimeR.png')
            self.sprite = pygame.transform.scale(self.sprite, (35, 35), )
            self.spritey += 5

        if keys_pressed[K_SPACE]:
            if pygame.key.set_repeat(1, 1):
                movey = -4
                sprite_state = 'JUMPING'


DOWN ='down'
direction=DOWN
velocity = 0
movex = 0
movey = 0
sprite_state = 'RESTING'
Slime = Slime()

while True:
    DISPLAYSURF.blit(background,(0,0))

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