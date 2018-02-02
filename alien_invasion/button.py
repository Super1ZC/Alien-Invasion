import pygame.font

class Button():
	
	def __init__(self,ai_settings,screen,msg):
		"""初始化按钮的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#设置按钮的尺寸和其他属性(文本)
		self.width,self.height = 200,50
		self.button_colour = (0,255,0)
		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont(None,48)
		
		#创建rect的对象，并使其剧中
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center
		
		#按钮的标签只需要创建一次
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		"""将msg渲染成图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg,True,self.text_colour,
										  self.button_colour)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		"""绘制一个用颜色填充的按钮，再绘制文本"""
		self.screen.fill(self.button_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
