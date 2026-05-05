import pygame
import sys
import os
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont(None, 36)
# 👉 ОСТАВЬ ТОЛЬКО СУЩЕСТВУЮЩИЙ ФАЙЛ
playlist = ["track1.mp3"]
index = 0
def play():
   file = playlist[index]
   # проверка файла
   if not os.path.exists(file):
       print("FILE NOT FOUND:", file)
       return
   try:
       pygame.mixer.music.load(file)
       pygame.mixer.music.play()
       print("PLAYING:", file)
   except Exception as e:
       print("ERROR:", e)
play()
running = True
paused = False
while running:
   screen.fill((0, 0, 0))
   text = font.render(f"Track: {playlist[index]}", True, (255, 255, 255))
   screen.blit(text, (50, 120))
   info = font.render("P=Play S=Pause R=Resume Q=Quit", True, (200, 200, 200))
   screen.blit(info, (20, 200))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_p:
               play()
           if event.key == pygame.K_s:
               pygame.mixer.music.pause()
               paused = True
           if event.key == pygame.K_r:
               pygame.mixer.music.unpause()
               paused = False
           if event.key == pygame.K_q:
               running = False
   pygame.display.update()
pygame.quit()
sys.exit()