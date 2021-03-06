import sys, random
import pygame
from pygame.locals import *

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

		self.stars = self.generate_stars()

		self.main()

	def generate_stars(self):
		return [[random.randint(0, self.width), random.randint(0, self.height)] for i in range(self.total_stars)]

	def draw_stars(self):
		for star in self.stars:
			pygame.draw.line(self.background,
											 (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
			star[0] = star[0] - 1
			if star[0] < 0:
				star[0] = self.width
				star[1] = random.randint(0, self.height)

	def exit(self):
		pygame.quit()
		sys.exit(2)

	def fps_and_playtime_caption(self):
		text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self.playtime)
		pygame.display.set_caption(text)

	def main(self):
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

			self.fps_and_playtime_caption()
			self.background.fill((0, 0, 0))
			self.draw_stars()
			self.screen.blit(self.background, (0, 0))
			pygame.display.update()


if __name__ == '__main__':
	Screen(width=800, height=800, stars=600, fps=100)
