# newfrom pygame import *
from time import time as timer
from random import randint


font.init()
font2 = font.SysFont('Arial', 30)
win = font2.render('YOU WIN!',True,(255,215,0))
lose1 = font2.render('Player 1 LOSE!', True,(180,0,0))
lose2 = font2.render('Player 2 LOSE!', True,(180,0,0))

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, x, y,size_x, size_y, speed):
      super().__init__()
      self.image = transform.scale(image.load(player_image),(size_x, size_y))
      self.speed = speed
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

   def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update1(self):
      keys= key.get_pressed()
      if keys[K_UP] and self.rect.y > 5:
         self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < h-80:
         self.rect.y += self.speed
   def update2(self):
      keys= key.get_pressed()
      if keys[K_w] and self.rect.y > 5:
         self.rect.y -= self.speed
      if keys[K_s] and self.rect.y < h-80:
         self.rect.y += self.speed
l = 900
h =700
speed_x = 3
speed_y = 3

window = display.set_mode((l, h))
display.set_caption('Ping-Pong')
#фон сцены
background = transform.scale(image.load('gazone.png'), (l,h))
player1 = Player('rocet.png', 10, 20 ,100, 150,5 )
player2 = Player('rocet.png',l-80 , 20,100, 150,5 )
ball = GameSprite('ball.png', randint(300,l-400),20, 40,40, 2)     

game = True
clock = time.Clock()
FPS = 60
clock.tick(FPS)
finish= False
run  = True
while game:
   for e in event.get():
      if e.type == QUIT:
         game = False
   if not finish:
      window.blit(background,(0,0))
      player1.update2()
      player2.update1()
      
      ball.rect.x += speed_x
      ball.rect.y += speed_y
      if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
         speed_x *= -1
         speed_y *= 1
      if ball.rect.y > h-50 or ball.rect.y <0:
         speed_y *= -1
      if ball.rect.x < 0:
         finish = True
         window.blit(lose1,(200,20))
         game_over = True
      if ball.rect.x > l:
         finish = True
         window.blit(lose2,(200,20))
         game_over = True

      player1.reset()
      player2.reset()
      ball.reset()
   else:
      finish = False
      ball = GameSprite('ball.png', 250,20, 40,40, 2)  
      time.delay(50)

   display.update()
   clock.tick(FPS)
