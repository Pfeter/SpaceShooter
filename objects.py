import random
import pygame

BLACK = (0, 0, 0)

class Asteroid(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/mid_1.png').convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

    def update(self):
        self.rect.x -= 2

        if self.rect.x <= -35:
            self.rect.y = random.randint(0, 366)
            self.rect.x = 640

    def generate_asteroid_list(self, number_of_asteroids):
        pass

pygame.init()

size = (640, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("spaceshooter")

done = False

clock = pygame.time.Clock()

background_image = pygame.image.load('images/bg_blue.png').convert()

asteroid_list = pygame.sprite.Group()

for i in range(random.randint(6, 13)):
    asteroid = Asteroid()
    asteroid.rect.x = random.randint(640, 1281)
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
