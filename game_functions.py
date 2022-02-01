import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown(event, settings, screen, ship, bullets, stats, 
	aliens, score):
	"""Responds to key presses"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		if not stats.game_status:
			start_game(stats, aliens, bullets, settings, screen, ship,
				score)
	
def check_keyup(event, ship):
	"""Responds to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(settings, screen, ship, bullets, stats, button, aliens,
		score):
	"""Responds to keys and mouse clicks"""
	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, settings, screen, ship, bullets, 
				stats, aliens, score)
		elif event.type == pygame.KEYUP:
			check_keyup(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, button, mouse_x, mouse_y, aliens,
				bullets, settings, screen, ship, score)
			
def check_play_button(stats, button, mouse_x, mouse_y, aliens, bullets, 
	settings, screen, ship, score):
	"""Behavior for play button when clicked"""
	button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_status:
		start_game(stats, aliens, bullets, settings, screen, ship,
			score)
		
def start_game(stats, aliens, bullets, settings, screen, ship, score):
	"""Actions which restarts the game"""
	stats.game_status = True
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	settings.init_dynamic_settings()
	score.score_prep()
	score.prep_high_score()
	score.prep_level()
	aliens.empty()
	bullets.empty()
	create_fleet(settings, screen, aliens, ship)
	ship.center_ship()

def fire_bullets(settings, screen, ship, bullets):
	"""Fires bullets under limit"""
	if len(bullets) < settings.bullets_max:
			new_bullet = Bullet(settings, screen, ship)
			bullets.add(new_bullet)

def update_bullets(bullets, aliens, settings, screen, ship, stats,
		score):
	"""Updates position of bullets, get rid of old ones"""
	if stats.game_status:
		bullets.update()
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		bullet_alien_collision(settings, screen, aliens, ship, bullets,
			stats, score)
				
def bullet_alien_collision(settings, screen, aliens, ship, bullets,
		stats, score):
	"""Responds to bullet and 'alien' collisions'"""
	collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collision:
		for alien in collision.values():
			stats.score += settings.alien_points * len(alien)
			score.score_prep()
		check_high_score(stats, score)

	if len(aliens) == 0:
		bullets.empty()
		settings.increase_speed()
		stats.level += 1
		score.prep_level()
		create_fleet(settings, screen, aliens, ship)

def update_screen(settings, screen, ship, bullets, alien, button, stats,
		score):
	"""Updates images on screen, flips to newest screen"""
	screen.fill(settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.draw(screen)
	score.draw_score()
	if not stats.game_status:
		button.draw_button()
	pygame.display.flip()
	
def create_fleet(settings, screen, aliens, ship):
	"""Creates first row of aliens"""
	alien = Alien(settings, screen)
	num_aliens = get_alien_num(settings, alien.rect.width)
	num_rows = get_row_num(settings, ship.rect.height, 
		alien.rect.height)

	for row_num in range(num_rows):
		for num in range(num_aliens):
			create_aliens(settings, screen, aliens, num, row_num)

def get_alien_num(settings, alien_w):
	"""Gets the number og aliens in a row"""
	available_space = settings.screen_l - 2 * alien_w
	num_aliens = int(available_space / (2 * alien_w))
	return num_aliens
	
def create_aliens(settings, screen, aliens, num, row_num):
	"""Creates an alien, sets position"""
	alien = Alien(settings, screen)
	alien_w = alien.rect.width
	alien.x = alien_w + (2 * num * alien_w)
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + (2 * row_num * alien.rect.height)
	alien.add(aliens)
	
def get_row_num(settings, ship_h, alien_h):
	"""Get number of rows of aliens"""
	available_space = settings.screen_w - (3 * alien_h) - alien_h
	num_rows = int((available_space / (alien_h * 2)))
	return num_rows

def update_aliens(settings, aliens, ship, stats, screen, bullets):
	"""Updates aliens position"""
	check_fleet_edges(settings, aliens)
	aliens.update()
	
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, stats, screen, ship, aliens, bullets)
	check_aliens_bottom_hit(settings, stats, screen, ship, aliens, bullets)
		
		
def ship_hit(settings, stats, screen, ship, aliens, bullets):
	"""Behavior when ship hit by alien"""
	if stats.num_lives > 0:
		stats.num_lives -= 1
		aliens.empty()
		bullets.empty()
		create_fleet(settings, screen, aliens, ship)
		ship.center_ship()
		sleep(1)
	else:
		stats.game_status = False
		pygame.mouse.set_visible(True)
		
def check_aliens_bottom_hit(settings, stats, screen, ship, aliens, bullets):
	"""Checks if aliens hit bottom of screen"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(settings, stats, screen, ship, aliens, bullets)
			break
	
def check_fleet_edges(settings, aliens):
	"""Behavior for the aliens' motions"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break
			
def change_fleet_direction(settings, aliens):
	"""Changes aliens' directions and drops down"""
	for alien in aliens.sprites():
		alien.rect.y += settings.drop_speed
	settings.direction *= -1
	
def check_high_score(stats, score):
	"""Checks and uodates the high score"""
	if stats.high_score < stats.score:
		stats.high_score = stats.score
		score.prep_high_score()
