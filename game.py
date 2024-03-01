import pygame, random, math, sys, time
'''Konstantine was here on line 2
alec
test
Dimitri
James is the player
Bob is the enemy'''
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
last_collision = time.time()
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
oil = pygame.image.load('oil_spill.png')
cone = pygame.image.load('traffic_cone_art.png')
car = pygame.image.load('StepHBig2.png')
car = pygame.transform.scale(car, (150, 105))
tree_1 = pygame.image.load('tree.png')
tree_2 = pygame.image.load('another_tree.png')
bg = pygame.image.load("background.png")
pygame.transform.scale(tree_1, (50, 50))
pygame.transform.scale(tree_2, (50, 50))
pygame.mixer.music.load('racing_background_music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
music_playing = True
lives = 5
tree_counter = 0

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,70))
        self.image = car
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = HEIGHT - 50
        self.speedx = 0
        self.speedy = 0
        self.ticker = 0

    def update(self):
        speed = 10
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.x or keystate[pygame.K_a] and self.rect.x > 90:
            self.speedx = -speed
            #if self.rect.x > (1 - road_perc) * WIDTH:
        if keystate[pygame.K_d] and self.rect.x or keystate[pygame.K_RIGHT] and self.rect.x < WIDTH - 230:
            self.speedx = speed
        if keystate[pygame.K_q]:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        #if keystate[pygame.K_UP]:
            #self.speedy = -speed
            #self.ticker += 1 #NEW CODE
        #if keystate[pygame.K_DOWN]:
            #self.speedy = speed
            #self.ticker += 1 #NEW CODE
        self.rect.x += self.speedx
        #HERE WE ARE GOING TO WRAP AROUND THE EDGES IF THE SPRITE
        #GOES OFF THE SCREEN
        #REMEMBER THAT X IS LEFT TO RIGHT AND Y IS UP AND DOWN
        # if self.rect.x > WIDTH:
        #     self.rect.x = 0
        # if self.rect.x < 0:
        #     self.rect.x = WIDTH
        # self.rect.y += self.speedy
        # if self.rect.y > HEIGHT:
        #     self.rect.y = 0
        # if self.rect.y < 0:
        #     self.rect.y = HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image = random.choice([oil,cone])
        #self.image.fill(random.choice([MIDGREEN,DARKGREEN]))
        self.rect = self.image.get_rect()
        self.rect.centerx = ORIGIN[0]
        self.rect.centery = ORIGIN[1]
        self.speedx = 0
        self.speedy = 0
        self.heading = random.choice([60,75,90,105,120])####
    def update(self):
        speed = 10
        self.speedx = speed*math.cos(math.radians(self.heading))
        self.speedy = speed*math.sin(math.radians(self.heading))
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.y > HEIGHT:
            self.kill()
        if self.rect.x > WIDTH:
            self.kill()

class Road(pygame.sprite.Sprite):
    def __init__(self):
        self.width = 20 #50
        self.height = 5
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.width,self.height))
        #self.image = random.choice([oil,cone])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.centerx = ORIGIN[0]
        self.rect.centery = ORIGIN[1]
        self.speedx = 0
        self.speedy = 0
        self.heading = 90
        self.numrecs = (HEIGHT - ORIGIN[1])//self.height
        self.upperright = (WIDTH + self.width)//2
        self.targetright = (road_perc*WIDTH)
        self.step = (self.targetright - self.upperright) // self.numrecs
        self.increment = self.step * 2
        #self.heading = random.choice([30,60,90,120,150])####
    def update(self):
        self.width += self.increment
        self.image = pygame.Surface((self.width,30))
        self.image.fill(GREY)
        #self.speedx = WIDTH//2
        self.rect.centerx -= self.step
        self.speedy = self.height
        self.rect.centery += self.speedy
        #self.rect.centerx += self.speedx
        if self.rect.y > HEIGHT:
            self.kill()
        if self.rect.x > WIDTH:
            self.kill()
