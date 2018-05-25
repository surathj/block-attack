import pygame as pg
import Renderer


class Player():
	def __init__(self):
		self.player_id = None
		self.player_x = 300
		self.player_y = 300
		self.player_lead_x_change = 0
		self.player_lead_y_change  =0
		self.player_class = 0.14026667
		#self.ammo = ammo

		self.time_lasted = 0
		self.average_performance = 0

		#Possible Feature variables
		self.health = 100
		self.score = 0	#measures endurance
		self.class_packs = 0	#measures agility
		#apply game rules, violation of which will cost something
		#resourcefulness
		#ammo and shields
		self.renderer = Renderer.Renderer()

	def draw_player_block(self, pgm, gameDisplay, color, config_list):
		self.renderer.initialize(self, pgm, gameDisplay, color, config_list, None)
		self.renderer.render_object()

	def check_health(self):
		if(self.health == 0):
			return 1

	def calculate_endurance(self):
		self.endurance = 0
		pass

