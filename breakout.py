
import pygame
import random
pygame.init()
pygame.display.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (30, 144, 225)
COLOR_TRANSPARENT = (0, 0, 0, 0)

size_user = pygame.display.get_desktop_sizes()
size_x = size_user[0][0] * 0.3385
size_y = size_user[0][1] * 0.7222
screen_size = (size_x, size_y)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Breakout")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('000', True, COLOR_WHITE, COLOR_TRANSPARENT)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (50, 50)


# player lifes text
player_lifes_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
player_lifes_text = player_lifes_font.render('3', True, COLOR_WHITE, COLOR_TRANSPARENT)
player_lifes_rect = player_lifes_text.get_rect()
player_lifes_rect.midtop = (50, 50)

# player lifes
player_lifes = 3

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')

# creating player 1
player_1_size_y = 50
player_1_size_x = 20
player_1_y_spawn = screen_size[1] * 0.8974
player_1_x_spawn = screen_size[0] / 2 - (player_1_size_x / 2)
player_1_position = pygame.Rect(player_1_x_spawn, player_1_y_spawn, player_1_size_y, player_1_size_x)
player_1_waiting = pygame.Rect(0, 700, 1000, 20)
player_1_move_right = False
player_1_move_left = False
player_1_start_button = True


# creating obstacles

transparent_rectangle_obstacle = pygame.draw.rect(screen, COLOR_TRANSPARENT, (840, 1021, 55, 12))
retangle_position_x = screen_size[0] * 0.0723
retangle_position_y = screen_size[1] * 0.2179
retangle_size_x = screen_size[0] * 0.0615
retangle_size_y = screen_size[1] * 0.0141

red_obstacles = []
for n in range(2):
    for i in range(14):
        red_obstacle_rect = pygame.Rect(i*retangle_position_x, retangle_position_y + n * 20, retangle_size_x, retangle_size_y)
        red_obstacles.append(red_obstacle_rect)

orange_obstacles = []
for n in range(2, 4):
    for i in range(14):
        orange_obstacle_rect = pygame.Rect(i*retangle_position_x, retangle_position_y + n * 20, retangle_size_x, retangle_size_y)
        orange_obstacles.append(orange_obstacle_rect)

green_obstacles = []
for n in range(4, 6):
    for i in range(14):
        green_obstacle_rect = pygame.Rect(i*retangle_position_x, retangle_position_y + n * 20, retangle_size_x, retangle_size_y)
        green_obstacles.append(green_obstacle_rect)

yellow_obstacles = []
for n in range(6, 8):
    for i in range(14):
        yellow_obstacle_rect = pygame.Rect(i*retangle_position_x, retangle_position_y + n * 20, retangle_size_x, retangle_size_y)
        yellow_obstacles.append(yellow_obstacle_rect)

# creating ball
ball_x_size = screen_size[0] * 0.0153
ball_y_size = screen_size[1] * 0.0153
ball_x_spawn = (screen_size[0]/2) - ball_x_size
ball_y_spawn = (screen_size[1] * 0.4871) - ball_y_size
ball = pygame.Rect(ball_x_spawn, 380 - ball_y_size, ball_x_size, ball_y_size)
ball_random_x_list = [-5, 5]
ball_spawn = False
ball_dx = 5
ball_dy = 5
ball_random_x = random.choice(ball_random_x_list)

# score
score = 000
SCORE_MAX = 896

# game loop
game_loop = True
game_clock = pygame.time.Clock()

# waiting loop
waiting_loop = pygame.time.Clock()

# ball collision

ball_in_paddle_range_y = player_1_position.y + (player_1_size_y / 2) >= ball.y + ball_y_size >= player_1_position.y

