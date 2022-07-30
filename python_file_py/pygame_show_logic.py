import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Logic")
bg_color = (245, 240, 250)
image = "/red_alert_3y/python_work/image_bmp_jng_jpg/logic.bmp"


def blitlogic():
	image_logic = pygame.image.load(image)
	screen_rect = screen.get_rect()
	rect = image_logic.get_rect()
	rect.midbottom = screen_rect.midbottom
	screen.fill(bg_color)
	screen.blit(image_logic, rect)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	blitlogic()
	pygame.display.flip()
