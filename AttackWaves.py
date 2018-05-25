import TrueRandomAttack as tra
import Timer
import time
import random


directions = ["top", "left", "bottom", "right"]
speeds = [7,8,9,10,11,12]

red = (255,0,0)

#Global functions
def select_random_direction():
	direction = random.choice(directions)
	return direction


def select_random_speed():
	speed = random.choice(speeds)
	return speed


class Attack_Wave():
	def __init__(self, pg, gameDisplay, color, units_per_wave):
		self.pg = pg
		self.gameDisplay = gameDisplay
		self.color = color
		self.wave_isActive = False
		self.units_per_wave = units_per_wave
		self.attack_block_list = []

		self.now = time.time()
		self.future = self.now + random.choice(range(1,5))
		self.generate_wave()

	def generate_wave(self):
		for i in range(self.units_per_wave):
			atb = tra.AttackBlock(select_random_direction(), select_random_speed())
			self.attack_block_list.append(atb)

	def update_wave_coordinates(self):
		if(time.time() >= self.future):
			self.wave_isActive = True
			for i in self.attack_block_list:
					i.update_attack_block_coordinates()

	def update_wave_positions(self):
		if(self.wave_isActive):
			for i in self.attack_block_list:
					i.update_attack_block_position(self.pg, self.gameDisplay, self.color)

	def damage_player(self, player):
		for i in self.attack_block_list:						
			i.damage(player)
			if(player.health <= 0):
				return 1