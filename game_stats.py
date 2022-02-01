class Game_Stats():
	"""The statistics for Alien Invasion"""
	
	def __init__(self, settings):
		"""Initializes stats"""
		self.settings = settings
		self.reset_stats()
		self.game_status = False
		self.high_score = 0
		
	def reset_stats(self):
		"""Resets stats / re inits the attribute"""
		self.num_lives = self.settings.max_lives
		self.score = 0
		self.level = 1
