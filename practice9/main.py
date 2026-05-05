import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()
x, y = 300, 200
speed = 20
running = True
while running:
   screen.fill((255, 255, 255))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT] and x > 25:
       x -= speed
   if keys[pygame.K_RIGHT] and x < 575:
       x += speed
   if keys[pygame.K_UP] and y > 25:
       y -= speed
   if keys[pygame.K_DOWN] and y < 375:
       y += speed
   pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
   pygame.display.update()
   clock.tick(60)
pygame.quit()
sys.exit()