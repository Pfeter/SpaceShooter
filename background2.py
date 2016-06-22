import random, pygame

class Background(object):
    def generate_stars(self, stars, width, height):
        return [[random.randint(0, width), random.randint(0, height)] for i in range(stars)]

    def draw_stars(self, stars, background, width, height):
        for star in stars:
            pygame.draw.line(background, (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = width
                star[1] = random.randint(0, height)
