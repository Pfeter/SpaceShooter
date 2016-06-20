import sys, pygame
from pygame.locals import *
from spaceship import SpaceShip
# from background import Background

class Screen(object):
    def __init__(self, width=640, height=400, fps=60, stars=200):
        self.running = True
        self.fps = fps
        self.playtime = 0.0
        # self.total_stars = stars

        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont('mono', 20, bold=True)

        # self.stars = Background.generate_stars(self.background, self.stars)
        self.spaceship = SpaceShip()

        self.main()

    def exit(self):
        pygame.quit()
        sys.exit(2)

    def fps_and_playtime_caption(self):
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self.playtime)
        pygame.display.set_caption(text)

    def main(self):
        direction = [False, False, False, False]
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

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        direction[0] = True
                    if event.key == K_DOWN:
                        direction[1] = True
                    if event.key == K_RIGHT:
                        direction[2] = True
                    if event.key == K_LEFT:
                        direction[3] = True
                elif event.type == KEYUP:
                    direction[0] = False
                    direction[1] = False
                    direction[2] = False
                    direction[3] = False

            self.spaceship.move(direction)

            self.fps_and_playtime_caption()
            self.background.fill((0, 0, 0))
            # self.draw_stars()
            self.screen.blit(self.background, (0, 0))
            self.spaceship.draw(self.screen)
            pygame.display.update()

if __name__ == '__main__':
	Screen(width=800, height=800, stars=600, fps=100)
