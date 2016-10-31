import pygame
import random
import sys
import math
import time

pygame.init()

Row_no = 300
Rows_no = 350
Col_no = 320
randomShape_req = 1
Cols_no = 500
Name = "Global Tetris"
FPS = 10
clock_taken = pygame.time.Clock()
BackgroundImage = '1.jpg'
BackgroundImage_bg = '2.jpg'
#BackgroundImage2 = 'rsz_c29bf435b98b.jpg'
ShapeImage = 'block.png'
StartImage3 = 'block.png'
StartImage = '2.jpg'
Gameover = '3.jpg'
InstructionScreen = '4.jpg'



clock_used = pygame.time.Clock()
Box_size = 10
Coor = []
Ends_block = 0
Score_displace = 250
Images_displace = 230
Extension = 200
End_extension = 0
Start = 0


class Colors:
	def __init__(self):
		self._init = 1

	def getNavy(self):
		self._navy = (160, 160, 0)
		return self._navy
	def getRed(self):
		self._red = (255,0,0)
		return self._red

	def getGreen(self):
		self._green = (0,255,0)
		return self._green

	def getDarkRed(self):
		self._darkred =(255,100, 0)
		return self._darkred
	def getLightBlue(self):
		self._lightBlue = (0,0,100)
		return self._lightBlue
	def getDarkGreen(self):
		self._darkgreen = (50, 255, 0)
		return self._darkgreen
	def getBlue(self):
		self._blue = (0,0,255)

		return self._blue
	def getGrey(self):
		self._grey = (10, 10, 10)
		return self._grey
	def getBlack(self):
		self._black =  (0,0,0)
		return self._black
	def getWhite(self):
		self._white = (255,255,255)
		return self._white
