import random
import pygame

BLACK = (0, 0, 0)

class Stars():

    def __init__(self, background, width, height, max_stars):
        self.background = background
        self.width = width
        self.height = height
        self.total_stars = max_stars
        self.positions = self.generate_positions()

    def generate_positions(self):
        return [[random.randint(0, self.width), random.randint(0, self.height)] for i in range(self.total_stars)]

    def draw(self, star):
        pygame.draw.line(self.background, (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
        star[0] = star[0] - 1
        if star[0] < 0:
            star[0] = self.width
            star[1] = random.randint(0, self.height)

class Asteroid(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/med_1_p1.png').convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.asteroid_list = pygame.sprite.Group()

    def get_random_position(self):
        return {'x': random.randint(800, 1281), 'y': random.randint(0, 800)}

    def generate_asteroids(self, minimum, maximum):
        for i in range(random.randint(minimum, maximum)):
            position = self.get_random_position()
            asteroid = Asteroid()
            asteroid.rect.x = position['x']
            asteroid.rect.y = position['y']
            self.asteroid_list.add(asteroid)

    def update(self):
        self.rect.x -= 2
        if self.rect.x < -5:
            self.rect.y = random.randrange(0, 800)
            self.rect.x = random.randint(800, 1281)
