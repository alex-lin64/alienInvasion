import pygame.font


class Scoreboard():
	"""Scoreboard to represent number of aliens killed"""
	
	def __init__(self, screen, settings, stats):
		"""Inits atrributes"""
		self.screen = screen
		self.settings = settings
		self.screen_rect = screen.get_rect()
		self.stats = stats
		
		#Font settings
		self.txt_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 40)
		self.font_two = pygame.font.SysFont(None, 32)
		
		self.score_prep()
		self.prep_high_score()
		self.prep_level()
		
	def score_prep(self):
		"""Renders the scoreboard"""
		score_str = "{:,}".format(self.stats.score)
		self.score_image = self.font_two.render(score_str, True, 
			self.txt_color, self.settings.bg_color)
		
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def draw_score(self):
		"""Draws score to game"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		
	def prep_high_score(self):
		"""Renders high score"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.txt_color, self.settings.bg_color)
			
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top

	def prep_level(self):
		"""Renders the level"""
		self.level_image = self.font_two.render(str(self.stats.level), 
			True, self.txt_color, self.settings.bg_color)
		
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.right = self.screen_rect.right - 20
		self.level_image_rect.top = self.score_rect.bottom + 10
