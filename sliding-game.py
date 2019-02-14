from time import sleep
import random
import pygame
pygame.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pygame.display.set_mode((612, 768))
screen.fill(WHITE)
font = pygame.font.SysFont('monospace', 20)

numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

class Blank_Square(object):
	def __init__(self, row, col):

		self.row = row
		self.col = col
		x = 100 + col * 20
		y = 100 + row * 20
		self.rect = pygame.Rect(x, y, 20, 20)

class Number_Square(object):
	def __init__(self, row, col):

		self.row = row
		self.col = col

		randomnumber = random.choice(numbers)
		numbers.remove(randomnumber)
		self.label = font.render(randomnumber, 1, BLACK) #a number displayed on screen in a grid format

	def draw(self):
		x = 100 + self.col * 20
		y = 100 + self.row * 20
		self.rect = pygame.Rect(x, y, 20, 20)	#clickable object
		screen.blit(self.label, (x, y))

	def move(self, blank_square):
		if self.row == blank_square.row and (self.col == blank_square.col + 1 or self.col == blank_square.col - 1):
			#if the number is in the same row as the blank space
			rowf = blank_square.row; colf = blank_square.col
			rowi = self.row; coli = self.col
			self.row = rowf; self.col = colf
			blank_square.row = rowi; blank_square.col = coli

		if self.col == blank_square.col and (self.row == blank_square.row + 1 or self.row == blank_square.row - 1):
			#if the number is in the same coloumn as the blank space
			rowf = blank_square.row; colf = blank_square.col
			rowi = self.row; coli = self.col
			self.row = rowf; self.col = colf
			blank_square.row = rowi; blank_square.col = coli

a = Number_Square(0,0); b = Number_Square(0,1); c = Number_Square(0,2)
d = Number_Square(1,0); e = Number_Square(1,1); f = Number_Square(1,2)
g = Number_Square(2,0); h = Number_Square(2,1); o = Blank_Square(2,2)
grid = [a,b,c,d,e,f,g,h] #an array of number objects

while True:
	screen.fill(WHITE)
	pygame.event.pump()
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
	for n in grid:
		n.draw()
		if n.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
			print('click', n.col, n.row) 
			n.move(o)

	pygame.display.update()
