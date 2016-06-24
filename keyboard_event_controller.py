import pygame
from pygame.locals import *

def keyboard_event_controller(press, keyboard_events):
    if press[pygame.K_UP]:
        keyboard_events[0] = True
    else:
        keyboard_events[0] = False

    if press[pygame.K_DOWN]:
        keyboard_events[1] = True
    else:
        keyboard_events[1] = False

    if press[pygame.K_RIGHT]:
        keyboard_events[2] = True
    else:
        keyboard_events[2] = False

    if press[pygame.K_LEFT]:
        keyboard_events[3] = True
    else:
        keyboard_events[3] = False

    if press[pygame.K_SPACE]:
        keyboard_events[4] = True
    else:
        keyboard_events[4] = False

    # if press[pygame.K_a]:
    #     self.projectiles.append(Bomb(self.spaceship.x, self.spaceship.y))
    # if press[pygame.K_s]:
    #     self.lasers.append(Laser(self.spaceship.x, self.spaceship.y, self.width))

    return keyboard_events
