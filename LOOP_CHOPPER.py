"""
@author: Franck WIATROWSKI

Version: 0.2
"""
import pygame
import time
from random import randint


""" Initialisation de Pygame """
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)

""" Définition de l'environnement de jeu """
class AppInit(object):
    """ Classe pour créer des instances Pygame """
    
    def __init__(self, display_width, display_height, display_title):
        """ initialisation de l'application """
        self.size = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(display_title)
        
class Players(object):
    """ Classe pour la création de joueurs """
    
    def __init__(self, name, vehicule):
        """ initialise une instance joueur avec un nom et un sprite vehicule """
        self.available_vehicules = {
        "Chopper": "./Assets/chopper.png"
        }
        self.name = name
        self.sprite = pygame.image.load(self.available_vehicules[vehicule])

class Incoming(object):
    """ Classe pour la création d'obstacles """ 
    
    def __init__(self, incoming_type):
        """ Initialise une instance d'obstacle """
        self.available_asteroids = {
        1: "./Assets/asteroid01.png",
        2: "./Assets/asteroid02.png",
        3: "./Assets/asteroid03.png",
        4: "./Assets/asteroid04.png",
        5: "./Assets/asteroid05.png",
        6: "./Assets/asteroid06.png"
        }
        self.incoming_type = incoming_type
        self.sprite =  pygame.image.load(self.available_asteroids[incoming_type])

class Musics(object):
    """ Classe pour la gestion des musiques """
    
    def __init__(self, music):
        """ Initialisation d'un objet musique """
        self.available_musics = {
        "Epic": "./Assets/epic.ogg",
        "Supercopter": "./Assets/supercopter.ogg"
        }
        pygame.mixer.music.load(self.available_musics[music])
        pygame.mixer.music.play(-1)

color_black = (0, 0, 0) # couleurs disponible
main_display = AppInit(800, 600, "LOOP CHOPPER") # Affichage de la fenêtre
background_image = pygame.image.load("Assets/background02a.png") # Image de font
player_01 = Players("Franck", "Chopper") # Création joueur

""" chargement des obstacles (niveau 1) """
asteroid_sprite01 = Incoming(1)
asteroid_sprite02 = Incoming(2)
asteroid_sprite03 = Incoming(3)
asteroid_sprite04 = Incoming(4)
asteroid_sprite05 = Incoming(5)
asteroid_sprite06 = Incoming(6)

clock = pygame.time.Clock() # Initialisation de l'horloge

def score(param_score):
    """ fonction d'affichage du score in game """
    score_font = pygame.font.Font('Assets/BradBunR.ttf', 40)
    score_display = score_font.render("score: " + str(param_score), True, (200, 82, 82))
    main_display.size.blit(score_display, (10, 10))

def exit_game():
    """ Fonction de sortie du programme """
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                return event.key
    return  None

def game_over(final_score):
    """ Fonction d'affichage de l'écran GameOver """
    gameover_font = pygame.font.Font('Assets/BradBunR.ttf', 130)
    replay_font = pygame.font.Font('Assets/BradBunR.ttf', 30)
    score_font = pygame.font.Font('Assets/BradBunR.ttf', 30)
    score_display = score_font.render("Votre score est de : " + str(final_score) + " points", True, (200, 82, 82))
    replay_display = replay_font.render("Appuyez sur <SPACE> pour rejouer ou <ESC> pour quitter",True,(200,82,82))
    gameover_display = gameover_font.render("Raté !!", True, (200, 82, 82))
    main_display.size.blit(gameover_display, (250, 300))
    main_display.size.blit(replay_display, (100, 450))
    main_display.size.blit(score_display, (250, 50))
    pygame.mixer.music.fadeout(2000)
    pygame.display.update()
    time.sleep(2)
    while exit_game() == None :
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    main()
                    
        
        
""" Fonction affichant l'écran titre """
def main_title():
    main_title_running = True
    x_background_01 = 0
    y_background_01 = 0
    main_display.size.blit(background_image, (x_background_01, y_background_01))
    main_title_font = pygame.font.Font('Assets/BradBunR.ttf', 100)
    main_title_text = main_title_font.render("LOOP CHOPPER", True, (200, 82, 82))
    main_display.size.blit(main_title_text, (150, 100))
    main_title_subfont = pygame.font.Font('Assets/BradBunR.ttf', 30)
    main_title_subtext = main_title_subfont.render("Appuyez sur <SPACE> pour commencer !", True, (200, 82, 82))
    main_display.size.blit(main_title_subtext, (180, 250))
    pygame.display.update()
    
    while main_title_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    main()

""" Fonction affichant l'écran de fin """
def ending():
    ending_running = True
    ending_background = pygame.image.load("Assets/ending.jpeg")
    x_ending_background = 0
    y_ending_background = 0
    main_display.size.blit(ending_background, (x_ending_background, y_ending_background))
    pygame.display.update()
    ending_music = Musics("Supercopter") # Musique Ending
    #pygame.mixer.music.load('Assets/supercopter.ogg')
    #pygame.mixer.music.play(-1)
    pygame.draw.rect(main_display.size, color_black, [0, 536, 800, 64])
    ending_font = pygame.font.SysFont('Brady Bunch Remastered', 58)
    ending_display = ending_font.render("FÉLICITATIONS !", True, (200, 82, 82))
    main_display.size.blit(ending_display,(250, 530))
    pygame.display.update()
    pygame.time.wait(12000)
    pygame.draw.rect(main_display.size, color_black, [0, 536, 800, 64])
    ending_font_sub = pygame.font.SysFont('Brady Bunch Remastered', 58)
    ending_display_sub = ending_font_sub.render("Appuyez sur <ESC> pour quitter", True, (200, 82, 82))
    main_display.size.blit(ending_display_sub,(50, 530))
    pygame.display.update()
    
    while ending_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


