from pygame import *

win_width = 500
win_height = 500
window = display.set_mode((win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= 3
        if keys[K_s]:
            self.rect.y += 3
        if keys[K_a]:
            self.rect.x -= 3
        if keys[K_d]:
            self.rect.x += 3
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed 
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width =  width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(255, 0,0,25, 100,200,200)
wall2 = Wall(255, 0,0,200, 10,200,200)

display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'),(win_width, win_height))
player = Player('hero.png', 100, 100, 4)
enemy = Enemy('cyborg.png', 100, 250, 4)
game = True
clock = time.Clock()
mixer.init()
mixer.music.load('money.ogg')
mixer.music.play()

while  game:
    for e in event.get():
        if e.type == QUIT:
            game == False
    window.blit(background,(0,0))
    player.reset()
    player.update()
    enemy.reset()
    enemy.update()
    wall1.draw_wall()
    wall2.draw_wall()
    display.update()
    clock.tick(120)

  
