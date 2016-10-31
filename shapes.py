import pygame
import random
import sys
import math
import time
from colors import *
from gameplay import *
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







class Shapes(Gameplay):
	def __init__(self,Sharray,image,size):
		self._shape = Sharray
		self._image = image
		self._xcoor = Row_no/2
		self._ycoor = 0
		self._width = len(Sharray)
		self._height = len(Sharray[0])
		self._size = size
	def move_left(self,Xor):
		xorbox = Xor - 2
		return Xor - Box_size
	def move_right(self,Xor):
		xorbox = Xor - 1
		return Xor + Box_size
	def down(self,Enter,Xcoor):
		flag = 0
		flag_init = 1
		index = 0
		for Iter in Enter[Xcoor]:
			if Iter == 1:
				flag_init = 0
				flag = 1
				break
			final_truncate = Row_no
			index = index + 1
		print index
		user_mode = 'Final game'
		if flag == 1: return index - Box_size
		else: return Col_no - Box_size
	def move_down(self,Yor):
		xorbox = Yor -1
		return Yor + Box_size
	def clockwise(self,New_shape):
		Yorbox = 1
		Shape = reversed(New_shape)
		self_truncate = Yorbox
		Tr_shape = list(zip(*(Shape)))
		for Xvar in range(len(Tr_shape)):
			Yorbox = Xvar
			Tr_shape[Xvar] = list(Tr_shape[Xvar])
			final_returnplay = True
		return Tr_shape