""" Fonction principale """
def main():
    
    current_score = 0 # initialisation du score
    level_one_music = Musics("Epic") # Musiques (1er Niveau)
    
    """ Position initiale du joueur, du font et des obstacles """
    x_player_sprite = 150
    y_player_sprite = 250
    x_background_image = 0
    y_background_image = 0
    x_asteroid_sprite01 = 800
    y_asteroid_sprite01 = randint(-50, 500)
    x_asteroid_sprite02 = 900
    y_asteroid_sprite02 = randint(-20, 500)
    x_asteroid_sprite03 = 1000
    y_asteroid_sprite03 = randint(-10, 500)
    x_asteroid_sprite04 = 1100
    y_asteroid_sprite04 = randint(-50, 500)
    x_asteroid_sprite05 = 1000
    y_asteroid_sprite05 = randint(-20, 500)
    x_asteroid_sprite06 = 900
    y_asteroid_sprite06 = randint(-30, 500)

    ym_player_sprite = 5 # Variable de mouvement
    
    """ Gestion de la vitesse des obstacle en fonction du score """
    xm_asteroid_sprite = 6

    """ Logique du jeu """

    running = True # Variable de boucle de l'application
    
    """ Boucle de l'application """
    while running:
        clock.tick(40) 
        main_display.size.blit(background_image, (x_background_image, x_background_image))
        
        """ Rendu des obstacles & du sprite joueur """
        main_display.size.blit(asteroid_sprite01.sprite, (x_asteroid_sprite01, y_asteroid_sprite01))
        main_display.size.blit(asteroid_sprite02.sprite, (x_asteroid_sprite02, y_asteroid_sprite02))
        main_display.size.blit(asteroid_sprite03.sprite, (x_asteroid_sprite03, y_asteroid_sprite03))
        main_display.size.blit(asteroid_sprite04.sprite, (x_asteroid_sprite04, y_asteroid_sprite04))
        main_display.size.blit(asteroid_sprite05.sprite, (x_asteroid_sprite05, y_asteroid_sprite05))
        main_display.size.blit(asteroid_sprite06.sprite, (x_asteroid_sprite06, y_asteroid_sprite06))
        main_display.size.blit(player_01.sprite, (x_player_sprite, y_player_sprite))
        
        y_player_sprite += ym_player_sprite # Déplacement du joueur

        """ Déplacement des obstacles """
        x_asteroid_sprite01 -= xm_asteroid_sprite
        x_asteroid_sprite02 -= xm_asteroid_sprite
        x_asteroid_sprite03 -= xm_asteroid_sprite
        x_asteroid_sprite04 -= xm_asteroid_sprite
        
        """ Évènements joueur """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_UP:
                    ym_player_sprite = -20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ym_player_sprite = 10

        """ Incrémentation du score en fonction de la position des obstacles """
        if x_asteroid_sprite01 < -100:
            current_score += 1
            x_asteroid_sprite01 = 1000
        if x_asteroid_sprite02 < -100:
            current_score += 1
            x_asteroid_sprite02 = 1100
        if x_asteroid_sprite03 < -100:
            current_score += 1
            x_asteroid_sprite03 = 1200
        if x_asteroid_sprite04 < -1000:
            current_score += 1
            x_asteroid_sprite04 = 1100
        if x_asteroid_sprite05 < -1000:
            current_score += 1
            x_asteroid_sprite05 = 1100
        if x_asteroid_sprite06 < -1000:
            current_score += 1
            x_asteroid_sprite06 = 1100

        """ Gestion des collisions """
        if x_player_sprite > x_asteroid_sprite01 - 50 and x_player_sprite < x_asteroid_sprite01 + 50:
            if y_player_sprite > y_asteroid_sprite01 - 50 and y_player_sprite < y_asteroid_sprite01 + 50 :
                game_over(current_score)
        if x_player_sprite > x_asteroid_sprite02 - 50 and x_player_sprite < x_asteroid_sprite02 + 50:
            if y_player_sprite > y_asteroid_sprite02 - 50 and y_player_sprite < y_asteroid_sprite02 + 50 :
                game_over(current_score)
        if x_player_sprite > x_asteroid_sprite03 - 50 and x_player_sprite < x_asteroid_sprite03 + 50:
            if y_player_sprite > y_asteroid_sprite03 - 50 and y_player_sprite < y_asteroid_sprite03 + 50 :
                game_over(current_score)
        if x_player_sprite > x_asteroid_sprite04 - 50 and x_player_sprite < x_asteroid_sprite04 + 50:
            if y_player_sprite > y_asteroid_sprite04 - 50 and y_player_sprite < y_asteroid_sprite04 + 50 :
                game_over(current_score)
        if y_player_sprite > 600 or y_player_sprite < 0:
            game_over(current_score)

        """ Atteinte du score/Fin du jeu """
        if current_score >= 50:
            ending()

        score(current_score)
        pygame.display.update()

""" Lancement & arrêt du programme """
main_title()
pygame.quit()
quit()