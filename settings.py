class Settings():
	"""Stores Alien Invasion settings"""
	
	def __init__(self):
		"""Initializes game settings"""
		self.screen_l = 1200
		self.screen_w = 800
		self.bg_color = (255, 255, 255)
		
		#bullet settings
		self.bullet_w = 3
		self.bullet_h = 14
		self.bullet_color = 30, 60, 30
		self.bullets_max = 10

		#alien settings
		self.drop_speed = 10
		self.max_lives = 2

		#Leveling scale
		self.speed_increase = 1.1
		self.init_dynamic_settings()
		self.score_scale = 1.5
		
	def init_dynamic_settings(self):
		"""Initializes dynamic settings"""
		self.ship_speed = 1.5
		self.bullet_speed = 2.5
		self.alien_speed = .5
		self.direction = 1
		self.alien_points = 10
		
	def increase_speed(self):
		"""Increases speed of game per level"""
		self.ship_speed *= self.speed_increase
		self.bullet_speed *= self.speed_increase
		self.alien_speed *= self.speed_increase
		self.alien_points = int(self.alien_points * self.score_scale)
	
