import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Spaceship(pygame.sprite.Sprite):

	def __init__(self, width=800, height=800):
		pygame.sprite.Sprite.__init__(self)

		self.MAX_X = 800
		self.MAX_Y = 800
		self.angle = 270
		self.direction = None

		self.image = pygame.transform.rotate(pygame.image.load("images/spaceship_top.png"), self.angle)
		self.image.convert()
		self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 350

		self.projectiles = pygame.sprite.Group()
		self.score = 0
		self.movement_speed = 2

	def get_action_from_key_press(self, press):
		if press[pygame.K_UP]: self.direction = 'up'
		if press[pygame.K_DOWN]: self.direction = 'down'
		if press[pygame.K_RIGHT]: self.direction = 'right'
		if press[pygame.K_LEFT]: self.direction = 'left'
		if self.direction:
			self.move()

	def validate_move(self):
		return 0 < self.rect.x + self.movement_speed < self.MAX_X and 0 < self.rect.y + self.movement_speed < self.MAX_Y

	def movement_routing(self, press):
		self.get_action_from_key_press(press)
		self.move()

	def move(self):
		self.validate_move()
		if self.direction == 'up':
			self.rect.y -= self.movement_speed
		if self.direction == 'down':
			self.rect.y += self.movement_speed
		if self.direction == 'right':
			self.rect.x += self.movement_speed
		if self.direction == 'left':
			self.rect.x -= self.movement_speed


class Bullet(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/bullet.png").convert()
		self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.rect.x += 2.5