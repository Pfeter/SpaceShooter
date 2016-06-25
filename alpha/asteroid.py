import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Asteroid(pygame.sprite.Sprite):

	def __init__(self, max_x, max_y):
		pygame.sprite.Sprite.__init__(self)
		self.max_x = max_x
		self.max_y = max_y
		self.image = pygame.image.load("images/asteroid.png").convert()
		self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = random.randint(max_x, max_x * 2)
		self.rect.y = random.randint(0, max_y)

	def update(self):
		self.rect.x -= 3
		if self.rect.x < 0:
			self.rect.x = random.randint(self.max_x, self.max_x * 2)
			self.rect.y = random.randint(0, self.max_y)
