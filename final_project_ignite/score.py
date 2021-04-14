import os
import math
import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, distance_from_start, number, final = None):
        super().__init__()
        if number == "score":
            image_location = os.path.join("assets", "numbers", "score.png")
            self.image = pygame.image.load(image_location).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = 550
            self.rect.y = -45
        elif final == True:
            image_location = os.path.join("assets", "numbers", str("number" + str(number) +".png"))
            self.image = pygame.image.load(image_location)
            self.image = pygame.transform.scale(self.image, (200,200))
            self.rect = self.image.get_rect()
            self.rect.x = 380 + (distance_from_start * 47)
            self.rect.y = 330
        else:
            image_location = os.path.join("assets", "numbers", str("number" + str(number) +".png"))
            self.image = pygame.image.load(image_location).convert_alpha() 
            self.rect = self.image.get_rect()
            self.rect.x = 670 + (distance_from_start * 31)
            self.rect.y = -45
