import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
warna_bg = (240,24, 55)

pygame.display.set_caption("Hallo APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen,(0, 0, 255),(0, 0),(300, 300))
	pygame.draw.line(screen,(0, 0, 255),(0, 20),(300, 320))
	pygame.display.flip()