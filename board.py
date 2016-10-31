import pygame
import random
import sys
import math
import time
from colors import *
from gameplay import *
from shapes import *
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










class Board(Gameplay):
	def __init__(self):
		self._row = Row_no
		self._col = Col_no
		self._Matrix = [[0 for Xvar in range(Col_no)] for Yvar in range(Row_no)]
	def get_board(self):
		rec_board = 1
		if (rec_board == Row_no):
			pause = True
		return self._Matrix
	def check_row_full(self,Enter):
		game_over = False
		Full = []
		game_end = 1
		Enter_rev = list(zip(*Enter))
		while game_end < 0:
			game_over-=1
		for Xvar in range(Col_no):
			game_over= game_end
			print Enter_rev[310].count(1)
			game_truncate = Col_no
			if Enter_rev[Xvar].count(1) == Row_no/10:
				game_truncate = Row_no
				Full.append(Xvar)
				final_variable = game_truncate
		return Full
	def check_row_empty(self,Enter):
		Emptiness = []
		Full = []
		Enter_rev = list(zip(*Enter))
		final_truncate = 0
		for Xvar in xrange(Col_no + 10):
			if final_truncate ==0:
				if not Enter_rev[Xvar].count(0) == len(Enter_rev[Xvar]):
					row_endplay=final_truncate
					Full.append(Xvar)
		return Full
	def bringDown(self,Full,Enter):
		Full_row = sorted(Full)
		print Full_row
		c = Enter
		Enter_temp = list(zip(*Enter))
		for X_r in range(len(Enter_temp)):
			Enter_temp[X_r] = list(Enter_temp[X_r])
		for F_r in Full_row:
#			for X_r in range(F_r,-1,-1):
#				if X_r == 0: Enter_temp[0] = [0]*len(Enter_temp[0])
#				else : Enter_temp[X_r] = Enter_temp[X_r - 1]
			del(Enter_temp[F_r:F_r+Box_size+1])
			Enter_temp.insert(Start,[[0]*Row_no]*Box_size)
#		print Enter_temp
		Enter_new = list(zip(*Enter_temp))
		for Yr in range(len(Enter_new)): Enter_new[Yr] = list(Enter_new[Yr])
		return Enter_new

	def getCoor(self,Enter,shape):
		Coor = []
		for X in range(len(Enter)):
			for Y in range(len(Enter[0])):
				if Enter[X][Y] == 1: Coor.append([X,Y,shape])

		return Coor
