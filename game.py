import pygame as pg
import time
import random
from multiprocessing import Process

#custome files
import GameObject
import Player
import TrueRandomAttack as tra
import AttackWaves as atw
import ClassPack as cp

pg.init()
pg.font.init()
display_width = 800
display_height = 600

gameObject = GameObject.GameObject()
colors = GameObject.Colors()


#display x,y
gameDisplay = pg.display.set_mode((display_width, display_height)) 
pg.display.set_caption('Block Hunger Games')


font = pg.font.SysFont(None, 25)


def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [gameObject.display_width/2, gameObject.display_height/2])

def load_message():
	screen_text = font.render("Please wait while the game loads", True, (255,0,0))
	gameDisplay.blit(screen_text, [gameObject.display_width/2, gameObject.display_height/2])



now = time.time()
future = now + 2
def gameloop():
	white = (255,255,255)
	black = (0,0,0)
	red = (255,0,0)

	#pg.display.update()
	gameExit = False
	gameOver = False
	
	
	clock = pg.time.Clock()
	FPS = 30


	#creating player object
	player = Player.Player()
	#creating single classpack
	classPack = cp.ClassPack(pg, gameDisplay, player)
	
	waves = []
	loading_done = False

	
	for i in range(10):
		new_atw = atw.Attack_Wave(pg, gameDisplay, colors.red, 2)
		new_atw.generate_wave()
		waves.append(new_atw)


	'''
	The Game loop starts here
	'''
	#game loop
	while not gameExit:
		#update block positions to simulate movement
		for i in waves:
			i.update_wave_coordinates()


		while gameOver == True:
			gameDisplay.fill(colors.white)
			message_to_screen("Game Over! Press C to play again or Q to quit!", red)
			pg.display.update()

			for event in pg.event.get():
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_q:
						gameExit = True
						gameOver = False
					if event.key == pg.K_c:
						now = time.time()
						gameloop()


		#game event loop
		for event in pg.event.get():
			if event.type == pg.QUIT:
				gameExit = True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					player.player_lead_x_change = -10
					#lead_y_change = 0	# to avoid diagonal movement
				elif event.key == pg.K_RIGHT:
					player.player_lead_x_change = 10
					#lead_y_change = 0
				elif event.key == pg.K_UP:
					player.player_lead_y_change = -10
					#lead_x_change = 0
				elif event.key == pg.K_DOWN:
					player.player_lead_y_change = 10
					#lead_x_change = 0
					
			#allow keyup to stop x,y movement
			if event.type == pg.KEYUP:
				if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
					player.player_lead_x_change = 0
				if event.key == pg.K_UP or event.key == pg.K_DOWN:
					player.player_lead_y_change = 0
				#print(event)

			#boudary logic
			if(player.player_x >= display_width or player.player_x < 0 or player.player_y >= display_height or player.player_y < 0):
				gameOver = True
		
		#update player position
		player.player_x += player.player_lead_x_change
		player.player_y += player.player_lead_y_change

		gameDisplay.fill(colors.white)

		#player block
		player.draw_player_block(pg, gameDisplay, black, [player.player_x, player.player_y, gameObject.player_block_width, gameObject.player_block_height])
		classPack.draw_cpack()


		# for i in waves:
		# 	i.update_wave_positions()
		# 	result = i.damage_player(player)
		# 	if(result == 1):
		# 		gameOver = True
		# 		print(gameOver)


		pg.display.update()
	
		
		#increase amount of pixels moved and reduce fps clocking
		#balance fps and x,y _change
		#current: 30 fps, 10 px/s
		clock.tick(gameObject.FPS)
	
	'''message_to_screen("You Lose", red)
	pg.display.update()
	time.sleep(2)'''		
	#pg.quit()
	quit()
if __name__ == '__main__':
	gameloop()