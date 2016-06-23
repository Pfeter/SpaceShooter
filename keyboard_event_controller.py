import pygame
from pygame.locals import *

def keyboard_event_controller(press, direction):
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

	# if press[pygame.K_SPACE]:
	#     self.projectiles.append(Bullet(self.spaceship.x, self.spaceship.y))
	# if press[pygame.K_a]:
	#     self.projectiles.append(Bomb(self.spaceship.x, self.spaceship.y))
	# if press[pygame.K_s]:
	#     self.lasers.append(Laser(self.spaceship.x, self.spaceship.y, self.width))

    return direction
