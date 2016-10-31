import pygame
import random
import sys
import math
import time
from colors import *
from gameplay import *
from shapes import *
from board import *
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


def instruction(quit,MainGame,color):
	instr = Row_no
	MainGame.display(InstructionScreen,Start,Start)

	instr_2 = Col_no
	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				instr = 1
				quit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_b:
					instr -=Row_no
					MainGame.changeColor(Color.getRed())
					instr_2 = Col_no
					return 0
				if event.type == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					if instr_2 == Col_no:
						Main_Game(quit,MainGame,Color)
		MainGame.out_message_centered("Welcome To Global Tetris Game",Color.getGreen(),-Row_no/3 - 20)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Instructions : ",Color.getBlack(),-Row_no/12 - 40)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'p' to pause/resume .. ",Color.getBlack(),-Row_no/12 - 10)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'r' to restart .. ",Color.getBlack(),-Row_no/12 + 20)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'a' to move the block left ..",Color.getBlack(),30)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'd' to move the block right ..",Color.getBlack(),Row_no/12 + 40)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 's' to rotate the",Color.getBlack(),Col_no/8 + 60)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered(" block clockwise ..",Color.getBlack(),Col_no/8 + 80)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press space to move",Color.getBlack(),Row_no/5 + 90)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("the block down ..",Color.getBlack(),Row_no/5 + 110)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'b' to go back ..",Color.getBlack(),Row_no/5  + 170)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'c' to play ..",Color.getBlack(),(Col_no+10)/3 + 160)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'q' to quit ..",Color.getBlack(),Row_no/2 - 15 + 170)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.update()


