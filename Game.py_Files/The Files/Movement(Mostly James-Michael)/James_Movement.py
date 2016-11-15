import pygame, sys, time
from pygame.locals import *
from pygame.transform import scale

pygame.init()

FPS=90
fpsClock=pygame.time.Clock()

width=807
height=489
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('Slime Evo background.png')



DOWN='down'

sprite=pygame.image.load('SlimeR.png')
sprite = pygame.transform.scale(sprite,(35, 35),)
spritex=200
spritey=130
direction=DOWN
velocity = 0
movex = 0
movey = 0
sprite_state = 'RESTING'

while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                sprite=pygame.image.load('Slimeleft.png')
                sprite = pygame.transform.scale(sprite,(40, 40),)
            elif (event.key == K_RIGHT):
                sprite=pygame.image.load('Slimeright.fw.png')
                sprite = pygame.transform.scale(sprite, (40, 40),)
            elif (event.key == K_UP):
                sprite=pygame.image.load('SlimeR.png')
                sprite = pygame.transform.scale(sprite, (35, 35),)
            #elif (event.key == K_DOWN):
                #sprite=pygame.image.load('SlimeR.png')


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_LEFT]:
        spritex -= 5

    if keys_pressed[K_RIGHT]:
        spritex +=5

    if keys_pressed[K_UP]:
        spritey -=5

    if keys_pressed[K_DOWN]:
        spritey +=5

    if keys_pressed[K_SPACE]:
        if pygame.key.set_repeat(1,1):
            movey =-4
            sprite_state = 'JUMPING'



    #if event.type==KEYUP:
     #   if event.key==K_SPACE:
      #      if movey >= 5:
       #         for x in range(5, 0, -1):
        #            spritey = +1



    spritey+=movey


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
    print movey

    pygame.display.update()
    fpsClock.tick(FPS)