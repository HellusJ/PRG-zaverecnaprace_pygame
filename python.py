import pygame
import sys
import random
import time
from obrazky import *

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Kostky")



#funkce
def napis(text,font_size,x,y):
    vykres = pygame.font.SysFont(None, font_size).render(text, True, textcolor)
    screen.blit(vykres, (x,y))

souradnice = [(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700)]



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
    global players_points
    players_points = 0
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
                    napis(f"points: {players_points}",40,30,660)

                    for i in range(6):
                        losovani = random.choice(kostky)
                        hod.append(losovani)

                    y = 235
                    for kosticka in hod:
                        screen.blit(kosticka,(y, 480))
                        y += 40

                    pocet_jednicek = hod.count(kostka1)
                    pocet_dvojek = hod.count(kostka2)
                    pocet_trojek = hod.count(kostka3)
                    pocet_ctverek = hod.count(kostka4)
                    pocet_petek = hod.count(kostka5)
                    pocet_sestek = hod.count(kostka6)

                    #jednicky
                    if pocet_jednicek == 1:
                        players_points += 100
                    if pocet_jednicek == 2:
                        players_points += 200
                    if pocet_jednicek == 3:
                        players_points += 1000
                    if pocet_jednicek == 4:
                        players_points += 2000
                    if pocet_jednicek == 5:
                        players_points += 4000
                    if pocet_jednicek == 6:
                        players_points += 8000
                    
                    #dvojky
                    if pocet_dvojek == 3:
                        players_points = players_points + (2 * 100)
                    if pocet_dvojek == 4:
                        players_points = players_points + (2 * 200)
                    if pocet_dvojek == 5:
                        players_points = players_points + (2 * 400)
                    if pocet_dvojek == 6:
                        players_points = players_points + (2 * 800)   
                    
                    #trojky
                    if pocet_trojek == 3:
                        players_points = players_points + (3 * 100)
                    if pocet_trojek == 4:
                        players_points = players_points + (3 * 200)
                    if pocet_trojek == 5:
                        players_points = players_points + (3 * 400)
                    if pocet_trojek == 6:
                        players_points = players_points + (3 * 800)

                    #ctverky
                    if pocet_ctverek == 3:
                        players_points = players_points + (4 * 100)
                    if pocet_ctverek == 4:
                        players_points = players_points + (4 * 200)
                    if pocet_ctverek == 5:
                        players_points = players_points + (4 * 400)
                    if pocet_ctverek == 6:
                        players_points = players_points + (4 * 800)

                    #petky
                    if pocet_petek == 1:
                        players_points += 50
                    if pocet_petek == 2:
                        players_points += 100
                    if pocet_petek == 3:
                        players_points = players_points + (5 * 100)
                    if pocet_petek == 4:
                        players_points = players_points + (5 * 200)
                    if pocet_petek == 5:
                        players_points = players_points + (5 * 400)
                    if pocet_petek == 6:
                        players_points = players_points + (5 * 800) 

                    #sestky
                    if pocet_sestek == 3:
                        players_points = players_points + (6 * 100)
                    if pocet_sestek == 4:
                        players_points = players_points + (6 * 200)
                    if pocet_sestek == 5:
                        players_points = players_points + (6 * 400)
                    if pocet_sestek == 6:
                        players_points = players_points + (6 * 800) 

                    hod.clear()

        napis(f"points: {players_points}",40,30,660)
        pygame.display.flip()
        pygame.time.delay(60)

def animace_ruk():
    for z in range(10):
        snimek = animace_ruce[z]
        x,y = souradnice[z]
        screen.blit(pozadi,(0,0))
        screen.blit(ruce_opp,(210, 0))
        napis(f"points: {players_points}",40,30,660)
        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (x, y) 
        screen.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.2)

menu()