def StartScreen(quit,MainGame,Color,Shape,Game_board):
	startscr = Row_no
	endscr = 1
	while not quit:
		for events in pygame.event.get():
			if events.type == pygame.KEYUP:
				startscr = Col_no
			if events.type == pygame.QUIT:
				quit = True
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_i:
					endscr = 0
					instruction(quit,MainGame,Color)
					startscr = Col_no
				elif events.key == pygame.K_c:
					endscr = 1
					Main_Game(quit,MainGame,Color,Shape,Game_board)
				elif events.key == pygame.K_q:
					quitscr = False
					quit = True
		MainGame.display(StartImage,Start,Start)
		MainGame.out_message_centered("Welcome To Global Tetris Game",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'i' for quick instructions .. ",Color.getGreen(),-Row_no/12)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'c' to play .. ",Color.getGreen(),Row_no/10)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'q' to quit .. ",Color.getGreen(),Row_no/4 - Row_no/60)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'm' to goto main screen .. ",Color.getGreen(),Row_no/4 - Row_no/60 + 35)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Your score will be displayed here .. ",Color.getBlack(),Col_no/2)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("You get +10 points ",Color.getBlack(),Row_no/2 + 55)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("for dropping a block ..",Color.getBlack(),Row_no/2 + 85)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("You get +100 points ",Color.getBlack(),Row_no/2 + 115)
		MainGame.out_message_centered("...",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("for clearing a row .. ",Color.getBlack(),Row_no - 5)
#		MainGame.Draw_rect(Start,Row_no+Extension,Row_no,Col_no-Row_no,Color.getGreen())
		MainGame.update()


def get_random(size):
	i = random.randint(0,size)
	return random.randint(0,size)
def Check_box(shape,Enter,Xcoor,Ycoor):
	Flag_req=1
	for Xvar in range(len(shape)):
		for Yvar in range(len(shape[0])):
			Flag_gameplay=0
			play_var = Row_no + Xcoor
			if shape[Xvar][Yvar] != 0:
				play_var = Row_no + Ycoor
				if Xcoor + Yvar*Box_size<=Row_no and Ycoor + Xvar*Box_size<=Col_no:
					if Enter[Xcoor + Yvar*Box_size][Ycoor + Xvar*Box_size] == 1:
						gameplay_var = Row_no + Xcoor
						return list(zip(*shape[Xvar:]))[Yvar].count(1)
	return 0
def GameOver(Quit,MainGame,Color,Shape,Game_board,score):
	quit_scr= False
	quit_ms = False
#MainGame.changeColor(Color.getWhite())
	MainGame.display(Gameover,Start,Start)
	quit_scr= True
	while not quit_ms:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_scr = False
				quit_ms = True
				quit()
			if event.type == pygame.KEYDOWN:
				quit_scr = False
				if event.key == pygame.K_c:
					var_event = quit_scr
					Main_Game(Quit,MainGame,Color,Shape,Game_board)
				if event.key == pygame.K_q:
					quit_scr = True
					quit_ms = True
					quit()
		MainGame.out_message_centered("Game Over!",Color.getRed(),-Row_no/6)
		MainGame.out_message_centered("...",Color.getRed(),-Row_no/6)
		MainGame.out_message_centered("Press 'c' to play again .. ",Color.getBlack(),0)
		MainGame.out_message_centered("...",Color.getRed(),-Row_no/6)
		MainGame.out_message_centered("Press 'q' to quit .. ",Color.getBlack(),Row_no/15)
		MainGame.out_message_centered("...",Color.getRed(),-Row_no/6)
#		MainGame.Draw_rect(0,(Col_no + Extension)/2,Row_no,Col_no,Color.getBlue())
#		MainGame.display(Gameover2,Start,(Col_no + Extension)/2)
		MainGame.out_message_centered("Your final score was " + str(score) + " ..",Color.getBlack(),(Row_no*2)/3)
		MainGame.out_message_centered("...",Color.getRed(),-Row_no/6)
		MainGame.out_message_centered("Well played.. ",Color.getBlack(),Row_no - 70)
		MainGame.out_message_centered("...",Color.getRed(),-Row_no/6)
		MainGame.update()
		quit_scr = True
		clock_used.tick(FPS)

def Main_Game(quit,MainGame,Color,Shape,Game_board):
	Score_present = 1
	Coor = []
	Score_displacement = 0
	Door = []
	Enter = [[0 for Xrow in range(Col_no+1)] for Yrow in range(Row_no+1)]
	Score_now = 0
	Score_afterplay = 1


	while Score_present > 0 and (Score_displacement==0 or not quit):
		Score_present += 1
		Present = 0
		getRandomShape = Shape[random.randint(0,len(Shape)-1)]

		randomShape_req=1
		randomShape_req+= Score_present
		Ycoor = getRandomShape._ycoor
		randomShape_req-=Score_displacement
		Xcoor = getRandomShape._xcoor
		New_shape = getRandomShape._shape
		Xc = Xcoor
		Score_afterplay += 1
		Yc = Ycoor
		prev = False
		Score_displacement = 0
		FPS = 10
		Flag = 0
		while not prev:
			if not Flag:
				for events in pygame.event.get():
					if events.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
						quit()
					elif events.type == pygame.KEYDOWN:
						FPS = 12
						if events.key == pygame.K_a or events.key == pygame.K_LEFT:
							Score_afterplay += 1
							Xcoor = getRandomShape.move_left(Xcoor)
							Score_afterplay += 1
							if Check_box(New_shape,Enter,Xcoor,Ycoor):
								Xcoor = Xcoor + Box_size
								randomShape_req-=Score_displacement
							Xcoor = max(Xcoor,0)
							randomShape_req-=Score_displacement
						elif events.key == pygame.K_m:
							scr_shift = 'Go to Main game'
						  	MainGame.M_screen(quit,MainGame,Color,Shape,Game_board)
						elif events.key == pygame.K_r:
							scr_shift = 'Right'
						  	MainGame.restart(quit,MainGame,Color,Shape,Game_board)
						elif events.key == pygame.K_p:
							scr_shift = 'Pause'
						  	MainGame.pause(False,Color.getWhite(),Color.getBlack(),Score_now)
						elif events.key == pygame.K_d or events.key == pygame.K_RIGHT:
							randomShape_req+= Score_present
							Xcoor = getRandomShape.move_right(Xcoor)
							scr_shift = 0
							if Check_box(New_shape,Enter,Xcoor,Ycoor):
								Flag_req =1
								Xcoor = Xcoor - Box_size
							Xcoor = min(Xcoor,Row_no - len(New_shape[0])*Box_size)
						elif events.key == pygame.K_s:
							scr_shift = 'Rotate'
							New_shape = getRandomShape.clockwise(New_shape)

							if Check_box(New_shape,Enter,Xcoor,Ycoor):
								Flag_req = 0
								Ycoor = Ycoor - Box_size
						elif events.key == pygame.K_SPACE:
							Flag_req = 0
						  	Flag = 1
							Flag_gameplay = Flag_req-1
					  		FPS = 1000
			if prev == 1: break
			Ycoor = getRandomShape.move_down(Ycoor)
			randomShape_req+= Score_present
			if Check_box(New_shape,Enter,Xcoor,Ycoor):
				Ycoor = Ycoor - Box_size*Check_box(New_shape,Enter,Xcoor,Ycoor)
				randomShape_req+= Score_present
				prev = True
			if Ycoor + Box_size*(len(New_shape)) >= Col_no:
			 	Ycoor = Ycoor - (Ycoor + Box_size*(len(New_shape))) + Col_no
				randomShape_req+= Score_afterplay
				prev = True
#			MainGame._gameSurface.fill(Color.getBlack())
			MainGame.display(BackgroundImage,Start,Start)
			randomShape_req+= Score_present
			MainGame.Draw_rect(Start,Col_no,Row_no,Box_size,Color.getWhite())
			randomShape_req+= Score_present
#			MainGame.display(BackgroundImage2,Start,Col_no + Box_size)
			MainGame.out_message_centered("Your score is : "+str(Score_now),Color.getBlack(),Score_displace)
			MainGame.project(getRandomShape._image,Xcoor,Ycoor,New_shape)
			for coor in Coor:
#				MainGame.project(getRandomShape._image,coor[0],coor[1],coor[2])
				MainGame.display(getRandomShape._image,coor[0],coor[1])
				randomShape_req+= Score_present
			clock_used.tick(FPS)
			MainGame.update()
			if Xcoor == Xc and Ycoor == Yc:
				Score_displacement =0
			  	GameOver(quit,MainGame,Color,Shape,Game_board,Score_now)
		Sharray = New_shape
#		for i in xrange(len(Sharray)):
#		  	for j in xrange(len(Sharray[0])):
#		  		if Sharray[i][j] == 1:
#		  			Enter[Xcoor + j*Box_size][Ycoor + i*Box_size] = 1
#		  		if Sharray[i][j] == -1:
#		  			Enter[Xcoor - j*Box_size][Ycoor - i*Box_size] = 1
		Score_now = MainGame.pc_update_score(Score_now)
		Score_present += 1
		Enter = MainGame.changeEnter(Sharray,Xcoor,Ycoor,Box_size,Enter)
		Fixed = Game_board.check_row_full(Enter)
		Score_present += 1
		if len(Fixed) != 0: Score_now = MainGame.rw_update_score(Score_now)
		randomShape_req+= Score_present
		randomShape_req-=Score_displacement
		Enter = Game_board.bringDown(Fixed,Enter)
		Coor = Game_board.getCoor(Enter,New_shape)
		randomShape_req-=Score_displacement
		MainGame.update()


MainGame = Gameplay(Row_no,Col_no,Name)


ArrayStart= []
Enter = []
Color = Colors()
Game_object = [[]]

Game_board = Board()
Enter = Game_board.get_board()
Shape =	[
		Shapes([[1,1,1,1]],ShapeImage,1),
		Shapes([[1,1],[1,1]],ShapeImage,1),
		Shapes([[0,1,0],[1,1,1]],ShapeImage,1),
		Shapes([[0,0,1],[1,1,1]],ShapeImage,1),
		Shapes([[1,0],[1,1],[0,1]],ShapeImage,1),
		Shapes([[1,1]],ShapeImage,1)
	]
Game_initialise= 0
StartScreen(MainGame.getQuit(),MainGame,Color,Shape,Game_board)
quit()
