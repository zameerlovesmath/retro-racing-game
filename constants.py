import pygame

FPS_count = 0
make_it_harder = 200
WIDTH = 800
HEIGHT = 500
ORIGIN = (WIDTH//2,HEIGHT//5)
road_perc = 1
colour = 0
colours = 0
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
MIDGREEN = (0,143,17)
GRASSC = (36, 161, 14)
DARKGREEN = (0,59,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREY = (173,171,163)

pause_screen = pygame.image.load('pause-screen.png')
oil = pygame.image.load('oil_spill.png')
cone = pygame.image.load('traffic_cone_art.png')
car = pygame.image.load('car_game_thing.png')
pygame.mixer.music.load('racing_background_music.mp3')
tree_1 = pygame.image.load('tree.png')
tree_2 = pygame.image.load('another_tree.png')
bg = pygame.image.load("background.png")
game_over_screen = pygame.image.load("game_over_screen.png")