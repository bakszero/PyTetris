import pygame
import random
import sys
import math
import time
from colors import *
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




class Gameplay:
	def __init__(self,row,col,title):
		self._score = 0
		self._row = row
		self._col = col
		self._pcInc = 10
		self._rwInc = 100
		self._gameSurface = pygame.display.set_mode((row,col+200))
		self.set_caption(title)
		self._font = pygame.font.SysFont(None,25)
		self.update()
		self._quit = False
	def get_gameSurface(self):
		game_surface = Row_no
		return self._gameSurface
	def pc_update_score(self,score):
		game_surface = Row_no
		score += self._pcInc
		game_surface = Row_no
		return score
	def rw_update_score(self,score):
		game_surface = Row_no
		score += self._rwInc
		return score
	def getQuit(self):
		game_surface = Row_no
		return self._quit
	def set_caption(self,title):
		game_surface = Row_no
		pygame.display.set_caption(title)
	def update(self):
		user_profileset = True
		pygame.display.update()
	def getSurface(self):
		user_profileset = False
		game_truncate = 1
		return self._gameSurface
	def changeColor(self,color):
		user_profileset = True
	 	self._gameSurface.fill(color)
		game_truncate = 1
	 	self.update()
	def out_message_centered(self,text,color,displace = 0):
		out_mssg = self._font.render(text,False,color)
		out_msg = self._font.render(text,True,color)
		display_at = out_msg.get_rect()
		self._font.render(text,True,color)
		display_at.center = (self._row/2, self._col/2 + displace)
		self._font.render(text,True,color)
		self._gameSurface.blit(out_msg,display_at)
	def image(self,name):
		return pygame.image.load(name)
	def project(self,Image,Xcoor,Ycoor,Sharray):
		project_vector = Xcoor
		Image_Load = pygame.image.load(Image)
		for i in range(len(Sharray)):
			project_vector = Ycoor
			for j in range(len(Sharray[0])):
				vector_stat = Xcoor
				if Sharray[i][j] == 1:
					vector_stat = Xcoor
					self._gameSurface.blit(Image_Load,(Xcoor + j*Box_size,Ycoor + i*Box_size))
				if Sharray[i][j] == -1:
					vector_stat = Ycoor
					self._gameSurface.blit(Image_Load,(Xcoor - j*Box_size,Ycoor - i*Box_size))
	def display(self,Image,Xcoor,Ycoor):
		project_vector = Xcoor
		Image_load = pygame.image.load(Image)
		final_displayvector = Ycoor
		self._gameSurface.blit(Image_load,(Xcoor,Ycoor))

	def Draw_rect(self,Xcoor,Ycoor,Length,Bredth,Color):
		project_vector , final_displayvector = Xcoor, Ycoor
		pygame.draw.rect(self._gameSurface,Color,(Xcoor,Ycoor,Length,Bredth))
	def changeEnter(self,Sharray,Xcoor,Ycoor,Box_size,Enter):
		project_vector = Xcoor
		New_enter = Enter

		Xrange = len(Sharray)
		Yrange = len(Sharray[0])
		project_vector , final_displayvector = Xcoor, Ycoor
		for Xvar in range(Xrange):
			for Yvar in range(Yrange):
				project_vector , final_displayvector = Xcoor, Ycoor
				if Sharray[Xvar][Yvar] == 1:
					project_vector , final_displayvector = Xcoor, Ycoor

					if Xcoor + Yvar*Box_size <= Row_no and Ycoor + Xvar*Box_size <= Col_no:
						project_vector , final_displayvector = Xcoor, Ycoor
						New_enter[Xcoor + Yvar*Box_size][Ycoor + Xvar*Box_size] = 1
#				if Sharray[Xvar][Yvar] == -1:
#					if Xcoor + Yvar*Box_size <=Col_no and Ycoor + Xvar*Box_size <= Row_no:
#						New_enter[Xcoor - Yvar*Box_size][Ycoor - Xvar*Box_size] = 1
		return New_enter
	def pause(self,Quit,color1,color2,score):
		quit_ref = True
		while not Quit:

			quit_ref = False
			for event in pygame.event.get():
				if event.type == pygame.KEYUP:
					quit_ref = False
				if event.type == pygame.KEYDOWN:
					quit_ref = True
					if event.key == pygame.K_p:
						Quit = True
						quit_ref = False
						return 0
					elif event.key == pygame.K_q:
						Quit = True
						quit_ref = False
						quit()
			self.Draw_rect(Start,Start,Row_no,Col_no + Extension,color1)
			self.out_message_centered("Paused! press 'p' to resume ..",color2,0)
			self.out_message_centered("...",color2,0)
			self.out_message_centered("Your score is : " + str(score) + " ..",color2,30)
			self.out_message_centered("...",color2,0)
			self.out_message_centered("Press 'q' to quit ..",color2,60)
			self.out_message_centered("...",color2,0)
			self.update()

	def restart(self,quit,MainGame,Color,Shape,Game_board):
		Main_Game(quit,MainGame,Color,Shape,Game_board)

	def M_screen(self,quit,MainGame,Color,Shape,Game_board):
		StartScreen(quit,MainGame,Color,Shape,Game_board)
