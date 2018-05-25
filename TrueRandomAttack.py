import GameObject
import random
import time
import Block
import Renderer
import AttackUnitMover as AUM

gameObject = GameObject.GameObject()
red = (255,0,0)
display_width = 800
display_height = 600

class AttackBlock(Block.Block):
	def __init__(self, direction, speed):
		self.color = red
		self.direction = direction
		self.speed = speed
		self.x = 0
		self.y = 0
		self.end_x = 0
		self.end_y = True
		self.isActive = True
		self.renderer = Renderer.Renderer()
		self.aum = AUM.AttackUnitMover()

		self.top_side_attack_config = []
		self.left_side_attack_config = []
		self.bottom_side_attack_config = []
		self.right_side_attack_config = []

		self.create_attack_config()

	def create_attack_config(self):
		if(self.direction == "top"):
			self.top_side_attack_config = [self.create_top_attack(), 0, 10, 10]
			self.end_x = self.top_side_attack_config[0]
			self.end_y = gameObject.display_height
		elif(self.direction == "left"):
			self.left_side_attack_config = [0, self.create_left_attack(), 10, 10]
			self.end_x = gameObject.display_width
			self.end_y = self.left_side_attack_config[1]
		elif(self.direction == "bottom"):
			self.bottom_side_attack_config = [self.create_bottom_attack(), gameObject.display_height-10, 10, 10]
			self.end_x = self.bottom_side_attack_config[0]
			self.end_y = self.bottom_side_attack_config[1] - gameObject.display_height -10
		else:
			self.right_side_attack_config = [gameObject.display_width-10, self.create_right_attack(), 10 , 10]
			self.end_x = self.right_side_attack_config[0] - gameObject.display_width - 10
			self.end_y = self.right_side_attack_config[1]

	

	def create_top_attack(self):
		top_attack_startx = random.randrange(0, gameObject.display_width)
		return top_attack_startx

	def create_bottom_attack(self):
		bottom_attack_startx = random.randrange(0, gameObject.display_width)
		return bottom_attack_startx

	def create_left_attack(self):
		left_attack_starty = random.randrange(0, gameObject.display_height)
		return left_attack_starty

	def create_right_attack(self):
		right_attack_starty = random.randrange(0, gameObject.display_height)
		return right_attack_starty

	def update_attack_block_coordinates(self):
		self.aum.initialize(self)
		self.aum.move()

	#create/update new attack block position 
	def update_attack_block_position(self, pgm, gameDisplay, color):
		self.renderer.initialize(self, pgm, gameDisplay, color, None, None)
		self.renderer.render_object()

	def damage(self, player):
		if(self.isActive == True):
			if(player.player_x > self.x and player.player_x < self.x + 10 or player.player_x + 10 > self.x and player.player_x + 10 < self.x + 10):
				if(player.player_y > self.y and player.player_y < self.y + 10):
					player.health -= 5
					#print(player.player_x, " ", self.x, " ", player.player_y, " ", self.y, " : ", player.health)
					self.isActive = False
				elif(player.player_y + 10 > self.y and player.player_y + 10 < self.y + 10):
					player.health -= 5
					#print(player.player_x, " ", self.x, " ", player.player_y, " ", self.y, " : ", player.health)
					self.isActive = False

