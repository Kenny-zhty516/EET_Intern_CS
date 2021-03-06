import sys
import pygame
from bullet import Bullet

# def update_screen(ai_settings, screen, ship):
#     """Update images on the screen and flip to the new screen."""
#     # Redraw the screen during each pass through the loop.
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#     # Make the most recently drawn screen visible.
#     pygame.display.flip()
    
def update(self):
    """Update the ship's position based on movement flags."""
 # Update the ship's center value, not the rect.
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.center += self.ai_settings.ship_speed_factor
    if self.moving_left and self.rect.left > 0:
        self.center -= self.ai_settings.ship_speed_factor

 # Update rect object from self.center.
    self.rect.centerx = self.center
    
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True    
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
           bullets.remove(bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    
    
    pygame.display.flip()
        


# def check_events(event, ship):
#     """Respond to keypresses and mouse events."""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
            
#         elif event.type == pygame.KEYDOWN:
#             def check_keydown_events(event, ship):
#                 """Respond to keypresses."""
#                 if event.key == pygame.K_RIGHT:
#                     # Move the ship to the right.
#                     ship.moving_right = True  
#                 elif event.key == pygame.K_LEFT:
#                     # Move the ship to the left.
#                     ship.moving_left = True  
            
#             def check_keyup_events(event, ship):
#                 """Respond to key releases."""      
#                 if event.key == pygame.K_RIGHT:
#                     ship.moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     ship.moving_left = False
                
        #         elif event.type == pygame.KEYUP:
        #             if event.key == pygame.K_RIGHT:
        #                 ship.moving_right = False
                      
        #         elif event.key == pygame.K_LEFT:
        #             # Move the ship to the left.
        #             ship.moving_left = True
           
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         ship.moving_right = False
        #     elif event.key == pygame.K_LEFT:
        #         ship.moving_left = False\
            
        

            
    