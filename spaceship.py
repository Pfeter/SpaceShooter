import pygame

class SpaceShip(object):
    def __init__(self):
        self.x = 50
        self.y = 200
        self.direction_angle = 270
        self.spaceship_image_up = pygame.transform.rotate(pygame.image.load("images/spaceship_up_full.png"), self.direction_angle)
        self.spaceship_image_normal = pygame.transform.rotate(pygame.image.load("images/spaceship_top.png"), self.direction_angle)
        self.spaceship_image_down = pygame.transform.rotate(pygame.image.load("images/spaceship_down_full.png"), self.direction_angle)
        self.spaceship_image = self.spaceship_image_normal

    def draw(self, screen):
        screen.blit(self.spaceship_image, [self.x, self.y])

    def move(self, direction):
        if direction[0]:
            self.spaceship_image = self.spaceship_image_up
            self.y -= 1
        if direction[1]:
            self.spaceship_image = self.spaceship_image_down
            self.y += 1
        if direction[2]:
            self.x += 1
        if direction[3]:
            self.x -= 1
        if direction == [False, False, False, False]:
            self.spaceship_image = self.spaceship_image_normal
