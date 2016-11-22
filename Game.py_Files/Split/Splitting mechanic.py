import pygame
from pygame.locals import *

class Split:
    #Split state 0 = Has not split/is one whole slime. Split state 1 = Has split and cannot split further currently.
    def __init__(self, xP = 0, yP = 0):
        self.split_state = [0,1]
        self.xP = xP
        self.yP = yP
        self.xV = 0
        self.yV = 0

slimes = ['Slimeleft.png'(100, 100), 'Slimeright.png'(100,100)]
speed = 0.5
    #Returns information on whether or not the user has split yet
    def get_split_state(self):
        return self.split_state

    #Changes the split_state appropriately.
    def set_split_state(self):
        if self.split_state == 0 and KEYDOWN == K_i:
            slimes[1].xP = slimes[1].xP - slimes[0].xP * speed
            slimes[1].yP = slimes[1].yP - slimes[0].yP * speed
            self.split_state = 1
            return True
        else:
            self.split_state = 0
            return False



event.type == KEYDOWN K_i:
set_split_state()














