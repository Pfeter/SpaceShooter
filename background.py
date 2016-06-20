import sys, random
import pygame
from pygame.locals import *

class Screen(object):

	def __init__(self, width=640, height=400, fps=60):
		pygame.init()
		pygame.display.set_caption("Press ESC to quit")
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.clock = pygame.time.Clock()
		self.fps = fps
		self.playtime = 0.0
		self.font = pygame.font.SysFont('mono', 20, bold=True)
		self.stars = self.generate_stars(200)
		self.running = True

		self.main()

	def generate_stars(self, N):
		return [[random.randint(0, self.width), random.randint(0, self.height)] for i in range(N)]

	def draw_stars(self):
		for star in self.stars:
			pygame.draw.line(self.background,
											 (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
			star[0] = star[0] - 1
			if star[0] < 0:
				star[0] = self.width
				star[1] = random.randint(0, self.height)

	def main(self):
		while self.running:
			self.clock.tick(self.fps)
			for event in pygame.event.get():
				if event.type == QUIT:
					self.running = False
					pygame.quit()
					sys.exit(2)
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					self.running = False
					pygame.quit()
					sys.exit(2)
			self.background.fill((0, 0, 0))
			self.draw_stars()
			self.screen.blit(self.background, (0, 0))
			pygame.display.flip()


if __name__ == '__main__':
	Screen()