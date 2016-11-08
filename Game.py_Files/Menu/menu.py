import pygame
pygame.init()

#Assign Variables
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red2 = (200,0,0)
green = (0,255,0)
green2 = (0,200,0)
blue = (50,90,255)
display_width = 800
display_height = 600
Icon = pygame.image.load('icon.png')
Slime = pygame.image.load('SlimeR.png')
Slime2 = pygame.image.load('Slimeleft.png')
Slime3 = pygame.image.load('Slimeright.fw.png')
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SlimeEvo')
pygame.display.set_icon(Icon)
clock = pygame.time.Clock()
left = (150, 450, 100, 50)
right = (550, 450, 100, 50)
Menu = pygame.image.load('Background.png')
text1 = pygame.font.Font("Background2.ttf", 80)
text2 = pygame.font.Font("Background2.ttf", 30)
mouse = pygame.mouse.get_pos()

#Defines the tools for drawing the font
def text_objects(text,font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def text_objects2(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

Quit = text_objects2('Quit', text2)
Play = text_objects2('Play', text2)

#Menu Button(Left)
def LeftButton():
        mouse = pygame.mouse.get_pos()
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen,green,left)
            screen.blit(Slime2, (150, 330))
        else:
            pygame.draw.rect(screen, green2, (left))


#Menu Button(Right)
def RightButton():
        mouse = pygame.mouse.get_pos()

        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, red, (right))
            screen.blit(Slime3, (550, 330))

        else:
            pygame.draw.rect(screen,red2, (right))



#Keeping the menu alive(on) and creating the displayed imagery.
def game_intro():
    intro = True
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                    pygame.quit()
                    quit()
                elif mouse!= 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(Menu,(0,0))
        TextSurf, TextRect = text_objects('Slime-Evo', text1)
        TextRect.center = ((400), (100))
        screen.blit(TextSurf, TextRect)
        LeftButton()
        RightButton()
        screen.blit(Quit[0], (555, 460))
        screen.blit(Play[0], (151, 460))
        screen.blit(Slime, (300, 200))
        pygame.display.update()
game_intro()

#Deciding when to close the game and telling the game to close the game if you decide that the game needs to be closed. Close.
menuquit = False
while not menuquit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            menuquit = True

        print(event)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
