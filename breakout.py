
import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (30, 144, 225)
COLOR_TRANSPARENT = (0, 0, 0, 0)

# 14 por 8 paddles

screen_width = 840
screen_height = 1000
size = (840, 1020)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00000', True, COLOR_WHITE, COLOR_TRANSPARENT)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (50, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')

# creating player 1
player_1 = pygame.Rect(370, 920, 50, 20)
player_1_waiting = pygame.Rect(370, 920, 1000, 20)
player_1_move_right = False
player_1_move_left = False

# creating obstacles

transparent_rectangle = pygame.draw.rect(screen,COLOR_TRANSPARENT, (840, 1021, 55, 12))

red_obstacles = []
for n in range(2):
    for i in range(14):
        red_obstacle_rect = pygame.Rect(i*61, 210 + n * 20, 55, 12)
        red_obstacles.append(red_obstacle_rect)

orange_obstacles = []
for n in range(2, 4):
    for i in range(14):
        orange_obstacle_rect = pygame.Rect(i*61, 210 + n * 20, 55, 12)
        orange_obstacles.append(orange_obstacle_rect)

green_obstacles = []
for n in range(4, 6):
    for i in range(14):
        green_obstacle_rect = pygame.Rect(i*61, 210 + n * 20, 55, 12)
        green_obstacles.append(green_obstacle_rect)

yellow_obstacles = []
for n in range(6, 8):
    for i in range(14):
        yellow_obstacle_rect = pygame.Rect(i*61, 210 + n * 20, 55, 12)
        yellow_obstacles.append(yellow_obstacle_rect)

# creating ball
ball = pygame.Rect(470, 500, 10, 10)
ball_dx = 5
ball_dy = 5

# score
score_1 = 000
SCORE_MAX = 896

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_1_move_right = True
            if event.key == pygame.K_LEFT:
                player_1_move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_1_move_right = False
            if event.key == pygame.K_LEFT:
                player_1_move_left = False

    # checking the victory condition
    if score_1 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with top and bottom
        # will be the scoring or losing conditions
        if ball.top >= 1020:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball.bottom <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with player in game

        if player_1.y + 10 >= ball.y + 10 > player_1.y and player_1.x + 50 >= ball.x + 5 >= player_1.x:
            ball.y = player_1.y - 11
            ball_dy *= -1
            bounce_sound_effect.play()
        # collision with the right side
        if player_1.y + 20 >= ball.y + 10 > player_1.y and player_1.x + 50 >= ball.x + 5 >= player_1.x + 25:
            ball.x = player_1.x + 51
            ball_dy *= -1
            ball_dx *= -1
            bounce_sound_effect.play()
        # collision with the left side
        if player_1.y + 20 >= ball.y + 10 > player_1.y and player_1.x + 25 >= ball.x + 5 >= player_1.x:
            ball.x = player_1.x - 1
            ball_dy *= -1
            ball_dx *= -1
            bounce_sound_effect.play()

        # ball collision with the wall
        if ball.right > 840:
            ball_dx *= -1
            bounce_sound_effect.play()
        elif ball.left <= 10:
            ball_dx *= -1
            bounce_sound_effect.play()

        # ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # player 1 right movement
        if player_1_move_right:
            player_1.right += 5
        else:
            player_1.right -= 0

        # player 1  movement
        if player_1_move_left:
            player_1.left -= 5
        else:
            player_1.left += 0

        # player 1 collides with left wall
        if player_1.left <= 0:
            player_1.left = 0

        # player 1 collides with right wall
        elif player_1.right >= 840:
            player_1.right = 840

        # yellow obstacle collision
        collision_yellow = ball.collidelist(yellow_obstacles)
        if collision_yellow != -1:
            yellow_obstacles[collision_yellow] = transparent_rectangle
            bounce_sound_effect.play()
            ball_dx *= -1
            ball_dy *= -1

        # red obstacle collision
        collision_red = ball.collidelist(red_obstacles)
        if collision_red != -1:
            red_obstacles[collision_red] = transparent_rectangle
            bounce_sound_effect.play()
            ball_dx *= -1
            ball_dy *= -1

        # green obstacle collision
        collision_green = ball.collidelist(green_obstacles)
        if collision_green != -1:
            green_obstacles[collision_green] = transparent_rectangle
            bounce_sound_effect.play()
            ball_dx *= -1
            ball_dy *= -1

        # orange obstacle collision
        collision_orange = ball.collidelist(orange_obstacles)
        if collision_orange != -1:
            orange_obstacles[collision_orange] = transparent_rectangle
            bounce_sound_effect.play()
            ball_dx *= -1
            ball_dy *= -1

        # update score hud
        score_text = score_font.render(str(score_1), True, COLOR_WHITE, COLOR_TRANSPARENT)

        # drawing obstacles
        for red_obstacle in red_obstacles:
            pygame.draw.rect(screen, COLOR_RED, red_obstacle)
        for orange_obstacle in orange_obstacles:
            pygame.draw.rect(screen, COLOR_ORANGE, orange_obstacle)
        for green_obstacle in green_obstacles:
            pygame.draw.rect(screen, COLOR_GREEN, green_obstacle)
        for yellow_obstacle in yellow_obstacles:
            pygame.draw.rect(screen, COLOR_YELLOW, yellow_obstacle)

        # drawing objects
        pygame.draw.rect(screen, COLOR_BLUE, player_1)
        pygame.draw.rect(screen, COLOR_WHITE, ball)
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
