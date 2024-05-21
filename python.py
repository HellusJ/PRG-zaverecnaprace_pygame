import pygame
import sys
import random
import time
from obrazky import *

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Kostky")

#hra
body = 0
body_pc = 0

#funkce
def napis(text,font_size,x,y):
    vykres = pygame.font.SysFont(None, font_size).render(text, True, textcolor)
    screen.blit(vykres, (x,y))

souradnice = [(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700)]

def animace_ruk():
    for z in range(10):
        snimek = animace_ruce[z]
        x,y = souradnice[z]
        screen.blit(pozadi,(0,0))
        screen.blit(ruce_opp,(210, 0))
        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (x, y) 
        screen.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.2)

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

#pravidlas
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
        napis("První kdo získá 10000 bodů tak vyhrává!", 50, 20, 600)

        pygame.display.flip()
        pygame.time.delay(60)

#HRA
hod = []
def hra():
    while True:
        screen.blit(pozadi, (0, 0))
        screen.blit(ruce, (210,580))
        screen.blit(ruce_opp, (210, 0))
        screen.blit(throwbutton, throwbutton_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if throwbutton_rect.collidepoint(event.pos):

                    animace_ruk()

                    for i in range(6):
                        losovani = random.choice(kostky)
                        hod.append(losovani)

                    y = 235
                    for kosticka in hod:
                        screen.blit(kosticka,(y, 480))
                        y += 40

                    hod.clear()

        pygame.display.flip()
        pygame.time.delay(60)

menu()

