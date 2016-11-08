# Slime - EVO MEGA GAME

import pygame as pg
import random
from Setting import *
from Sprites import *


class Game:
    def __init__(self):
        # Initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((Width, Height))
        pg.display.set_caption("Slime EVO")
        self.Clock = pg.time.Clock()
        self.running = True

    def new(self):
        # Starts a new game
        self.all_Sprites = pg.sprite.Group()
        self.player = Player()
        self.all_Sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        self.Clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.Clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_Sprites.update()

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
        #Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.all_Sprites.draw(self.screen)
        # After Drawing Everything, Flips the Display
        pg.display.flip()

    def show_start_screen(self):
        # Game Start Screen
        pass

    def show_start_Screen(self):
        # Game End Screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_Screen()

pg.quit()
