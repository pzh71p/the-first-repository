import sys 
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))
bg_color = (0, 0, 250)
pygame.display.set_caption("The blue sky!")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill(bg_color)
	pygame.display.flip()
