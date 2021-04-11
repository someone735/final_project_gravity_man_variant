# Created by Schulich Ignite Flare and students of Schulich Ignite

import sys
import os
import pygame
from platform import Platform
from player import Player
from missile import Missile
from score import Score
import random

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()


# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Platforms sprite group
while True:
    platform_level = -2
    missile_level = 7.5
    platforms = pygame.sprite.Group()

    platforms.add(Platform(300, 600, 350, 50, platform_level))
    # platforms.add(Platform(700, 300, 400, 50, platform_level)) # upper middle benchmark 
    # platforms.add(Platform(700, 550, 400, 50, platform_level)) # lower middle benchmark
    # platforms.add(Platform(700, 250, 400, 50, platform_level))
    platforms.add(Platform(700, 200, 400, 50, platform_level))
    platforms.add(Platform(700, 150, 400, 50, platform_level))
    platforms.add(Platform(700, 100, 400, 50, platform_level))
    platforms.add(Platform(700, 50, 400, 50, platform_level))
    platforms.add(Platform(700, 600, 400, 50, platform_level))
    platforms.add(Platform(700, 650, 400, 50, platform_level))
    platforms.add(Platform(700, 700, 400, 50, platform_level))



    # Create the player sprite and add it to the players sprite group
    player = Player(400, 500)
    players = pygame.sprite.Group()
    players.add(player)


    platform_creation_time = 3000 
    platform_speed_time = platform_creation_time * 5
    creation_start_time = pygame.time.get_ticks()
    speed_start_time = pygame.time.get_ticks()
    increase_plat_speed = True
    decrease_plat_creation = True
    
    # Create missile sprite group and other variables related to missile sprite
    # (beginning firing time, firing time tracker (start and current), missile frequency time and time tracker)
    missiles = pygame.sprite.Group()
    missile_begin_firing_time = pygame.time.get_ticks()
    missile_firing_start_time = 10000
    missile_fire_time = 15000
    missile_begin_firing = False
    missile_begin_frequency_increase = False
    missile_frequency_increase_start_time = pygame.time.get_ticks()
    missile_frequency_increase_time = 25000
    
    # Defines death variable (triggers when to switch)
    death = False

    # Create background image and death message image
    background = pygame.image.load(os.path.join("assets", "background.jpg")).convert_alpha()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()
    death_message = pygame.image.load(os.path.join("assets", "death_message.png")).convert_alpha()
    death_message = pygame.transform.scale(death_message, (SCREEN_WIDTH, SCREEN_HEIGHT))

    controls = pygame.image.load(os.path.join("assets", "control_image.png")).convert_alpha()
    controls = pygame.transform.scale(controls, (500,400))
    screen_rect_controls = [50,0,550,450]
    controls_start_moving = 4000
    controls_start_moving_time = pygame.time.get_ticks()

    # Defines score variable and other variable related to score (score count, score time tracker (start), and print score (checks if score has been printed))
    score_uptick = 1000
    score_player_current = 0
    score_begin_count = pygame.time.get_ticks()
    score_sprite_group = pygame.sprite.Group()
    score_sprite_group.add(Score(0,"score"))
    score_sprite_group.add(Score(1,0))
    while True:
        """
        EVENTS section - how the code reacts when users do things
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                pygame.quit()
                sys.exit()
            
        # Keyboard events
        # flip gravity button
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            player.flip()
        # move left and right button
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            player.move(-player.move_speed, 0)
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            player.move(player.move_speed, 0)
        # jump button
        if keys_pressed[pygame.K_SPACE]:
            player.jump()
        # restart key
        if keys_pressed[pygame.K_r]:
            break

        """
        UPDATE section - manipulate everything on the screen
        """
        # updates all sprites in sprite groups 
        players.update()
        platforms.update()
        missiles.update()
        
        # moves tutorial image
        if controls_start_moving <= pygame.time.get_ticks() - controls_start_moving_time:
            screen_rect_controls[0] -= 1


        # if the player hasn't died 
        if death == False: 
            # Handle collisions with platforms
            hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
            for platform in hit_platforms:
                player.on_platform_collide(platform)

            if len(hit_platforms) <= 0:
                player.can_jump = False
                player.can_flip = False

            # Handle platform creation time
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

            # handles platform creation time increase and decrease in addition to platform speed
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
                    platform_level -= 0.070
                elif increase_plat_speed == False:
                    platform_level += 0.070
                if decrease_plat_creation == True:
                    platform_creation_time -= 300
                elif decrease_plat_creation == False:
                    platform_creation_time += 300

            # handles missile begin firing time 
            missile_begin_firing_current_time = pygame.time.get_ticks() - missile_begin_firing_time
            if missile_begin_firing_current_time >= missile_firing_start_time:
                missile_begin_firing = True
                missile_begin_frequency_increase = True

            # checks if it is time to begin spawning missiles 
            if missile_begin_firing == True:
                missile_firing_current_time = pygame.time.get_ticks() - missile_begin_firing_time       
                if missile_firing_current_time >= missile_fire_time:
                    missile_begin_firing_time = pygame.time.get_ticks()
                    missiles.add(Missile(SCREEN_WIDTH, player.rect.y-25, 75, 75, missile_level))
            
            # handles missile spawn rate
            if missile_begin_frequency_increase == True:
                missile_frequency_increase_current_time = pygame.time.get_ticks() - missile_frequency_increase_start_time
                if missile_frequency_increase_current_time >= missile_frequency_increase_time:
                    missile_frequency_increase_start_time = pygame.time.get_ticks()
                    missile_fire_time -= 1000
                    if missile_fire_time <= 1500:
                        missile_fire_time = 1500 
        
            # handles player and missile collisions
            player_hit_missiles = pygame.sprite.spritecollide(player, missiles, True)
            if len(player_hit_missiles) > 0:
                players = pygame.sprite.Group()
                platforms = pygame.sprite.Group()
                missiles = pygame.sprite.Group()
                death = True 
            
            # checks if player sprite goes past screen boundaries
            if player.rect.y < -50 or player.rect.y > SCREEN_HEIGHT or player.rect.x < -50 or player.rect.x > SCREEN_WIDTH:
                players = pygame.sprite.Group()
                platforms = pygame.sprite.Group()
                missiles = pygame.sprite.Group()
                death = True 

            # handles score updation
            score_current_time = pygame.time.get_ticks() - score_begin_count
            if score_current_time >= score_uptick:
                score_begin_count = pygame.time.get_ticks()
                score_player_current += 1
                score_player_current_string = str(score_player_current)
                score_sprite_group = pygame.sprite.Group()
                score_sprite_group.add(Score(0,"score"))
                place_value = 1
                for x in score_player_current_string:
                    if x == "0":
                        score_sprite_group.add(Score(place_value,0))
                    elif x == "1":
                        score_sprite_group.add(Score(place_value,1))
                    elif x == "2":
                        score_sprite_group.add(Score(place_value,2))
                    elif x == "3":
                        score_sprite_group.add(Score(place_value,3))
                    elif x == "4":
                        score_sprite_group.add(Score(place_value,4))
                    elif x == "5":
                        score_sprite_group.add(Score(place_value,5))
                    elif x == "6":
                        score_sprite_group.add(Score(place_value,6))
                    elif x == "7":
                        score_sprite_group.add(Score(place_value,7))
                    elif x == "8":
                        score_sprite_group.add(Score(place_value,8))
                    elif x == "9":
                        score_sprite_group.add(Score(place_value,9))
                    else:
                        pass
                    place_value += 1
        
            


        """
        DRAW section - make everything show up on screen
        """
        screen.fill(BLACK)  # Fill the screen with one colour
        
        # draws background, platforms, player, missiles and death message if needed
        screen.blit(background, screen_rect)
        score_sprite_group.draw(screen)
        platforms.draw(screen)
        players.draw(screen)
        missiles.draw(screen)
        screen.blit(controls, screen_rect_controls)
        # if player is died
        if death == True:
            screen.blit(death_message, screen_rect)
        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
        