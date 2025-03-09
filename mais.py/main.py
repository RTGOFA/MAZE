from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, speed):
        super().__init__()
        self.pimage = transform.scale(image.load(pimage), (65, 65))
        

        self.rect = self.pimage.get_rect()
        self.speed = speed


        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.pimage, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - self.rect.width:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x > win_width - self.rect.width - self.rect.width:
            self.direction = 'left'
        if self.rect.x < win_width * 0.6:
            self.direction = 'right'

        if self.direction == 'left':
            self.rect.x -= self.speed

        if self.direction == 'right':
            self.rect.x += self.speed

win_height = 500
win_width = 700

class Wall(sprite.Sprite):
    def __init__(self, R, G, B, wall_x,wall_y, wall_w, wall_h, ):
        super().__init__()
        self.R = R
        self.G = G
        self.B = B
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((R, G, B))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(2, 247, 121, 20, 20, 600, 20)
wall2 = Wall(2, 247, 121, 20, 20, 20, 400)
wall3 = Wall(2, 247, 121, 620, 20, 20, 400)
wall4 = Wall(2, 247, 121, 120, 120, 20, 400)
wall5 = Wall(2, 247, 121, 250, 20, 20, 400)
wall6 = Wall(2, 247, 121, 370, 120, 20, 420)

window = display.set_mode((win_width,win_height))
display.set_caption("лабіринт")
background = transform.scale(image.load("background.jpg"),  (win_width, win_height))

player = Player('hero.png', 10, win_height-80, 4)
enemy = Enemy('cyborg.png', win_height-80, 120, 2)
final = GameSprite('treasure.png', win_height-80, win_height-80, 0)

game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.get_volume

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')


while game:
    window.blit(background, (0, 0))

    player.update()
    enemy.update()

    player.draw()
    enemy.draw()
    final.draw()

    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()

    if sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or \
        sprite.collide_rect(player, wall3) or sprite.collide_rect(player, enemy):
        kick.play()
        player.rect.x = 10
        player.rect.y = win_height-80
    if sprite.collide_rect(player, final):
        time.delay(1000)
        money.play()
        game = False


    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)












