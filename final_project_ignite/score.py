import os
import math
import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, distance_from_start, number):
        super().__init__()
        if number == "score":
            image_location = os.path.join("assets", "numbers", "score.png")
            self.image = pygame.image.load(image_location).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = 550
            self.rect.y = -45
        else:
            image_location = os.path.join("assets", "numbers", str("number" + str(number) +".png"))
            self.image = pygame.image.load(image_location).convert_alpha() 
            self.rect = self.image.get_rect()
            self.rect.x = 670 + (distance_from_start * 31)
            self.rect.y = -45