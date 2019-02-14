import math, numpy, random 
from time import sleep
import pygame
pygame.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0; YELLOW = 255, 255, 0

screen = pygame.display.set_mode((1024, 768))

#used for updating the aiming system bar on the left
left = pygame.Rect(0, 0, 40, 768) 

screen.fill(WHITE)

class Target(object):
	def __init__(self):
		ranx = random.randint(600, 900) #left
		rany = random.randint(100, 600) #top
		self.rect = pygame.Rect(ranx, rany, 40, 10)
		screen.fill(BLACK, self)

	def contact(self, point):
		if self.rect.colliderect(point):
			screen.fill(YELLOW, self)
target = Target()

def aim():

	#initial aiming angle (radians)
	global angle
	angle = 1.37340077 
	degree = math.pi / 180 
	up = 0
	
	while True:
		pygame.event.pump()
		keys = pygame.key.get_pressed()
		aimbox = pygame.Rect(20, 300 - (up*15) , 15, 15)
		screen.fill(BLACK, aimbox) 

		#visual representation of the angle changing
		if keys[pygame.K_UP]:
			up += 1
			angle += degree
			sleep(0.25)
		if keys[pygame.K_DOWN]:
			up -= 1
			angle -= degree
			sleep(0.25)
		if keys[pygame.K_RETURN]:
			screen.fill(WHITE, left); pygame.display.update() 
			break
		pygame.display.update()  

def arc():

	#split the speed into its components
	M = 100
	vx = M * math.cos(angle) 
	vy = M * math.sin(angle)

	#draw the arc according to kinematic equations
	time = numpy.arange(0.0, 30.0, 0.1)
	for sec in time:
		x = int(vx * sec + 200) 
		y = int(-vy * sec + 0.5 * 9.81 * sec**2 + 600) 
		
		point = pygame.Rect(x, y, 2, 2)
		screen.fill(BLACK, point)

		#check for contact
		target.contact(point) 
		pygame.display.update() 

#game loop
while True:
	aim()
	arc()