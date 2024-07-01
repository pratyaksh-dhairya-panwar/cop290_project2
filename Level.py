import pygame
from scripts.Buttons import ScaledButton, Button
from scripts.game import Game
import os
import time


class level:
    def __init__(self,state,image):
        self.state = state
        self.image = image
        self.rect = self.image.get_rect()
        self.clicked = False
        self.level_no = state
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False
    def draw(self, screen):
        if self.state == 0:
            self.image = pygame.transform.scale(self.image, (500, 300))
            screen_width, screen_height = screen.get_size()
            image_width, image_height = self.image.get_size()
            position = ((screen_width - image_width) // 2, (screen_height - image_height) // 2)
            screen.blit(self.image, position)
            self.rect.topleft = position
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if action:
                if(self.level_no>=0 and self.level_no<len(maps_list)):
                    Game(self.level_no).run()
            return action
           

        if self.state == 1:
            self.image = pygame.transform.scale(self.image, (400, 250))
            screen_width, screen_height = screen.get_size()
            image_width, image_height = self.image.get_size()
            position = ((screen_width - 600), (screen_height - image_height) // 2)
            screen.blit(self.image, position)
            # time.sleep(0.2)
            self.rect.topleft = position
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if action:
                if(self.level_no>=0 and self.level_no<len(maps_list)):
                    Game(self.level_no).run()
            return action
        if self.state == -1:
            self.image = pygame.transform.scale(self.image, (400, 250))
            screen_width, screen_height = screen.get_size()
            image_width, image_height = self.image.get_size()
            position = (200, (screen_height - image_height) // 2)
            screen.blit(self.image, position)
            self.rect.topleft = position
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            if action:
                if(self.level_no>=0 and self.level_no<len(maps_list)):
                    Game(self.level_no).run()
            return action

    def clicked(self,screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


		#draw button
        screen.blit(self.image, self.rect)

        return action


def get_files_in_directory(directory):
    return sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

def load_and_scale_image(path, size=(300, 200)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

# usage
image_files = get_files_in_directory('data/images/Levels/')
maps_list = get_files_in_directory('data/maps/')
images = [load_and_scale_image(os.path.join('data/images/Levels/', f)) for f in image_files]

levels = [level(i%len(images)-1, img) for i, img in enumerate(images)]