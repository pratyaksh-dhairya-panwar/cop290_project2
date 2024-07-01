import os
import sys
import math
import random
import pygame
from scripts.Buttons import ScaledButton, Button
from scripts.Level import level, levels
import time


class Master:
    def __init__(self):
        pygame.mixer.init()
        self.sfx = {
            'ambience': pygame.mixer.Sound('data/music.wav')
        }
    def run(self):    
        pygame.mixer.music.load('data/music.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
        self.sfx['ambience'].play(-1)            
        clock = pygame.time.Clock()
        fps = 60

        screen_width = 1920
        screen_height = 1080

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('My Ninja')


        start_img = pygame.transform.scale(pygame.image.load('data/images/START.png'),(700,300))
        # exit_img = pygame.image.load('data/images/Quit.jpg')
        exit_img = pygame.transform.scale(pygame.image.load('data/images/Quit.png'),(700,300))

        start_button = ScaledButton(screen_width // 2 , screen_height // 2 -200, start_img)
        exit_button = ScaledButton(screen_width // 2, screen_height // 2  +200, exit_img)

        present="main_menu"
        run = True
        while run:
            clock.tick(fps)
            screen.fill((106, 96, 92))
            if present=="main_menu":
                if start_button.draw(screen):
                    present="level_selector"
                    time.sleep(0.2)
                if exit_button.draw(screen):
                    run = False
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False

            elif present=="level_selector":
                screen.fill((205, 247, 246))
                for level in levels:
                    level.draw(screen)
                    if level.check():
                        present="main_menu"
                        continue
                    # time.sleep(0.2)

                right_button = Button(screen.get_width()-100, screen.get_height()//2, pygame.transform.scale(pygame.image.load('data/images/arrow/right-arrow.png'), (50, 50))).draw(screen)
                left_button = Button(100, screen.get_height()//2, pygame.transform.scale(pygame.image.load('data/images/arrow/left-arrow.png'), (50, 50))).draw(screen)
                if left_button:
                    for i in levels:
                        i.state+=1
                        if i.state==len(levels)-1:
                            i.state=-1
                    time.sleep(0.2)
                if right_button:
                    for i in levels:
                        i.state-=1
                        if i.state==-2:
                            i.state=len(levels)-2
                    time.sleep(0.2)
                # print("working")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    # if event.type == pygame.KEYDOWN:
                    #     print("left")
                    #     if event.key == pygame.K_LEFT:
                    #         for i in levels:
                    #             i.state+=1
                    #             if i.state==len(levels)-1:
                    #                 i.state=-1
                    #         time.sleep(0.2)
                    #     if event.key == pygame.K_RIGHT:
                    #         print("right")
                    #         for i in levels:
                    #             i.state-=1
                    #             if i.state==-2:
                    #                 i.state=len(levels)-2
                    #         time.sleep(0.2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

Master().run()