class Blue(pygame.sprite.Sprite):
    def __init__(self):
        global colour
        self.width = 0
        self.height = 5
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.width,self.height))
        #self.image = random.choice([oil,cone])
        self.rect = self.image.get_rect()
        self.rect.centerx = ORIGIN[0]-25
        self.rect.centery = ORIGIN[1]
        self.speedx = 0
        self.speedy = 0
        self.heading = 90
        self.numrecs = (HEIGHT - ORIGIN[1])//self.height
        self.upperright = (WIDTH + self.width)//2
        self.targetright = (road_perc*WIDTH)
        self.step = (self.targetright - self.upperright) // self.numrecs
        self.increment = self.step * 2.0
        #self.heading = random.choice([30,60,90,120,150])####
        self.spacing = 0
        colour += 0.2
        if int(colour)%2 == 0:
            self.color = (BLUE)
        else:
            self.color = (WHITE)

    def update(self):
        self.width += self.increment
        self.image = pygame.Surface((self.width+50,5+self.spacing))
        self.image.fill(self.color)
        #self.speedx = WIDTH//2
        self.rect.centerx -= self.step
        self.speedy = self.height
        self.rect.centery += self.speedy
        #self.rect.centerx += self.speedx
        if self.rect.y > HEIGHT:
                self.kill()
        if self.rect.x > WIDTH:
                self.kill()

class TREE(pygame.sprite.Sprite):
    def __init__(self):
        self.width = 70
        self.height = 70
        pygame.sprite.Sprite.__init__(self)
        self.type_of_tree = random.choice([tree_1,tree_2])
        self.image = pygame.transform.scale(self.type_of_tree, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.left_or_right = random.choice([-1,1])
        if self.left_or_right == -1:
            self.rect.centerx = 265
        else:
            self.rect.centerx = WIDTH - 300
        self.rect.centery = ORIGIN[1]
        self.speedx = 0
        self.speedy = 0
        self.heading = 90

    def update(self):
        self.rect.x += self.left_or_right * 3
        self.rect.y += 3
        self.width += 0.4
        self.height += 0.4
        self.image = pygame.transform.scale(self.type_of_tree, (self.width, self.height))
        if self.rect.y > HEIGHT:
            self.kill()
        if self.rect.x > WIDTH:
            self.kill()


all_sprites = pygame.sprite.Group()
last_time_volume_changed = time.time()
james = Player()
bob = Enemy()
all_sprites.add(james)
all_sprites.add(bob)
road_sprites = pygame.sprite.Group()
running = True
def draw_score(LIVES):
    steering_wheel = pygame.image.load('steering_wheel_thing.png')
    steering_wheel = pygame.transform.scale(steering_wheel, (80, 80))
    wheel = steering_wheel.get_rect()
    OFFSET = 60
    for i in range(LIVES):
        wheel.centerx = WIDTH - OFFSET
        wheel.centery = 40
        screen.blit(steering_wheel, wheel)
        OFFSET += 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
    pygame.event.get()
    blue = Blue()
    roady = Road()
    road_sprites.add(blue)
    road_sprites.add(roady)
    keystate = pygame.key.get_pressed()
    tree_counter += 1
    if pygame.sprite.collide_rect(james, bob) and time.time() - 0.25 > last_collision:
        last_collision = time.time()
        lives -= 1
        # print("hi")

    if lives <= 0:
        running = False
        print("You died")

    #make it harder part
    FPS_count += 1
    if FPS_count >= 3600:
        make_it_harder -= 5
    if make_it_harder <= 15:
        make_it_harder = 30
    if random.randint(1, make_it_harder) == 15:
        bob = Enemy()
        all_sprites.add(bob)
        all_sprites.remove(james)
        all_sprites.add(james)
    if tree_counter == 5:
        tree_guy = TREE()
        all_sprites.add(tree_guy)
        tree_counter %= 5
    if keystate[pygame.K_s]:
        if music_playing:
            pygame.mixer.music.pause()
            music_playing = False
        else:
            pygame.mixer.music.unpause()
            music_playing = True
    if keystate[pygame.K_EQUALS] and time.time() - last_time_volume_changed > 0.2:
        volume = pygame.mixer.music.get_volume() + 0.05
        last_time_volume_changed = time.time()
        if volume < 0:
            volume = 0
        if volume > 1:
            volume = 1
        pygame.mixer.music.set_volume(volume)
    if keystate[pygame.K_MINUS] and time.time() - last_time_volume_changed > 0.2:
        volume = pygame.mixer.music.get_volume() - 0.05
        last_time_volume_changed = time.time()
        if volume < 0:
            volume = 0
        if volume > 1:
            volume = 1
        pygame.mixer.music.set_volume(volume)
    road_sprites.update()
    all_sprites.update()
    screen.blit(bg,(0,0))
    #screen.fill(GRASSC)
    draw_score(lives)
    road_sprites.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
