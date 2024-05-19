import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Kostky")

    #OBRAZKY
#barvy
menucolor = (220,255,255)
textcolor = (0,0,0)

#pozadi
pozadi = pygame.image.load("background.png")

#buttons
playbutton = pygame.transform.scale(pygame.image.load("button_play.png"), (300,150))
playbutton_rect = playbutton.get_rect()
playbutton_rect.center = (355, 160)

quitbutton = pygame.transform.scale(pygame.image.load("button_quit.png"), (260,140))
quitbutton_rect = playbutton.get_rect()
quitbutton_rect.center = (369, 335)

rulesbutton = pygame.transform.scale(pygame.image.load("rules_button.png"), (355,140))
rulesbutton_rect = playbutton.get_rect()
rulesbutton_rect.center = (317, 500)

stepback = pygame.transform.scale(pygame.image.load("stepback.png"), (45,45))
stepback_rect = playbutton.get_rect()
stepback_rect.topleft = (5, 5)

#ruce
ruce = pygame.transform.scale(pygame.image.load("ruce.png"), (280, 120))
ruce_shaking_1 = pygame.transform.scale(pygame.image.load("ruce_shaking_1.png"), (80, 80))
ruce_Shaking_2 = pygame.transform.scale(pygame.image.load("ruce_Shaking_2.png"), (90, 90))
ruce_throw = pygame.transform.scale(pygame.image.load("ruce_throw.png"), (308, 132))

ruce_opp = pygame.transform.scale(pygame.image.load("ruce_opp.png"), (280, 120))
ruce_opp_shaking_1 = pygame.transform.scale(pygame.image.load("ruce_opp_shaking_1.png"), (80, 80))
ruce_opp_Shaking_2 = pygame.transform.scale(pygame.image.load("ruce_opp_Shaking_2.png"), (90, 90))
ruce_opp_throw = pygame.transform.scale(pygame.image.load("ruce_opp_throw.png"), (308, 132)) 

#kostky
kostka1 = pygame.image.load("kostka_1.png")
kostka2 = pygame.image.load("kostka_2.png")
kostka3 = pygame.image.load("kostky_3.png")
kostka4 = pygame.image.load("kostky_4.png")
kostka5 = pygame.image.load("kostky_5.png")
kostka6 = pygame.image.load("kostky_6.png")

#pravidla
rules1 = pygame.transform.scale(pygame.image.load("rules_picture.png"), (560, 560))
rules1_rect = rules1.get_rect()
rules1_rect.topleft = (70, 15)

animace_ruce = [ruce, ruce_shaking_1,ruce_Shaking_2, ruce_throw]
kostky = [kostka1,kostka2,kostka3,kostka4,kostka5,kostka6]

#text
def napsattext(text,font_size,x,y):
    vykres = pygame.font.SysFont(None, font_size).render(text, True, textcolor)
    screen.blit(vykres, (x,y))

#menu
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
                elif rulesbutton_rect.collidepoint(event.pos):
                    rules()
                
        screen.fill(menucolor)
        screen.blit(playbutton, playbutton_rect)
        screen.blit(quitbutton, quitbutton_rect)
        screen.blit(rulesbutton, rulesbutton_rect)
        pygame.display.flip()

#pravidla
def rules():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if stepback_rect.collidepoint(event.pos):
                    menu()

        screen.fill(menucolor)
        screen.blit(stepback, stepback_rect)
        screen.blit(rules1, rules1_rect)
        napsattext("První kdo získá 10000 bodů tak vyhrává!", 50, 20,600)

        pygame.display.flip()
        pygame.time.delay(60)

#HRA
def hra():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.blit(pozadi, (0, 0))
        screen.blit(ruce, (210,580))
        screen.blit(ruce_opp, (210, 0))
        pygame.display.flip()
        pygame.time.delay(60)
        
menu()
