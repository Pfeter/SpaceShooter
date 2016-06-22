import sys, random, pygame
from pygame.locals import *
from spaceship import *
from stars import Stars, Asteroid

class Screen(object):
    def __init__(self, width=640, height=400, fps=60, stars=200):
        self.running = True
        self.fps = fps
        self.playtime = 0.0
        self.total_stars = stars

        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont('mono', 20, bold=True)

        self.stars = Stars(self.background, self.width, self.height, self.total_stars)
        self.asteroids = Asteroid()
        self.asteroid_list = self.asteroids.generate_asteroids(12, 15)

        self.spaceship = Spaceship()

        self.projectiles = []

        self.main()

    def exit(self):
        pygame.quit()
        sys.exit()

    def fps_and_playtime_caption(self):
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self.playtime)
        pygame.display.set_caption(text)

    def asteroid_positions(self):
        return [(aster.rect.x, aster.rect.y) for aster in self.asteroids.asteroid_list]

    def main(self):
        direction = [False, False, False, False]
        while self.running:
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0

            for event in pygame.event.get():
                press = pygame.key.get_pressed()
                if event.type == QUIT:
                    self.running = False
                    self.exit()

                elif press[pygame.K_ESCAPE]:
                    self.running = False
                    self.exit()

                if press[pygame.K_UP]:
                    direction[0] = True
                else:
                    direction[0] = False
                if press[pygame.K_DOWN]:
                    direction[1] = True
                else:
                    direction[1] = False
                if press[pygame.K_RIGHT]:
                    direction[2] = True
                else:
                    direction[2] = False
                if press[pygame.K_LEFT]:
                    direction[3] = True
                else:
                    direction[3] = False
                if press[pygame.K_SPACE]:
                    self.projectiles.append(Bullet(self.spaceship.x, self.spaceship.y))
                # if press[pygame.K_a]:
                #     self.projectiles.append(Bomb(self.spaceship.x, self.spaceship.y))
                # if event.key == K_S:
                #     self.projectiles.append(Laser(self.spaceship.x, self.spaceship.y))

            self.fps_and_playtime_caption()
            self.background.fill((0, 0, 0))
            for star in self.stars.positions:
                self.stars.draw(star)

            self.screen.blit(self.background, (0, 0))
            self.asteroids.asteroid_list.draw(self.screen)
            for aster in self.asteroids.asteroid_list:
                aster.update()
            all_asteroid_pos = self.asteroid_positions()
            self.spaceship.move(direction)
            self.spaceship.draw(self.screen)

            for projectile in self.projectiles:
                if projectile.x > 800 :
                    self.projectiles.remove(projectile)
                projectile.update()
                if (projectile.x, projectile.y) in all_asteroid_pos:
                    print("hey")
                projectile.draw(self.screen)

            pygame.display.update()

if __name__ == '__main__':
  Screen(width=800, height=800, stars=600, fps=100)
