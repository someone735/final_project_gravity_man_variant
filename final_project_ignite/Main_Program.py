# Created by Schulich Ignite Flare and students of Schulich Ignite

import sys
import os
import pygame
from platform import Platform
from player import Player
from missile import Missile
from death_message import Death_message
import random

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

bg = pygame.image.load(os.path.join("assets","bg.png"))
# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60
platform_level = -2
missile_level = 7
# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# screen.blit(bg, bg.get_rect())
# Platforms sprite group
platforms = pygame.sprite.Group()

platforms.add(Platform(300, 600, 350, 50, platform_level))
# platforms.add(Platform(100, 500, 200, 50))
platforms.add(Platform(700, 300, 250, 50, platform_level)) # upper middle benchmark 
platforms.add(Platform(700, 550, 250, 50, platform_level)) # lower middle benchmark
platforms.add(Platform(700, 250, 250, 50, platform_level))
platforms.add(Platform(700, 200, 250, 50, platform_level))
platforms.add(Platform(700, 150, 250, 50, platform_level))
platforms.add(Platform(700, 100, 250, 50, platform_level))
platforms.add(Platform(700, 50, 250, 50, platform_level))
platforms.add(Platform(700, 600, 250, 50, platform_level))
platforms.add(Platform(700, 650, 250, 50, platform_level))
platforms.add(Platform(700, 700, 250, 50, platform_level))



# Create the player sprite and add it to the players sprite group
player = Player(400, 500)
players = pygame.sprite.Group()
players.add(player)

missiles = pygame.sprite.Group()
death_messages = pygame.sprite.Group()

platform_creation_time = 3000 
platform_speed_time = platform_creation_time * 5
creation_start_time = pygame.time.get_ticks()
speed_start_time = pygame.time.get_ticks()
increase_plat_speed = True
decrease_plat_creation = True

missile_firing_start_time = 7500
missile_fire_time = 5000

death = False
while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        
    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.flip()
        
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.move(-player.move_speed, 0)
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.move(player.move_speed, 0)
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        pass  # Now that we have platforms, there's no reason to make the player move down.
    if keys_pressed[pygame.K_SPACE]:
        player.jump()
    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        pass
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line

    """
    UPDATE section - manipulate everything on the screen
    """
    
    players.update()
    platforms.update()
    missiles.update()
    death_messages.update()


    # Handle collisions with platforms
    if death == False:
        hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
        for platform in hit_platforms:
            player.on_platform_collide(platform)

        if len(hit_platforms) <= 0:
            player.can_jump = False
            player.can_flip = False
        creation_current_time = pygame.time.get_ticks() - creation_start_time
        if creation_current_time >= platform_creation_time:
            creation_start_time = pygame.time.get_ticks()
            random_platform_height = random.randint(1,10)
            if random_platform_height == 1:
                platforms.add(Platform(1000, 50, 350, 50, platform_level))
            elif random_platform_height == 2:
                platforms.add(Platform(1000, 100, 350, 50, platform_level))
            elif random_platform_height == 3:
                platforms.add(Platform(1000, 150, 350, 50, platform_level))
            elif random_platform_height == 4:
                platforms.add(Platform(1000, 200, 350, 50, platform_level))
            elif random_platform_height == 5:
                platforms.add(Platform(1000, 250, 350, 50, platform_level))
            elif random_platform_height == 6:
                platforms.add(Platform(1000, 300, 350, 50, platform_level))
            elif random_platform_height == 7:
                platforms.add(Platform(1000, 550, 350, 50, platform_level))
            elif random_platform_height == 8:
                platforms.add(Platform(1000, 600, 350, 50, platform_level))
            elif random_platform_height == 9:
                platforms.add(Platform(1000, 650, 350, 50, platform_level))
            elif random_platform_height == 10:
                platforms.add(Platform(1000, 700, 350, 50, platform_level))

        speed_current_time = pygame.time.get_ticks() - speed_start_time
        if speed_current_time >= platform_speed_time:
            speed_start_time = pygame.time.get_ticks()
            if platform_creation_time > 3000:
                decrease_plat_creation = True
                if platform_level < -3:
                    increase_plat_speed = False
            elif platform_creation_time < 1800:
                decrease_plat_creation = False
                if platform_level > -2:
                    increase_plat_speed = True
            
            if increase_plat_speed == True:
                platform_level -= 0.075
            elif increase_plat_speed == False:
                platform_level += 0.075
            if decrease_plat_creation == True:
                platform_creation_time -= 275
            elif decrease_plat_creation == False:
                platform_creation_time += 275

            # print(platform_level)
            # print(platform_creation_time)
        missile_begin_firing_current_time = pygame.time.get_ticks()
        if missile_begin_firing_current_time >= missile_firing_start_time:
            if missile_begin_firing_current_time >= missile_firing_start_time and missile_begin_firing_current_time <= missile_firing_start_time + 100:
                print("firing")
            missile_firing_current_time = pygame.time.get_ticks() - missile_fire_time
            if missile_firing_current_time >= missile_fire_time:
                missile_fire_time = pygame.time.get_ticks()
                print("missile fired")
                missiles.add(Missile(1000, player.rect.y-25, 125, 100, missile_level))
                
        player_hit_missiles = pygame.sprite.spritecollide(player, missiles, True)
        if len(player_hit_missiles) > 0:
            players = pygame.sprite.Group()
            platforms = pygame.sprite.Group()
            missiles = pygame.sprite.Group()
            death = True 
        
    if death == True:
        death_messages.add(Death_message(int(SCREEN_WIDTH/4), int(SCREEN_HEIGHT/4), int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/7*3)))
     
    
        


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    
    # gameDisplay.blit(bg, (0, 0))
    platforms.draw(screen)
    players.draw(screen)
    missiles.draw(screen)
    death_messages.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    