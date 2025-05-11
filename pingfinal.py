from pygame import*
from time import time as timer
font.init()
#переменные
win_width = 900
win_height = 700
BACK = (200, 255, 255)
FPS = 60
r_point = 0
l_point = 0
speed_x = 3
speed_y = 3

window = display.set_mode((win_width, win_height))
display.set_caption('ДЖАМП- ДЖАМП')
window.fill(BACK)
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, image_obj, x, y, width, height, speed):
        super().__init__()
        self.image = image.load(image_obj)
        self.image = transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 595:
            self.rect.y += self.speed  

    def update_left(self):  
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 595:
            self.rect.y += self.speed

racket_left = Player('racket.png', 10, 300, 30, 100, 4)
racket_right = Player('racket.png', 860, 300, 30, 100, 4)
ball = GameSprite('ball.png', 425, 325, 50, 50, 3)

font_check = font.SysFont('Areal', 70)
r_check = font_check.render(str(r_point), True, (0,0,0))
l_check = font_check.render(str(l_point), True, (0,0,0))
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(BACK)
        racket_left.update_left()
        racket_right.update_right()
        r_check = font_check.render(str(r_point), True, (0,0,0))
        l_check = font_check.render(str(l_point), True, (0,0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > win_height - 50:
            speed_y *= -1

        if sprite.collide_rect(racket_left, ball) or sprite.collide_rect(racket_right, ball):
            speed_x *= -1

        if ball.rect.x < 5:
            r_point += 15
            time.delay(500)
            ball.rect.x = 425
            ball.rect.x = 325


        if ball.rect.x > 845:
            l_point += 15
            time.delay(500)
            ball.rect.x = 425
            ball.rect.x = 325



        racket_left.reset()
        racket_right.reset()
        ball.reset()
        window.blit(l_check, (415, 5))
        window.blit(r_check, (475, 5))

        if r_point >= 60:
            finish = True
            winner = font_check.render('Игрок прав прав', True, (200,50,0)) 
            window.blit(winner, (150, 330))
        if l_point >= 60:
            finish = True
            winner = font_check.render('Игрок слива молодец', True, (200,50,0))
            window.blit(winner, (150, 330))


    else:
        time.delay(3000)
        racket_right.rect.y = 300
        racket_left.rect.y = 300
        ball.rect.x = 425
        ball.rect.y = 325
        r_point = 0
        l_point = 0
        finish = False


    display.update()
    clock.tick(FPS)
