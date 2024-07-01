import pygame

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, screen):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		screen.blit(self.image, self.rect)

		return action
      
class ScaledButton():
    def __init__(self, x, y, image, scale_factor=1):
        self.image_normal = image
        self.scalefactor = scale_factor
        self.image_hover = pygame.transform.scale(image, (int(image.get_width() * self.scalefactor), int(image.get_height() * self.scalefactor)))
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.center = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.image = self.image_hover
            if self.scalefactor <=1.1:
                self.scalefactor += 0.01
                self.image_hover = pygame.transform.scale(self.image_normal, (int(self.image_normal.get_width() * self.scalefactor), int(self.image_normal.get_height() * self.scalefactor)))
                self.rect = self.image_hover.get_rect()
                self.rect.center = self.center
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        else:
            self.image = self.image_hover
            if self.scalefactor >=1:
                self.scalefactor -= 0.02
                self.image_hover = pygame.transform.scale(self.image_normal, (int(self.image_normal.get_width() * self.scalefactor), int(self.image_normal.get_height() * self.scalefactor)))
                self.rect = self.image_hover.get_rect()
                self.rect.center = self.center

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        screen.blit(self.image, self.rect)

        return action
   