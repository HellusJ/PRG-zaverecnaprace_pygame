import pygame
import sys
import random
import time
from obrazky import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Kostky")

#funkce
def napis(text,font_size,x,y):
    vykres = pygame.font.SysFont(None, font_size).render(text, True, textcolor)
    screen.blit(vykres, (x,y))

def zvuk(nazev):
    sound = pygame.mixer.Sound(nazev)
    sound.play()

souradnice = [(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700),(350,700)]
souradnice_opp = [(350,80),(350,80),(350,80),(350,80),(350,80),(350,80),(350,80),(350,120),(350,120),(350,120)]

#menu
def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton_rect.collidepoint(event.pos):
                    zvuk("click_sound.mp3")
                    hra()
                    
                elif quitbutton_rect.collidepoint(event.pos):
                    zvuk("click_sound.mp3")
                    time.sleep(0.25)
                    sys.exit()

                elif rulesbutton_rect.collidepoint(event.pos):
                    zvuk("click_sound.mp3")
                    rules()
        
        screen.fill(menucolor)
        screen.blit(playbutton, playbutton_rect)
        screen.blit(rulesbutton, rulesbutton_rect)
        screen.blit(quitbutton, quitbutton_rect)
        
        pygame.display.flip()

#pravidlas
def rules():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if stepback_rect.collidepoint(event.pos):
                    zvuk("click_sound.mp3")
                    menu()

        screen.fill(menucolor)
        screen.blit(stepback, stepback_rect)
        screen.blit(rules1, rules1_rect)
        napis("První kdo získá 10000 bodů tak vyhrává!", 50, 20, 600)

        pygame.display.flip()
        pygame.time.delay(60)

