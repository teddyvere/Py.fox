import pygame
from . Config import FPS, WIDTH, HEIGHT, RED
from . Sprites import Player, Enemy, Laser

# Initialize Pygame
pygame.init()



# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("StarFox Clone")

# Load imagesGame\static\images\player_ship.png
player_img = pygame.image.load("Game\static\images\player_ship.png").convert_alpha()
enemy_img = pygame.image.load("Game\static\images\enemy_ship.png").convert_alpha()
background_img = pygame.image.load("Game\static\images\pixel_space.png").convert_alpha()



# Game initialization
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
lasers = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Spawn enemies
for i in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Background scrolling
background_y = 0
scroll_speed = 5

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # Check for collisions between lasers and enemies
    hits = pygame.sprite.groupcollide(enemies, lasers, True, True)
    for hit in hits:
        # Respawn a new enemy
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Background scrolling
    background_y += scroll_speed
    if background_y >= HEIGHT:
        background_y = 0

    # Draw everything
    screen.blit(background_img, (0, background_y - HEIGHT))
    screen.blit(background_img, (0, background_y))
    all_sprites.draw(screen)

    # Flip display
    pygame.display.flip()

pygame.quit()
