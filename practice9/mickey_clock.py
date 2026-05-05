import pygame
import sys
import math
from datetime import datetime
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Clock with Numbers")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
center = (200, 200)
radius = 140
running = True
while running:
   screen.fill((255, 255, 255))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   now = datetime.now()
   seconds = now.second
   minutes = now.minute
   # 🔵 цифры часов (круг 12 часов)
   for i in range(1, 13):
       angle = math.radians(i * 30)  # 360 / 12 = 30°
       x = center[0] + radius * math.sin(angle)
       y = center[1] - radius * math.cos(angle)
       text = font.render(str(i), True, (0, 0, 0))
       rect = text.get_rect(center=(x, y))
       screen.blit(text, rect)
   # 🟢 секундная стрелка
   sec_angle = math.radians(seconds * 6)
   sec_x = center[0] + 120 * math.sin(sec_angle)
   sec_y = center[1] - 120 * math.cos(sec_angle)
   # 🔵 минутная стрелка
   min_angle = math.radians(minutes * 6)
   min_x = center[0] + 90 * math.sin(min_angle)
   min_y = center[1] - 90 * math.cos(min_angle)
   # центр
   pygame.draw.circle(screen, (0, 0, 0), center, 5)
   # стрелки
   pygame.draw.line(screen, (255, 0, 0), center, (sec_x, sec_y), 2)
   pygame.draw.line(screen, (0, 0, 255), center, (min_x, min_y), 4)
   pygame.display.update()
   clock.tick(1)
pygame.quit()
sys.exit()