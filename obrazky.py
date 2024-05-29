import pygame

#barvy
menucolor = (220,255,255)
textcolor = (0,0,0)

#pozadi
pozadi = pygame.image.load("background.png")

#buttons
playbutton = pygame.transform.scale(pygame.image.load("button_play.png"), (300,150))
playbutton_rect = playbutton.get_rect()
playbutton_rect.center = (355, 100)

quitbutton = pygame.transform.scale(pygame.image.load("button_quit.png"), (260,140))
quitbutton_rect = playbutton.get_rect()
quitbutton_rect.center = (370, 440)

rulesbutton = pygame.transform.scale(pygame.image.load("rules_button.png"), (355,140))
rulesbutton_rect = playbutton.get_rect()
rulesbutton_rect.center = (315, 275)

stepback = pygame.transform.scale(pygame.image.load("stepback.png"), (45,45))
stepback_rect = playbutton.get_rect()
stepback_rect.topleft = (5, 5)

throwbutton = pygame.transform.scale(pygame.image.load("throw_button.png"), (83,35))
throwbutton_rect = playbutton.get_rect()
throwbutton_rect.topleft = (510, 590)

throw_opp_button = pygame.transform.scale(pygame.image.load("throw_opp_button.png"), (83,35))
throw_opp_button_rect = playbutton.get_rect()
throw_opp_button_rect.topleft = (510, 75)

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
kostka1 = pygame.transform.scale(pygame.image.load("kostka_1.png"), (25, 25))
kostka2 = pygame.transform.scale(pygame.image.load("kostka_2.png"), (25, 25))
kostka3 = pygame.transform.scale(pygame.image.load("kostky_3.png"), (25, 25))
kostka4 = pygame.transform.scale(pygame.image.load("kostky_4.png"), (25, 25))
kostka5 = pygame.transform.scale(pygame.image.load("kostky_5.png"), (25, 25))
kostka6 = pygame.transform.scale(pygame.image.load("kostky_6.png"), (25, 25))

#pravidla
rules1 = pygame.transform.scale(pygame.image.load("rules_picture.png"), (560, 560))
rules1_rect = rules1.get_rect()
rules1_rect.topleft = (70, 15)

animace_ruce_opp = [ruce_opp_shaking_1,ruce_opp_Shaking_2,ruce_opp_shaking_1,ruce_opp_Shaking_2,ruce_opp_shaking_1,ruce_opp_Shaking_2, ruce_opp_shaking_1, ruce_opp_throw, ruce_opp_throw, ruce_opp]
animace_ruce = [ruce_shaking_1,ruce_Shaking_2,ruce_shaking_1,ruce_Shaking_2,ruce_shaking_1,ruce_Shaking_2, ruce_shaking_1, ruce_throw, ruce_throw, ruce]
kostky = [kostka1,kostka2,kostka3,kostka4,kostka5,kostka6]
kostky_opp = [kostka1,kostka2,kostka3,kostka4,kostka5,kostka6]

#sign
uwonsign = pygame.transform.scale(pygame.image.load("winneris_sign.png"), (300, 66))
uwonsign_rect = uwonsign.get_rect()
uwonsign_rect.topleft = (200, 250)