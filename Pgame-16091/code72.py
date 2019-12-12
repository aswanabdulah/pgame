# Pemrograman Game Praktikum 7
# latihan code 7.1 : Pgame

import pygame, sys
from pygame.locals import*

pygame.init()

DYSPLAYSURF = pygame.display.set_mode ((700, 400))

pygame.display.set_caption ('Hello Ances!')

while True: # main game loop
	for event in pygame.event.get ();
	if event.type == QUIT:
		pygame.quit ()
	pygame.display.update ()
