import pygame
import random
import glob

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Asteroid():

	def __init__(self, max_x, max_y):
		self.max_x = max_x
		self.max_y = max_y
		self.image = None
		self.speed = 0

	def make_sprite(self):
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(self.max_x, self.max_x * 2)
		self.rect.y = random.randint(0, self.max_y)

	def update(self):
		self.rect.x -= self.speed
		if self.rect.x < 0:
			self.rect.x = random.randint(self.max_x, self.max_x * 2)
			self.rect.y = random.randint(0, self.max_y)


class SmallAsteroid(Asteroid, pygame.sprite.Sprite):

	def __init__(self, max_x, max_y):
		pygame.sprite.Sprite.__init__(self)
		self.max_x = max_x
		self.max_y = max_y
		self.image = pygame.image.load(random.choice(glob.glob("images/asteroids/SMALL/*.png")))
		self.make_sprite()
		self.value = 100
		self.speed = 5

class MediumAsteroid(Asteroid, pygame.sprite.Sprite):

	def __init__(self, max_x, max_y):
		pygame.sprite.Sprite.__init__(self)
		self.max_x = max_x
		self.max_y = max_y
		self.image = pygame.image.load(random.choice(glob.glob("images/asteroids/MEDIUM/*.png")))
		self.make_sprite()
		self.value = 50
		self.speed = 4

class BigAsteroid(Asteroid, pygame.sprite.Sprite):
	def __init__(self, max_x, max_y):
		pygame.sprite.Sprite.__init__(self)
		self.max_x = max_x
		self.max_y = max_y
		self.image = pygame.image.load(random.choice(glob.glob("images/asteroids/BIG/*.png")))
		self.make_sprite()
		self.value = 30
		self.speed = 3
