import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red2 = (200,0,0)
green = (0,255,0)
green2 = (0,200,0)
blue = (0,0,255)
display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SlimeEvo')
clock = pygame.time.Clock()

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def game_intro():
    intro = True

    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(black)
        text1 = pygame.font.Font('freesansbold.ttf', 155)
        TextSurf, TextRect = text_objects('SlimeEvo', text1)
        TextRect.center = ((display_width/2), (display_height/2))
        screen.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(screen, green2, (150, 450, 100, 50))

        pygame.draw.rect(screen, red, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)




game_intro()

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
