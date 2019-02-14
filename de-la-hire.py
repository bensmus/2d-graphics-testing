#math window: center is 0,0 w/ x y axis

import math
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
WHITE = 255, 255, 255; BLACK = 0, 0, 0
GREEN = 51, 204, 51; PURPLE = 204, 51, 255
elipsss = []

def m(l): #math window
	s = [300, 300]
	s[0] += l[0]
	s[1] -= l[1]
	return s #standard window

x1 = 200; x2 = -200; i = -1; h = 1
while True: #continuously spin
	for x in range(x1, x2, i): #semicircle

		clock = pygame.time.Clock()
		screen.fill(WHITE)

		pygame.draw.line(screen, BLACK, m([-300,0]), m([300, 0])) #x-axis
		pygame.draw.line(screen, BLACK, m([0,300]), m([0, -300])) #y-axis

		pygame.draw.circle(screen, BLACK, m([0,0]), 200, 1)
		pygame.draw.circle(screen, BLACK, m([0,0]), 100, 1)

		y1 = math.sqrt(200 ** 2 - x ** 2) * h
		pygame.draw.line(screen, GREEN, m([0,0]), m([x, y1]))
		pygame.draw.line(screen, GREEN, m([x, y1]), m([x, 0]))

		y2 = math.sqrt(100 ** 2 - (x/2) ** 2) * h
		pygame.draw.line(screen, GREEN, m([x/2, y2]), m([x/2, 0]))

		elipsss.append([x, int(y2)])
		for point in elipsss:
			pygame.draw.circle(screen, PURPLE, m(point), 2, 1)

		pygame.display.update()
		clock.tick(20)

	#cover all quadrants; e.g 3, 4
	x1 = x1 * -1
	x2 = x2 * -1
	i = i * -1
	h = h * -1