#HRA
pc_points = 0
players_points = 0
hod = []
hod_opp = []
def hra():

    global pc_points
    global players_points

    while True:

        screen.blit(pozadi, (0, 0))
        screen.blit(ruce, (210,580))
        screen.blit(ruce_opp, (210, 0))
        screen.blit(throwbutton, throwbutton_rect)
        screen.blit(throw_opp_button, throw_opp_button_rect)

        #vyhra/prohra
        if pc_points >= 10000 or players_points >= 10000:
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if throwbutton_rect.collidepoint(event.pos):

                    animace_ruk()
                    zvuk("diceroll_sound.mp3")
                    
                    for i in range(6):
                        losovani = random.choice(kostky)
                        hod.append(losovani)

                    y = 235
                    for kosticka in hod:
                        screen.blit(kosticka,(y, 480))
                        y += 40

                    pygame.display.flip()
                    pygame.time.wait(3000)

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

                    

                    #postupka
                    postupka = set(kostky)
                    porovnani = set(hod)
                    if postupka == porovnani:
                        players_points += 1500

                    #tridvojice
                    
                    hod.clear()
                    zvuk("points_sound.mp3")

                elif throw_opp_button_rect.collidepoint(event.pos):

                    animace_ruk_opp()
                    zvuk("diceroll_sound.mp3")

                    for i in range(6):
                        losovani2 = random.choice(kostky_opp)
                        hod_opp.append(losovani2)

                    y = 235
                    for kosticka2 in hod_opp:
                        screen.blit(kosticka2,(y, 230))
                        y += 40

                    pygame.display.flip()
                    pygame.time.wait(3000)

                    pocet_jednicek_opp = hod_opp.count(kostka1)
                    pocet_dvojek_opp = hod_opp.count(kostka2)
                    pocet_trojek_opp = hod_opp.count(kostka3)
                    pocet_ctverek_opp = hod_opp.count(kostka4)
                    pocet_petek_opp = hod_opp.count(kostka5)
                    pocet_sestek_opp = hod_opp.count(kostka6)

                    #jednicky
                    if   pocet_jednicek_opp == 1:
                        pc_points += 100
                    if   pocet_jednicek_opp == 2:
                        pc_points += 200
                    if   pocet_jednicek_opp == 3:
                        pc_points += 1000
                    if   pocet_jednicek_opp == 4:
                        pc_points += 2000
                    if   pocet_jednicek_opp == 5:
                        pc_points += 4000
                    if   pocet_jednicek_opp == 6:
                        pc_points += 8000
                    
                    #dvojky
                    if pocet_dvojek_opp == 3:
                        pc_points = pc_points + (2 * 100)
                    if pocet_dvojek_opp == 4:
                        pc_points = pc_points + (2 * 200)
                    if pocet_dvojek_opp == 5:
                        pc_points = pc_points + (2 * 400)
                    if pocet_dvojek_opp == 6:
                        pc_points = pc_points + (2 * 800)   
                    
                    #trojky
                    if pocet_trojek_opp == 3:
                        pc_points = pc_points + (3 * 100)
                    if pocet_trojek_opp == 4:
                        pc_points = pc_points + (3 * 200)
                    if pocet_trojek_opp == 5:
                        pc_points = pc_points + (3 * 400)
                    if pocet_trojek_opp == 6:
                        pc_points = pc_points + (3 * 800)

                    #ctverky
                    if pocet_ctverek_opp == 3:
                        pc_points = pc_points + (4 * 100)
                    if pocet_ctverek_opp == 4:
                        pc_points = pc_points + (4 * 200)
                    if pocet_ctverek_opp == 5:
                        pc_points = pc_points + (4 * 400)
                    if pocet_ctverek_opp == 6:
                        pc_points = pc_points + (4 * 800)

                    #petky
                    if pocet_petek_opp == 1:
                        pc_points += 50
                    if pocet_petek_opp == 2:
                        pc_points += 100
                    if pocet_petek_opp == 3:
                        pc_points = pc_points + (5 * 100)
                    if pocet_petek_opp == 4:
                        pc_points = pc_points + (5 * 200)
                    if pocet_petek_opp == 5:
                        pc_points = pc_points + (5 * 400)
                    if pocet_petek_opp == 6:
                        pc_points = pc_points + (5 * 800) 

                    #sestky
                    if pocet_sestek_opp == 3:
                        pc_points = pc_points + (6 * 100)
                    if pocet_sestek_opp == 4:
                        pc_points = pc_points + (6 * 200)
                    if pocet_sestek_opp == 5:
                        pc_points = pc_points + (6 * 400)
                    if pocet_sestek_opp == 6:
                        pc_points = pc_points + (6 * 800)

                    #postupka
                    postupka2 = set(kostky_opp)
                    porovnani2 = set(hod_opp)
                    if postupka2 == porovnani2:
                        pc_points += 1500

                    #tridvojice
                

                    hod_opp.clear()
                    zvuk("points_sound.mp3")

        napis(f"points: {players_points}",40,30,660)
        napis(f"points: {pc_points}", 40,30,20)
        pygame.display.flip()
        pygame.time.delay(60)

def animace_ruk():
    for z in range(10):
        snimek = animace_ruce[z]
        x,y = souradnice[z]
        screen.blit(pozadi,(0,0))
        screen.blit(ruce_opp,(210, 0))
        napis(f"points: {players_points}",40,30,660)
        napis(f"points: {pc_points}", 40,30,20)
        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (x, y) 
        screen.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.2)



def animace_ruk_opp():
    for g in range(10):
        snimek2 = animace_ruce_opp[g]
        x2,y2 = souradnice_opp[g]
        screen.blit(pozadi,(0,0))
        screen.blit(ruce,(210, 580))
        snimek2_rect = snimek2.get_rect()
        snimek2_rect.midbottom = (x2, y2)         
        napis(f"points: {players_points}",40,30,660)
        napis(f"points: {pc_points}", 40,30,20)
        screen.blit(snimek2, snimek2_rect)
        pygame.display.update()
        time.sleep(0.2)

menu()