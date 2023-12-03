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
screen_size_x = screen_size[0]
screen_size_y = screen_size[1]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Breakout")

# score text
score_size = screen_size_x * 0.0769
score_font = pygame.font.Font('assets/PressStart2P.ttf', int(score_size))
score_text = score_font.render('0', True, COLOR_WHITE, COLOR_TRANSPARENT)
score_text_rect = score_text.get_rect()
score_text_x = screen_size_x * 0.0769
score_text_y = screen_size_y * 0.0641
score_text_rect.topleft = (score_text_x, score_text_y)


# player lifes text
player_lifes_size = screen_size_x * 0.0769
player_lifes_font = pygame.font.Font('assets/PressStart2P.ttf', int(player_lifes_size))
player_lifes_text = player_lifes_font.render('3', True, COLOR_WHITE, COLOR_TRANSPARENT)
player_lifes_rect = player_lifes_text.get_rect()
player_lifes_text_x = screen_size_x * 0.9076
player_lifes_text_y = screen_size_y * 0.0641
player_lifes_rect.topright = (player_lifes_text_x, player_lifes_text_y)

# player lifes
player_lifes = 3

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')

# creating player 1
player_speed = screen_size_x * 0.010
player_1_size_y = screen_size_y * 0.0256
player_1_size_x = screen_size_x * 0.0769
player_1_y_spawn = screen_size_y * 0.8974
player_1_x_spawn = screen_size_x / 2 - (player_1_size_x / 2)
player_1_position_and_design = pygame.Rect(player_1_x_spawn, player_1_y_spawn, player_1_size_x, player_1_size_y)
player_1_waiting = pygame.Rect(0, player_1_y_spawn, 1000, 20)
player_1_move_right = False
player_1_move_left = False
<<<<<<< HEAD
waiting_for_start = True
=======
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
>>>>>>> ae4db026873a4227b24a5ccf7b3ce1907e3722a3

# creating ball
ball_x_size = screen_size_x * 0.0153
ball_y_size = screen_size_y * 0.0153
ball_x_spawn = (screen_size_x/2) - ball_x_size
ball_y_spawn = (screen_size_y * 0.4871) + ball_y_size
ball_x_speed = screen_size_x * 0.0069
ball_y_speed = screen_size_y * 0.0069
ball = pygame.Rect(ball_x_spawn, ball_y_spawn, ball_x_size, ball_y_size)
ball_random_x_list = [-ball_x_speed, ball_x_speed]
ball_spawn = False
ball_dx = ball_x_speed
ball_dy = ball_y_speed


# score
score = 000
SCORE_MAX = 896

# game restart
game_restart = True

# game loop
game_loop = True
game_clock = pygame.time.Clock()

# waiting loop
waiting_loop = pygame.time.Clock()

# creating obstacles

transparent_rectangle_obstacle = pygame.draw.rect(screen, COLOR_TRANSPARENT, (0, 0, 0, 0))
retangle_position_x = screen_size_x * 0.0723
retangle_position_y = screen_size_y * 0.2179
retangle_size_x = screen_size_x * 0.0615
retangle_size_y = screen_size_y * 0.0141

