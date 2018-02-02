import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self,ai_settings,screen):
		"""初始化飞船并放在屏幕底部中央"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载飞船图片并获得其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		#放置飞船
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#移动标志
		self.moving_right = False
		self.moving_left = False
		
		#在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)
		
	def update(self):
		"""根据移动标志调整位置"""
		#更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		#根据self.center更新rect对象	
		self.rect.centerx = self.center

	def blitme(self):
		"""将飞船移到准确的位置"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx
