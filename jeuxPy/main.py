import pygame
import os

pygame.init()

WIDTH = 800
HEIGHT = 640
screen = pygame.display.set_mode([WIDTH,  HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)

clock = pygame.time.Clock()
fps = 60

#variable de jeu
GRAVITY = 0.5

#variable d'action du jouer
moving_left = False
moving_right = False
shoot = False

#load img
#balles
bullet_img = pygame.image.load("C:/Users/pedro/Documents/LP_MIAW/jeuxPy/images/icons/bullet.png").convert_alpha()

#couleur du font
BG = (144, 201, 120)
RED = (255, 0, 0)

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0,280), (WIDTH, 280))

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()



        #load all img for players
        animation_types = ['idle', 'run', 'jump']
        for animation in animation_types:
            #reset les images animation
            temp_list = []
            #numbre de fichier dans un doc
            num_of_frames = len(os.listdir(f'C:/Users/pedro/Documents/LP_MIAW/jeuxPy/images/{self.char_type}/{animation}'))
            for i in range (num_of_frames):
                img = pygame.image.load(f'C:/Users/pedro/Documents/LP_MIAW/jeuxPy/images/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale) , (int(img.get_height() * scale) )))
                temp_list.append(img)
            self.animation_list.append(temp_list)
           
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



    def move(self, moving_left, moving_right):
        
        #reinitialisation des mouvements
        dx = 0
        dy = 0
        
        #assignement du movement left right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:     
            dx = self.speed
            self.flip = False
            self.direction = 1

        #jump
        if self.jump == True and self.in_air == False:
           self.vel_y = -11 
           self.jump = False
           self.in_air = True
        
        #gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y
      
        #check coliision avec le sol
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        #update position carée
        self.rect.x += dx
        self.rect.y += dy


    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN: 
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #resart animation list 
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    
    def update_action(self, new_action):
        #regarder si a nouvelle action est differente a l'encienne
        if new_action!= self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
       


    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.directin = direction


#creat sprite group
bullet_group = pygame.sprite.Group()

    
            


player = Soldier('player', 500, 100, 2, 5)
enemy = Soldier('enemy', 200, 100, 2, 5)



run = True
while run :

    clock.tick(fps)

    draw_bg()

    player.update_animation()
    player.draw()
    enemy.update_animation()
    enemy.draw()


    #update and draw bullet
    bullet_group.update()
    bullet_group.draw(screen)

    #update player actions
    if player.alive:
        #shoot bullets
        if shoot:
            bullet = Bullet(player.rect.centerx, player.rect.centery,10 , player.direction)
            bullet_group.add(bullet)
            shoot = False
        if player.in_air:
            player.update_action(2)#jump
        elif moving_left or moving_right :
            player.update_action(1) #run
        else: 
            player.update_action(0) #idle
        player.move(moving_left, moving_right)
    
    

    
    for event in pygame.event.get(): 
        #quit
        if event.type == pygame.QUIT:
            run = False
        #keyboard press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_z and player.alive:
                player.jump = True

        #keyboard release
        if event.type == pygame.KEYUP:      
            if event.key == pygame.K_q:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            



        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