while game_loop:
    while player_1_start_button:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_1_start_button = False
                game_loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_1_start_button = False
                    ball = pygame.Rect(ball_x_spawn, ball_y_spawn, 0, 0)
                    ball_dy = 5
                    ball_dx = ball_random_x
            # checking the victory condition in waiting
        if score < SCORE_MAX:

            # clear screen
            screen.fill(COLOR_BLACK)

            # ball collision with top in waiting

            if ball.top <= 0:
                ball_dy *= -1
                bounce_sound_effect.play()

            # ball collision with player in waiting

            if ball_in_paddle_range_y and player_1_waiting.x + 1000 >= ball.x >= player_1_waiting.x:
                ball.y = player_1_position.y - ball_y_size
                ball_dy *= -1
                bounce_sound_effect.play()

            # ball collision with the wall in waiting
            if ball.right >= screen_size[0]:
                ball_dx *= -1
                bounce_sound_effect.play()
            elif ball.left <= 0:
                ball_dx *= -1
                bounce_sound_effect.play()

            # ball movement in waiting
            ball.x += ball_dx
            ball.y += ball_dy

            # yellow obstacle collision in waiting
            collision_yellow = ball.collidelist(yellow_obstacles)
            if collision_yellow != -1:
                ball_dy *= -1
                bounce_sound_effect.play()

            # red obstacle collision in waiting
            collision_red = ball.collidelist(red_obstacles)
            if collision_red != -1:
                ball_dy *= -1
                bounce_sound_effect.play()

            # green obstacle collision in waiting
            collision_green = ball.collidelist(green_obstacles)
            if collision_green != -1:
                ball_dy *= -1
                bounce_sound_effect.play()

            # orange obstacle collision in waiting
            collision_orange = ball.collidelist(orange_obstacles)
            if collision_orange != -1:
                ball_dy *= -1
                bounce_sound_effect.play()

            # drawing obstacles in waiting
            for red_obstacle in red_obstacles:
                    pygame.draw.rect(screen, COLOR_RED, red_obstacle)
            for orange_obstacle in orange_obstacles:
                    pygame.draw.rect(screen, COLOR_ORANGE, orange_obstacle)
            for green_obstacle in green_obstacles:
                    pygame.draw.rect(screen, COLOR_GREEN, green_obstacle)
            for yellow_obstacle in yellow_obstacles:
                    pygame.draw.rect(screen, COLOR_YELLOW, yellow_obstacle)

            # drawing objects in waiting
            pygame.draw.rect(screen, COLOR_BLUE, player_1_waiting)
            pygame.draw.rect(screen, COLOR_WHITE, ball)
            screen.blit(score_text, score_text_rect)
        else:
            # drawing victory in waiting
            screen.fill(COLOR_BLACK)
            screen.blit(score_text, score_text_rect)

            # update screen
        pygame.display.flip()
        waiting_loop.tick(60)


    # game starts

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RCTRL:
                ball_spawn = True
                if ball_spawn:
                    ball = pygame.Rect(ball_x_spawn, ball_y_spawn, ball_x_size, ball_y_size)
                    pygame.draw.rect(screen, COLOR_WHITE, ball)

    # checking the victory condition
    if score < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with top and bottom
        # will be the scoring or losing conditions
        if ball.top >= screen_size[1]:
            ball = pygame.Rect(ball_x_spawn, ball_y_spawn, 0, 0)
            player_lifes -= 1
        if ball.top <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with player in game

        if ball_in_paddle_range_y and player_1_position.x + player_1_size_x >= ball.x + (ball_x_size / 2) >= player_1_position.x:
            ball.y = player_1_position.y - ball_y_size
            ball_dy *= -1
            bounce_sound_effect.play()

        # collision with the right side
        if ball_in_paddle_range_y and player_1_position.x + player_1_size_x >= ball.x + (ball_x_size / 2) >= player_1_position.x + (player_1_size_x / 2):
            ball.x = player_1_size_x + 1
            ball_dy *= -1
            ball_dx *= -1
            bounce_sound_effect.play()

        # collision with the left side
        if ball_in_paddle_range_y and player_1_position.x + (player_1_size_x / 2) >= ball.x + (ball_x_size / 2) >= player_1_position.x:
            ball.x = player_1_position.x - (ball_x_size + 1)
            ball_dy *= -1
            ball_dx *= -1
            bounce_sound_effect.play()

        # ball collision with the wall
        if ball.right >= screen_size[0]:
            ball_dx *= -1
            bounce_sound_effect.play()
        elif ball.left <= 0:
            ball_dx *= -1
            bounce_sound_effect.play()

        # ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # player 1 right movement
        if player_1_move_right:
            player_1_position.right += 7
        else:
            player_1_position.right -= 0

        # player 1  movement
        if player_1_move_left:
            player_1_position.left -= 7
        else:
            player_1_position.left += 0

        # player 1 collides with left wall
        if player_1_position.left <= 0:
            player_1_position.left = 0

        # player 1 collides with right wall
        elif player_1_position.right >= screen_size[0]:
            player_1_position.right = screen_size[0]

        # yellow obstacle collision
        collision_yellow = ball.collidelist(yellow_obstacles)
        if collision_yellow != -1:
            yellow_obstacles[collision_yellow] = transparent_rectangle_obstacle
            bounce_sound_effect.play()
            ball_dy *= -1
            score += 1

        # red obstacle collision
        collision_red = ball.collidelist(red_obstacles)
        if collision_red != -1:
            red_obstacles[collision_red] = transparent_rectangle_obstacle
            bounce_sound_effect.play()
            ball_dy *= -1
            score += 7

        # green obstacle collision
        collision_green = ball.collidelist(green_obstacles)
        if collision_green != -1:
            green_obstacles[collision_green] = transparent_rectangle_obstacle
            bounce_sound_effect.play()
            ball_dy *= -1
            score += 3

        # orange obstacle collision
        collision_orange = ball.collidelist(orange_obstacles)
        if collision_orange != -1:
            orange_obstacles[collision_orange] = transparent_rectangle_obstacle
            bounce_sound_effect.play()
            ball_dy *= -1
            score += 5

        # update score hud
        score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_TRANSPARENT)
        player_lifes_text = player_lifes_font.render(str(player_lifes), True, COLOR_WHITE, COLOR_TRANSPARENT)

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
        pygame.draw.rect(screen, COLOR_BLUE, player_1_position)
        pygame.draw.rect(screen, COLOR_WHITE, ball)
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
