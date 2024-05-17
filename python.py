import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Kostky")

    #OBRAZKY
#barvy
menucolor = (220,255,255)

#pozadi
pozadi = pygame.image.load("background.png")

#buttons
playbutton = pygame.transform.scale(pygame.image.load("button_play.png"), (300,150))
playbutton_rect = playbutton.get_rect()
playbutton_rect.center = (355, 245)

quitbutton = pygame.transform.scale(pygame.image.load("button_quit.png"), (260,140))
quitbutton_rect = playbutton.get_rect()
quitbutton_rect.center = (369, 420)

#ruce
ruce = pygame.transform.scale(pygame.image.load("ruce.png"), (280, 120))
ruce_shaking_1 = pygame.transform.scale(pygame.image.load("ruce_shaking_1.png"), (80, 80))
ruce_Shaking_2 = pygame.transform.scale(pygame.image.load("ruce_Shaking_2.png"), (90, 90))
ruce_throw = pygame.transform.scale(pygame.image.load("ruce_throw.png"), (308, 132))

#kostky
kostka1 = pygame.image.load("kostka_1.png")
kostka2 = pygame.image.load("kostka_2.png")
kostka3 = pygame.image.load("kostky_3.png")
kostka4 = pygame.image.load("kostky_4.png")
kostka5 = pygame.image.load("kostky_5.png")
kostka6 = pygame.image.load("kostky_6.png")

animace_ruce = [ruce, ruce_shaking_1,ruce_Shaking_2, ruce_throw]
kostky = [kostka1,kostka2,kostka3,kostka4,kostka5,kostka6]

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton_rect.collidepoint(event.pos):
                    hra()
                elif quitbutton_rect.collidepoint(event.pos):
                    sys.exit()
                
        screen.fill(menucolor)
        screen.blit(playbutton, playbutton_rect)
        screen.blit(quitbutton, quitbutton_rect)
        pygame.display.flip()

def hra():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #pozadi
        screen.blit(pozadi, (0, 0))

        #ruce
        screen.blit(ruce, (210,580))

        pygame.display.flip()
        pygame.time.delay(30)
        
menu()
