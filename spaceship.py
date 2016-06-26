import pygame

class Spaceship(object):
    def __init__(self):
        self.x = 50
        self.y = 200
        self.direction_angle = 270
        self.spaceship_image_up = pygame.transform.rotate(pygame.image.load("images/spaceship_up_full.png"), self.direction_angle)
        self.spaceship_image_normal = pygame.transform.rotate(pygame.image.load("images/spaceship_top.png"), self.direction_angle)
        self.spaceship_image_down = pygame.transform.rotate(pygame.image.load("images/spaceship_down_full.png"), self.direction_angle)
        self.image = self.spaceship_image_normal
        self.rate_of_fire = 10
        self.last_bullet_ticks = self.rate_of_fire
        self.projectiles = []
        self.lasers = []

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def move(self, direction):
        if direction[0]:
            self.image = self.spaceship_image_up
            self.y -= 1
        if direction[1]:
            self.image = self.spaceship_image_down
            self.y += 1
        if direction[2]:
            self.x += 1
        if direction[3]:
            self.x -= 1
        if direction == [False, False, False, False]:
            self.image = self.spaceship_image_normal

    def shoot(self, keyboard_events):
        if keyboard_events[4]:
            if self.last_bullet_ticks >= self.rate_of_fire:
                self.projectiles.append(Bullet(self.x, self.y))
                self.last_bullet_ticks = 0
            else:
                self.last_bullet_ticks += 1

class Projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def explode(self):
        self.image = pygame.image.load("images/exploded.png")

class Bomb(Projectile):
    def __init__(self, x, y):
        Projectile.__init__(self, x, y)
        self.image = pygame.image.load("images/bomb.png")
        self.timer = 100

    def update(self):
        if self.timer <= 0:
            self.explode()
        else:
            self.timer -= 1

class Bullet(Projectile):
    def __init__(self, x, y):
        Projectile.__init__(self, x, y)
        self.image = pygame.image.load("images/bullet.png")

    def update(self):
        self.x += 2

class Laser(object):
    def __init__(self, x, y, end_x):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = y

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.end_x, self.end_y))

    def update(self, ship_x, ship_y):
        self.x = ship_x
        self.y = ship_y
        self.end_x = ship_x + 800
        self.end_y = ship_y
