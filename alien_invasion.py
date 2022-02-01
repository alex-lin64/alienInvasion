import pygame
from settings import Settings
from ship import Ship
import game_functions as gfnc
from pygame.sprite import Group
from alien import Alien
from game_stats import Game_Stats
from button import Button
from scoreboard import Scoreboard


def run_game():
	#Initializes game, creates screen obj, bullet group, aliens
	pygame.init() 
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_l, 
		settings.screen_w))
	pygame.display.set_caption('Trump Invasion')
	bullets = Group()
	aliens = Group()
 
	#Makes a ship
	ship = Ship(settings, screen)

	#Create game stats instance
	stats = Game_Stats(settings)

	#Creates fleet
	gfnc.create_fleet(settings, screen, aliens, ship)

	#Play button
	button = Button(settings, screen, "Play")

	#Scoreboard
	score = Scoreboard(screen, settings, stats)

	#Starts main loops
	while True:
	
		#Keyboard and mouse events
		gfnc.check_events(settings, screen, ship, bullets, stats, 
			button, aliens, score)
		
		if stats.game_status:
			ship.update()
		
			#Removes bullets off screen
			gfnc.update_bullets(bullets, aliens, settings, screen, ship,
				stats, score)   
	
			#Moves aliens
			gfnc.update_aliens(settings, aliens, ship, stats, screen, 
				bullets)
	
		#Updates the screen
		gfnc.update_screen(settings, screen, ship, bullets, aliens, 
			button, stats, score)
		
	
run_game()		
