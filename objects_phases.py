import pygame
import random

BLACK = (0, 0, 0)

class Asteroid(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.counter = 0
        self.phases = []
        self.index = 0
        self.image = self.phases[self.index]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

    def update(self):
        self.rect.x -= self.speed

        self.counter += 1
        if self.counter >= self.counter_limit:

            self.index += 1
            if self.index >= len(self.phases):
                self.index = 0
            self.image = self.phases[self.index]
            self.image.set_colorkey(BLACK)
            self.counter = 0

        if self.rect.x <= -35:
            self.rect.y = random.randint(0, 366)
            self.rect.x = 640

    def generate_asteroid_list(self, number_of_asteroids):
        pass

class Small(Asteroid):

    def __init__(self):

        super(Asteroid, self).__init__()
        self.speed = 3
        self.counter_limit = 10
        self.size = 20
        self.counter = 0
        self.phases = []
        self.index = 0
        self.phases.append(pygame.image.load('images/small_1_p1.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p2.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p3.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p4.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p5.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p6.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p7.png').convert())
        self.phases.append(pygame.image.load('images/small_1_p8.png').convert())

        self.image = self.phases[self.index]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

class Medium(Asteroid):

    def __init__(self):

        super(Asteroid, self).__init__()
        self.speed = 2

        self.counter_limit = 20
        self.size = 30
        self.counter = 0
        self.phases = []
        self.index = 0
        self.phases.append(pygame.image.load('images/med_1_p1.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p2.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p3.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p4.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p5.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p6.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p7.png').convert())
        self.phases.append(pygame.image.load('images/med_1_p8.png').convert())

        self.image = self.phases[self.index]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

class Big(Asteroid):

    def __init__(self):

        super(Asteroid, self).__init__()
        self.speed = 1

        self.counter_limit = 35
        self.size = 45
        self.counter = 0
        self.phases = []
        self.index = 0
        self.phases.append(pygame.image.load('images/big_1_p1.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p2.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p3.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p4.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p5.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p6.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p7.png').convert())
        self.phases.append(pygame.image.load('images/big_1_p8.png').convert())

        self.image = self.phases[self.index]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)


pygame.init()

size = (640, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("spaceshooter")

done = False

clock = pygame.time.Clock()

background_image = pygame.image.load('images/bg_blue.png').convert()

asteroid_list = pygame.sprite.Group()

for i in range(random.randint(12, 21)):

    if i % 5 == 0:

        asteroid = Big()
        asteroid.rect.x = random.randrange(640, 1881, 50)
        asteroid.rect.y = random.randrange(0, 365, 50)
        asteroid_list.add(asteroid)

    elif i % 3 == 0:

        asteroid = Medium()
        asteroid.rect.x = random.randrange(640, 1881, 50)
        asteroid.rect.y = random.randrange(0, 365, 50)
        asteroid_list.add(asteroid)

    else:
        asteroid = Small()
        asteroid.rect.x = random.randrange(640, 1881, 50)
        asteroid.rect.y = random.randrange(0, 365, 50)
        asteroid_list.add(asteroid)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, [0, 0])

    asteroid_list.draw(screen)
    asteroid_list.update()

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
