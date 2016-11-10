import pygame
from pygame.locals import *

class Split:
    #Split state 0 = Has not split/is one whole slime. Split state 1 = Has split and cannot split further currently.
    def __init__(self):
        self.split_state = [0,1]

    #Returns information on whether or not the user has split yet
    def get_split_state(self):
        return self.split_state

    #Changes the split_state appropriately.
    def set_split_state(self):
        if self.split_state == 0:
            self.split_state = 1
            return True
        else:
            self.split_state = 0
            return False

    #Executes code based on state of split_state
    def split_exe(self):
        while self.split_state == 1:






