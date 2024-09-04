import pygame   
import random

# Initialize Pygame
pygame.init()

# Constants
WIN_WIDTH = 800
WIN_HEIGHT = 400
GROUND_HEIGHT = 300
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50 
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 40
JUMP_STRENGTH = 12
GRAVITY = 0.5
FPS = 90

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TREE_GREEN = (34, 139, 34)  # Warna hijau pokok

# Setup display
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Load assets
player_image = pygame.Surface(( PLAYER_WIDTH, PLAYER_HEIGHT))
player_image.fill(BLACK)
obstacle_image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle_image.fill(TREE_GREEN)  # Tukar warna hijau kepada hijau pokok

# Game variables
player_x = 50
player_y = GROUND_HEIGHT - PLAYER_HEIGHT
player_y_velocity = 0
is_jumping = False

obstacle_x = WIN_WIDTH
obstacle_y = GROUND_HEIGHT - OBSTACLE_HEIGHT

clock = pygame.time.Clock()

def draw_window():
    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(win, TREE_GREEN, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))  # Tukar warna hijau kepada hijau pokok
    
    # Draw the black line under the ground
    pygame.draw.line(win, BLACK, (0, GROUND_HEIGHT), (WIN_WIDTH, GROUND_HEIGHT), 5)
    
    pygame.display.update()

def main():
    global player_y, player_y_velocity, is_jumping, obstacle_x
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        # Player jump logic
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            player_y_velocity = -JUMP_STRENGTH
        
        if is_jumping:
            player_y += player_y_velocity
            player_y_velocity += GRAVITY
            if player_y >= GROUND_HEIGHT - PLAYER_HEIGHT:
                player_y = GROUND_HEIGHT - PLAYER_HEIGHT
                is_jumping = False
        
        # Move obstacle
        obstacle_x -= 5
        if obstacle_x < -OBSTACLE_WIDTH:
            obstacle_x = WIN_WIDTH

        # Check collision
        if (player_x + PLAYER_WIDTH > obstacle_x and
            player_x < obstacle_x + OBSTACLE_WIDTH and
            player_y + PLAYER_HEIGHT > obstacle_y):
            print("Game Over")
            run = False
        
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()