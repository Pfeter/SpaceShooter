import pygame
import random

from player import Spaceship, Bullet
from asteroid import Asteroid
from menu import Menu

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)


class Main(object):
	"""Game loop"""

	def __init__(self, height, width, fps):
		# GAME LOOP BOOLEAN
		self.game_running = True

		# SET UP CONSTANTS FOR THE GAME
		self.SCREEN_HEIGHT = height
		self.SCREEN_WIDTH = width
		self.FPS = fps
		self.TOTAL_STARS = random.randint(200, 250)

		self.playtime = 0

		# SET UP GUI, CLOCK AND FONT
		self.screen = pygame.display.set_mode([self.SCREEN_HEIGHT, self.SCREEN_WIDTH], pygame.HWSURFACE | pygame.DOUBLEBUF) # double buffering, framerate buff
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont('mono', 100, bold=True)

		# INIT PLAYER
		self.player = Spaceship(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
		self.player_sprite = pygame.sprite.Group()
		self.player_sprite.add(self.player)

		# CREATE GAME FIELD
		self.stars = self.generate_stars()
		self.asteroids = pygame.sprite.Group()
		self.generate_asteroids()

		self.game()

	def generate_stars(self):
		return [[random.randint(0, self.SCREEN_WIDTH), random.randint(0, self.SCREEN_HEIGHT)] for i in range(self.TOTAL_STARS)]

	def draw_stars(self):
		for star in self.stars:
			pygame.draw.line(self.background, (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
			star[0] = star[0] - 1
			if star[0] < 0:
				star[0] = self.SCREEN_WIDTH
				star[1] = random.randint(0, self.SCREEN_HEIGHT)

	def generate_asteroids(self):
		[self.asteroids.add(Asteroid(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) for i in range(random.randrange(15, 25))]

	def fps_and_playtime_caption(self):
		text = "SCORE: {0:} Playtime: {1:.2f} seconds".format(self.player.score, self.playtime)
		pygame.display.set_caption(text)


	def message_display(self, text):
		sys_font = pygame.font.SysFont("mono", 60, bold=True)
		rendered = sys_font.render(text, 0, (80, 200, 80))
		self.screen.blit(rendered, (250, 300))
		pygame.display.update()

	def game_over(self):
		exit_event = True
		while exit_event:
			events = list(pygame.event.get())
			quit_events = [event for event in events if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE]
			if quit_events:
				break
			self.message_display('GAME OVER')
		pygame.display.quit()


	def game(self):
		available_keyboard_events = {
			pygame.K_LEFT: 'left',
			pygame.K_RIGHT: 'right',
			pygame.K_UP: 'up',
			pygame.K_DOWN: 'down',
			pygame.K_SPACE: 'bullet'
		}


		while self.game_running:
			# GET GAME TIME
			milliseconds = self.clock.tick(self.FPS)
			self.playtime += milliseconds / 1000.0

			# EVENTS, KEYS
			events = list(pygame.event.get())
			keys = pygame.key.get_pressed()
			quit_events = [event for event in events if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE]
			keyup_events = [event for event in events if event.type == pygame.KEYUP and event.key in available_keyboard_events]
			if quit_events:
				pygame.quit()


			self.player.movement_routing(keys)

			self.fps_and_playtime_caption()
			self.background.fill(BLACK)
			self.draw_stars()
			self.screen.blit(self.background, (0, 0))
			self.player_sprite.draw(self.screen)
			self.asteroids.draw(self.screen)

			# CALLING UPDATE ON MAP OBJECTS
			[asteroid.update() for asteroid in self.asteroids]
			if len(self.asteroids) < 10:
				self.generate_asteroids()
			[bullet.update() for bullet in self.player.projectiles]

			# KEYBOARD EVENTS
			if [e for e in keyup_events if available_keyboard_events[e.key] == self.player.direction]:  # STOP SHIP IF KEY RELEASED
				self.player.direction = None
			if pygame.sprite.groupcollide(self.player_sprite, self.asteroids, True, True): # CHECKING ASTEROID COLLISION
				self.game_running = False
				self.game_over()  # DRAW EXIT SCREEN, THAN BREAK INTO MENU

			#BULLET - ASTEROID COLLISION DETECT
			if [e for e in keyup_events if available_keyboard_events[e.key] == 'bullet']:
				self.player.projectiles.add(Bullet(self.player.rect.x, self.player.rect.y))
			if pygame.sprite.groupcollide(self.asteroids, self.player.projectiles, True, True):
				self.player.score += 1
			self.player.projectiles.draw(self.screen)


			pygame.display.update()



if __name__ == '__main__':
	import sys

	pygame.init()
	pygame.display.set_caption("Press ESC to quit")

	pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
	pygame.mixer.music.load("sound/music.mp3")
	pygame.mixer.music.play()

	def menu_loop():
		menu_screen = pygame.display.set_mode((854, 480))
		menu_screen.fill((51, 51, 51))
		menu = Menu(['Start', 'Options', 'Quit'], menu_screen)
		menu.draw()
		pygame.key.set_repeat(199, 69)  # (delay,interval)
		pygame.display.update()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						menu.draw(-1)  # here is the Menu class function
					if event.key == pygame.K_DOWN:
						menu.draw(1)  # here is the Menu class function
					if event.key == pygame.K_RETURN:
						if menu.get_position() == 2:  # here is the Menu class function
							pygame.quit()
							sys.exit()
						elif menu.get_position() == 0:
							try:
								Main(800, 800, 100)
							except:
								pygame.init()
								menu_loop()
					if event.key == pygame.K_ESCAPE:
						pygame.display.quit()
						sys.exit()
					pygame.display.update()
				elif event.type == pygame.QUIT:
					pygame.display.quit()
					sys.exit()
			pygame.time.wait(8)
	menu_loop()
