import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class manages bullets fired from ship"""
	
	def __init__(self, settings, screen, ship):
		"""Creates bullet object"""
		super().__init__()
		self.screen = screen
		
		#Create bullet rect at origin, sets correct position
		rect = pygame.Rect(0, 0, settings.bullet_w, settings.bullet_h)
		self.rect = rect
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#Store bullet's decimal y-value
		self.y = float(self.rect.y)
		
		self.color = settings.bullet_color
		self.speed = settings.bullet_speed

	def update(self):
		"""Moves bullet up the screen"""
		self.y -= self.speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draws bullet to screen"""
		pygame.draw.rect(self.screen, self.color, self.rect) 
