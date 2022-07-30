import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

keep_going = True
GREEN = (250,255,255)
radius = 50

while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False
	pygame.draw.circle(screen,GREEN,(100,100), radius)
	pygame.display.update()

pygame.quit()