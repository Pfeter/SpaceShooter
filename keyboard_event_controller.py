import pygame
from pygame.locals import *

def keyboard_event_controller(press, direction, bullet_fire, last_bullet_ticks):
    keyboard_events = [direction, bullet_fire, last_bullet_ticks]

    if press[pygame.K_UP]:
        keyboard_events[0][0] = True
    else:
        keyboard_events[0][0] = False
    if press[pygame.K_DOWN]:
        keyboard_events[0][1] = True
    else:
        keyboard_events[0][1] = False
    if press[pygame.K_RIGHT]:
        keyboard_events[0][2] = True
    else:
        keyboard_events[0][2] = False
    if press[pygame.K_LEFT]:
        keyboard_events[0][3] = True
    else:
        keyboard_events[0][3] = False

    # if press[pygame.K_SPACE]:
    #     keyboard_events[1] = True
    # else:
    #     keyboard_events[1] = False
    #     keyboard_events[2] = 0
    # if press[pygame.K_a]:
    #     self.projectiles.append(Bomb(self.spaceship.x, self.spaceship.y))
    # if press[pygame.K_s]:
    #     self.lasers.append(Laser(self.spaceship.x, self.spaceship.y, self.width))

    return keyboard_events
