import os
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "player.png")
        self.walking_right_image = pygame.image.load(image_location).convert_alpha()
        self.walking_left_image = pygame.transform.flip(self.walking_right_image, True, False)
        self.walking_left_rightside_up = pygame.transform.flip(self.walking_left_image, False, True)
        self.walking_right_rightside_up = pygame.transform.flip(self.walking_right_image, False, True)
        self.image = self.walking_right_image
        self.rect = self.image.get_rect()
        self.left = False

        self.rect.x = x
        self.rect.y = y

        self.move_speed = 6
        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0.6
        self.jump_speed = 17.5
        
        self.can_flip = True
        self.can_jump = True
        self.rightside_up = True
 
    def update(self):
        # Move the player based on whatever the x_speed and y_speed are
        self.move(self.x_speed, self.y_speed)
        # Make the player fall due to gravity
        self.fall()
        if self.rightside_up == False:
            if self.left == True:
                self.image = self.walking_left_rightside_up
            else:
                self.image = self.walking_right_rightside_up
        elif self.rightside_up == True:
            if self.left == True:
                self.image = self.walking_left_image
            else:
                self.image = self.walking_right_image

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change 
        
        if x_change > 0:
            self.image = self.walking_right_image
            self.left = False
        elif x_change < 0:
            self.image = self.walking_left_image
            self.left = True

    def fall(self):
        self.y_speed += self.gravity

    def flip(self):
        if not self.can_flip:
            return
        
        if self.rect.y >= 450:
            self.gravity = -0.6
            self.y_speed = 0
            self.rightside_up = False
        elif self.rect.y < 450:
            self.gravity = 0.6
            self.y_speed = 0
            self.rightside_up = True
    
    def jump(self):
        if not self.can_jump:
            return
        if self.rect.y >= 450:
            self.y_speed = -1 * self.jump_speed
        elif self.rect.y < 450:
            self.y_speed = self.jump_speed
        
        

    def on_platform_collide(self, platform):
        # Need to set self.rect.y explicitly to avoid having the player clip through the floor
        # Note a new bug surfaces - players jumping from the underside will teleport to the top. This is left for students to solve if interested
        if self.rect.y <= 350:
            self.rect.y = platform.rect.y + self.rect.height-14
        else:
            self.rect.y = platform.rect.y - self.rect.height
        
        self.y_speed = 0
        self.can_flip = True
        self.can_jump = True