while game_restart:
    game_restart = False
    game_loop = True
    player_design = player_1_position_and_design

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

    while game_loop:
        while waiting_for_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_start = False
                    game_loop = False
                    game_restart = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ball_random_x = random.choice(ball_random_x_list)
                        waiting_for_start = False
                        ball = pygame.Rect(ball_x_spawn, ball_y_spawn, 0, 0)
                        ball_dy = ball_y_speed
                        ball_dx = ball_random_x
                # checking the victory condition in waiting
            if score < SCORE_MAX:

                # clear screen
                screen.fill(COLOR_BLACK)

                # ball collision with top in waiting

                if ball.top <= 0:
                    ball.y = 1
                    ball_dy *= -1
                    bounce_sound_effect.play()

                # ball collision with player in waiting
                ball_in_paddle_range_y = player_1_position_and_design.y + (player_1_size_y / 2) >= ball.y + ball_y_size >= player_1_position_and_design.y

                if ball_in_paddle_range_y and player_1_waiting.x + 1000 >= ball.x >= player_1_waiting.x:
                    ball.y = player_1_position_and_design.y - ball_y_size
                    ball_dy *= -1
                    bounce_sound_effect.play()

                # ball collision with the wall in waiting
                if ball.right >= screen_size_x:
                    ball.x = screen_size_x - (ball_x_size + 1)
                    ball_dx *= -1
                    bounce_sound_effect.play()
                elif ball.left <= 0:
                    ball.x = 1
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
                screen.blit(player_lifes_text, player_lifes_rect)

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
                        ball_random_x = random.choice(ball_random_x_list)
                        ball = pygame.Rect(ball_x_spawn, ball_y_spawn, ball_x_size, ball_y_size)
                        ball_dy = ball_y_speed
                        ball_dx = ball_random_x
                        pygame.draw.rect(screen, COLOR_WHITE, ball)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    game_restart == True
                    game_loop == False
                    waiting_for_start == False

        # checking the victory condition
        if score < SCORE_MAX:

            # clear screen
            screen.fill(COLOR_BLACK)

            # ball collision with top and bottom
            # will be the scoring or losing conditions
            if ball.top >= screen_size_y:
                ball.y = ball_y_spawn
                ball_dy = 0
                ball_dx = 0
                ball = pygame.Rect(ball_x_spawn, ball_y_spawn, 0, 0)
                player_lifes -= 1
            if ball.top <= 0:
                ball.y = 1
                ball_dy *= -1
                bounce_sound_effect.play()

            # ball collision with player in game

            ball_in_paddle_range_y = player_1_position_and_design.y + (player_1_size_y / 2) >= ball.y + ball_y_size >= player_1_position_and_design.y
            ball_in_side_paddle_range = player_1_position_and_design.y + player_1_size_y >= ball.y + (ball_y_size / 2) >= player_1_position_and_design.y
            ball_in_right_paddle_side_x = player_1_position_and_design.x + player_1_size_x >= ball.x >= player_1_position_and_design.x + (player_1_size_x / 2)
            ball_in_left_paddle_side_x = player_1_position_and_design.x + (player_1_size_x / 2) >= ball.x + ball_x_size >= player_1_position_and_design.x

            if ball_in_paddle_range_y and player_1_position_and_design.x + player_1_size_x >= ball.x + (ball_x_size / 2) >= player_1_position_and_design.x:
                ball.y = player_1_position_and_design.y - ball_y_size
                ball_dy *= -1
                bounce_sound_effect.play()

            # collision with the right side
            if ball_in_side_paddle_range and ball_in_right_paddle_side_x:
                ball.x = player_1_position_and_design.x + player_1_size_x + 3
                ball_dy *= -1
                ball_dx *= -1
                bounce_sound_effect.play()

            # collision with the left side
            if ball_in_side_paddle_range and ball_in_left_paddle_side_x:
                ball.x = player_1_position_and_design.x - (ball_x_size + 3)
                ball_dy *= -1
                ball_dx *= -1
                bounce_sound_effect.play()

            # ball collision with the wall
            if ball.right >= screen_size_x:
                ball.x = screen_size_x - (ball_x_size + 1)
                ball_dx *= -1
                bounce_sound_effect.play()
            elif ball.left <= 0:
                ball.x = 1
                ball_dx *= -1
                bounce_sound_effect.play()

            # ball movement
            ball.x += ball_dx
            ball.y += ball_dy

            # player 1 right movement
            if player_1_move_right:
                player_1_position_and_design.right += player_speed
            else:
                player_1_position_and_design.right -= 0

            # player 1  movement
            if player_1_move_left:
                player_1_position_and_design.left -= player_speed
            else:
                player_1_position_and_design.left += 0

            # player 1 collides with left wall
            if player_1_position_and_design.left <= 0:
                player_1_position_and_design.left = 0

            # player 1 collides with right wall
            elif player_1_position_and_design.right >= screen_size_x:
                player_1_position_and_design.right = screen_size_x

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
            pygame.draw.rect(screen, COLOR_BLUE, player_design)
            pygame.draw.rect(screen, COLOR_WHITE, ball)
            screen.blit(score_text, score_text_rect)
            screen.blit(player_lifes_text, player_lifes_rect)
        else:
            player_design = player_1_waiting

        if player_lifes == 0:

            waiting_for_start == True

            while waiting_for_start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting_for_start = False
                        game_loop = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            ball_random_x = random.choice(ball_random_x_list)
                            waiting_for_start = False
                            ball = pygame.Rect(ball_x_spawn, ball_y_spawn, 0, 0)
                            ball_dy = ball_y_speed
                            ball_dx = ball_random_x
                    # checking the victory condition in waiting after death
                if score < SCORE_MAX:

                    # clear screen
                    screen.fill(COLOR_BLACK)

                    # ball collision with top in waiting after death

                    if ball.top <= 0:
                        ball.y = 1
                        ball_dy *= -1
                        bounce_sound_effect.play()

                    # ball collision with player in waiting after death
                    ball_in_paddle_range_y = player_1_position_and_design.y + (player_1_size_y / 2) >= ball.y + ball_y_size >= player_1_position_and_design.y

                    if ball_in_paddle_range_y and player_1_waiting.x + 1000 >= ball.x >= player_1_waiting.x:
                        ball.y = player_1_position_and_design.y - ball_y_size
                        ball_dy *= -1
                        bounce_sound_effect.play()

                    # ball collision with the wall in waiting after death
                    if ball.right >= screen_size_x:
                        ball.x = screen_size_x - (ball_x_size + 1)
                        ball_dx *= -1
                        bounce_sound_effect.play()
                    elif ball.left <= 0:
                        ball.x = 1
                        ball_dx *= -1
                        bounce_sound_effect.play()

                    # ball movement in waiting after death
                    ball.x += ball_dx
                    ball.y += ball_dy

                    # yellow obstacle collision in waiting after death
                    collision_yellow = ball.collidelist(yellow_obstacles)
                    if collision_yellow != -1:
                        ball_dy *= -1
                        bounce_sound_effect.play()

                    # red obstacle collision in waiting after death
                    collision_red = ball.collidelist(red_obstacles)
                    if collision_red != -1:
                        ball_dy *= -1
                        bounce_sound_effect.play()

                    # green obstacle collision in waiting after death
                    collision_green = ball.collidelist(green_obstacles)
                    if collision_green != -1:
                        ball_dy *= -1
                        bounce_sound_effect.play()

                    # orange obstacle collision in waiting after death
                    collision_orange = ball.collidelist(orange_obstacles)
                    if collision_orange != -1:
                        ball_dy *= -1
                        bounce_sound_effect.play()

                    # drawing obstacles in waiting after death
                    for red_obstacle in red_obstacles:
                        pygame.draw.rect(screen, COLOR_RED, red_obstacle)
                    for orange_obstacle in orange_obstacles:
                        pygame.draw.rect(screen, COLOR_ORANGE, orange_obstacle)
                    for green_obstacle in green_obstacles:
                        pygame.draw.rect(screen, COLOR_GREEN, green_obstacle)
                    for yellow_obstacle in yellow_obstacles:
                        pygame.draw.rect(screen, COLOR_YELLOW, yellow_obstacle)

                    # drawing objects in waiting after death
                    pygame.draw.rect(screen, COLOR_BLUE, player_1_waiting)
                    pygame.draw.rect(screen, COLOR_WHITE, ball)
                    screen.blit(score_text, score_text_rect)
                    screen.blit(player_lifes_text, player_lifes_rect)

                    # update screen after death
                pygame.display.flip()
                waiting_loop.tick(60)

        # update screen
        pygame.display.flip()
        game_clock.tick(60)

pygame.quit()
