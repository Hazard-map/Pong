import sys

import pygame
from pygame.locals import *

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# sizes
SCREEN_SIZE = (400, 300)


class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set_position(self, *position):
		length = len(position)
		if length == 2:
			self.x = position[0]
			self.y = position[1]
		elif length == 1 and type(position[0]) == Position:
			p = position[0]
			self.x = p.x
			self.y = p.y
		else:
			raise Exception("wrong argument")

	def get_postion(self):
		return (self.x, self.y,)


class Ball:
    speed = 10
    color = WHITE
    width = 10
    height = 90

    def __init__(self, pos):
        self.pos = pos
    
    def _update_postion(self, key):
        ...

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.pos + (height, width))


def draw_two_rectangles(screen):
	pygame.draw.rect(screen, WHITE, (20, 70, 10, 180))
	pygame.draw.rect(screen, WHITE, (370, 70, 10, 180))


def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)

	while True:
		screen.fill(BLACK)

		draw_two_rectangles(screen)

		pygame.display.update()

		for event in pygame.event.get():
			# 閉じるボタンおしたら終了する
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


if __name__ == '__main__':
	main()

