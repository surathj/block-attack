import TrueRandomAttack as TRA

class AttackUnitMover:
	def initialize(self, obj):
		self.obj = obj

	def move(self):
		if(isinstance(self.obj, TRA.AttackBlock)):
			if(self.obj.isActive == True):
				if(self.obj.direction == "top"):
					if(self.obj.top_side_attack_config[1] == self.obj.end_y):
						self.obj = None
					else:
						self.obj.lead_top_attack_change = self.obj.speed
						self.obj.top_side_attack_config[1] += self.obj.lead_top_attack_change
						self.obj.x = self.obj.top_side_attack_config[0]
						self.obj.y = self.obj.top_side_attack_config[1]
				elif(self.obj.direction == "left"):
					if(self.obj.left_side_attack_config[0] == self.obj.end_x):
						self.obj = None
					else:
						self.obj.lead_left_attack_change = self.obj.speed
						self.obj.left_side_attack_config[0] += self.obj.lead_left_attack_change
						self.obj.x = self.obj.left_side_attack_config[0]
						self.obj.y = self.obj.left_side_attack_config[1]
				elif(self.obj.direction == "bottom"):
					if(self.obj.bottom_side_attack_config[1] == self.obj.end_y):
						self.obj = None
					else:
						self.obj.lead_bottom_attack_change = self.obj.speed
						self.obj.bottom_side_attack_config[1] -= self.obj.lead_bottom_attack_change
						self.obj.x = self.obj.bottom_side_attack_config[0]
						self.obj.y = self.obj.bottom_side_attack_config[1]
				else:
					if(self.obj.right_side_attack_config[0] == self.obj.end_x):
						self.obj = None
					else:
						self.obj.lead_right_attack_change = self.obj.speed
						self.obj.right_side_attack_config[0] -= self.obj.lead_right_attack_change
						self.obj.x = self.obj.right_side_attack_config[0]
						self.obj.y  =self.obj.right_side_attack_config[1]
