import sys
import pygame

def run_game():
	"""初始化并设置屏幕"""
	pygame.init()
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption('This is work 12-4')
	bg_colour = (255,255,255)
	
	#主循环
	while True:
		#时间循环
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					bg_colour = (0,0,0)
				elif event.key == pygame.K_DOWN:
					bg_colour = (0,0,255)
				elif event.key == pygame.K_RIGHT:
					bg_colour = (0,255,0)
				elif event.key == pygame.K_LEFT:
					bg_colour = (255,0,0)
		#重新上色
		screen.fill(bg_colour)		
		#刷新屏幕
		pygame.display.flip()
		
run_game()
