import sys, random, pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from spaceship import Spaceship, Bomb, Bullet, Laser
from background2 import Background
from keyboard_event_controller import keyboard_event_controller

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

        self.stars = Background.generate_stars(self, stars, width, height)
        self.spaceship = Spaceship()

        self.projectiles = []
        self.lasers = []

        self.main()

    def exit(self):
        pygame.quit()
        sys.exit()

    def fps_and_playtime_caption(self):
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self.playtime)
        pygame.display.set_caption(text)

    def main(self):
        keyboard_events = [False, False, False, False, False]
        while self.running:
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    self.exit()

                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False
                    self.exit()

                keyboard_event_controller(pygame.key.get_pressed(), keyboard_events)

            self.fps_and_playtime_caption()
            self.background.fill((0, 0, 0))
            Background.draw_stars(self, self.stars, self.background, self.width, self.height)
            self.screen.blit(self.background, (0, 0))
            self.spaceship.move(keyboard_events)
            self.spaceship.draw(self.screen)
            self.spaceship.shoot(keyboard_events, self.projectiles)

            for projectile in self.projectiles:
                projectile.update()
                projectile.draw(self.screen)
            for laser in self.lasers:
                laser.draw(self.screen)

            pygame.display.update()

if __name__ == '__main__':
	Screen(width=800, height=800, stars=600, fps=100)
