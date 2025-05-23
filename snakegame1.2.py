import pygame
import time
import random

# Initialize the game
pygame.init()

# Game variables
window_x = 1080  # Artırılmış boyut
window_y = 780  # Artırılmış boyut

# Create the display window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game")

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)       # Yılanın rengi
yellow = pygame.Color(255, 255, 0)  # Meyvenin rengi

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Snake default position
snake_position = [100, 50]

# First 2 blocks of snake's body (kısaltılmış)
snake_body = [[100, 50], [90, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# Setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Game Over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        f'Your Score is: {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    time.sleep(1)  # Wait a moment before showing continue prompt

    continue_font = pygame.font.SysFont('times new roman', 30)
    continue_surface = continue_font.render(
        'Press C to Continue or Q to Quit', True, white)
    continue_rect = continue_surface.get_rect()
    continue_rect.midtop = (window_x / 2, window_y / 2)
    game_window.blit(continue_surface, continue_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    main()

# Displaying Score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x / 10, 15)
    else:
        score_rect.midtop = (window_x / 2, window_y / 1.25)
    game_window.blit(score_surface, score_rect)

def main():
    global direction, change_to, score, snake_position, snake_body, fruit_position, fruit_spawn

    # Reset the game state
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50]]
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                      random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Ekranı kapatma olayı
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake crossing boundaries
        if snake_position[0] < 0:
            snake_position[0] = window_x - 10
        if snake_position[0] > window_x - 10:
            snake_position[0] = 0
        if snake_position[1] < 0:
            snake_position[1] = window_y - 10
        if snake_position[1] > window_y - 10:
            snake_position[1] = 0

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                              random.randrange(1, (window_y//10)) * 10]
        fruit_spawn = True

        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, red, pygame.Rect(
                pos[0], pos[1], 10, 10))  # Yılanın rengi kırmızı

        pygame.draw.rect(game_window, yellow, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))  # Meyvenin rengi sarı

        # Game Over conditions
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)

        pygame.display.update()

        fps.tick(30)  

# Start the game
main()




