import pygame

pygame.init()
screen = pygame.display.set_mode((620, 480))
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
	pygame.draw.rect(screen, (0, 0, 255),(100,100,400,300), 8)
	pygame.display.flip()