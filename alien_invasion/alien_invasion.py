import pygame

from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	"""Initialize the game and create a screen"""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((
		ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建Play按键
	play_button = Button(ai_settings,screen,'Play')
	
	#创建一艘飞船，一个子弹编组和一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	"""The main loop of the game"""
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
			aliens,bullets)
		
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,
				aliens,bullets)
			gf.update_aliens(ai_settings,stats,sb,screen,
				ship,aliens,bullets)
			
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
			play_button)
		
run_game()
			
		
