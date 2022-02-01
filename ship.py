import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	
	def __init__(self, settings, screen):
		"""Initializes ship and sets starting position"""
		self.screen = screen
		super(Ship, self).__init__()
		
		#Load ship image, get rect, init 
		self.image = pygame.image.load('images/b_obama.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.settings = settings
		
		#Starts 'ship' at bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update ship's position"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.settings.ship_speed
		
		self.rect.centerx = self.center
		
	def blitme(self):
		"""Draws the ship at current location"""
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		"""Centers the ship"""
		self.center = self.screen_rect.centerx
