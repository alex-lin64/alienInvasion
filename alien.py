import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class respresents single alien in fleet"""
	
	def __init__(self, settings, screen):
		"""Initializes alien attributes and sets position"""
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load('images/trump_face.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
	def update(self):
		"""Moves alien right"""
		self.x += (self.settings.alien_speed * self.settings.direction)
		self.rect.x = self.x
		
	def check_edges(self):
		"""Check edge collisions"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	def blitme(self):
		"""Draws the alien"""
		self.screen.blit(self.image, self.rect)

