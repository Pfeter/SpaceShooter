import sys, random, pygame
from pygame.locals import *
from spaceship import Spaceship, Bomb, Laser, Bullet
from stars import Stars, Asteroid

class Screen(object):
    def __init__(self, width=640, height=400, fps=60, stars=200):
        self.running = True
        self.score = 0

        # CONSTANT
        self.FPS = fps
        self.PLAYTIME = 0.0
        self.TOTAL_STARS = stars
        self.WIDTH = width
        self.HEIGHT = height

        # INITIALIZE SCREEN, CLOCK, FONT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert(self.screen)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('mono', 20, bold=True)

        # INITIALIZE SCREEN OBJECTS
        self.stars = Stars(self.background, self.WIDTH, self.HEIGHT, self.TOTAL_STARS)
        self.asteroid = Asteroid()
        self.spaceship = Spaceship()

        self.main()

    def exit(self):
        pygame.quit()
        sys.exit()

    def fps_and_playtime_caption(self):
        text = "FPS: {0:.2f}   Playtime: {1:.2f}   SCORE: {}".format(self.clock.get_fps(), self.PLAYTIME, self.score)
        pygame.display.set_caption(text)

    def is_valid_move(self):
        return self.spaceship.x in range(0, self.WIDTH) and self.spaceship.y in range(0, self.HEIGHT)

    def main(self):
        while self.running:

            # PLAYTIME
            milliseconds = self.clock.tick(self.FPS)
            self.PLAYTIME += milliseconds / 1000.0

            # MOVEMENT
            for event in pygame.event.get():
                self.spaceship.move_route(pygame.key.get_pressed())

            # DRAW SPACESHIP
            if self.is_valid_move:
                self.spaceship.draw(self.screen)

            # INITIALIZE BACKGROUND, DRAW STARS
            self.background.fill((0, 0, 0))
            for star in self.stars.positions:
                self.stars.draw(star)

            # UPDATE CAPTION
            self.fps_and_playtime_caption()

            # MAKE SCREEN
            self.screen.blit(self.background, (0, 0))

            # DRAW ASTEROIDS, PROJECTILES
            self.asteroid.asteroid_list.draw(self.screen)
            for comet in self.asteroid.asteroid_list:
                comet.update()

            self.projectile.projectile_list.draw(self.screen)
            for ammo in self.projectile.projectile_list:
                ammo.update()
                # COLLIDE CHECK
                asteroid_hit_list = pygame.sprite.spritecollide(ammo, self.asteroid.asteroid_list, True)
                self.score = len(asteroid_hit_list)


            pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Press ESC to quit")
    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")
    Screen(width=800, height=800, stars=600, fps=100)
