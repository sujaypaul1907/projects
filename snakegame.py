#firstly : pip install pygame

import pygame, time, random
from pygame.locals import *

pygame.init()
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)


win_width = 800
win_height = 600
window = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Snake Game")
time.sleep(5)

snake = 10
snake_speed = 15

font_style = pygame.font.SysFont('modernno20', 20)
score_font = pygame.font.SysFont('comicsansms', 30)

# fonts = pygame.font.get_fonts()
# print(fonts)

clock = pygame.time.Clock()

def user_score(score):
    number = score_font.render("Score : " + str(score), True, red)
    window.blit(number, [0,0])

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])
    

def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width/4, win_height/3])

def game_loop():
    gameover = False
    gameclose = False

    x1 = win_width/2
    y1 = win_height/2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 2

    foodx = round(random.randrange(0, win_width - snake)/10.0)*10.0
    foody = round(random.randrange(0, win_height - snake)/10.0)*10.0

    while not gameover:

        while gameclose == True:
            window.fill(grey)
            message("You Lost!! press P to play again and press Q to quit")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #gameover = True
                        #gameclose = True
                        pygame.quit()

                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0

                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake

                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake


        if x1 > win_width or x1 < 0 or y1 > win_height or y1 < 0:
            gameclose = True

        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)

        if len(snake_length_list) > snake_length:
            del snake_length_list[0]
        
        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake)/10.0)*10.0
            foody = round(random.randrange(0, win_height - snake)/10.0)*10.0
            snake_length += 1

        clock.tick(snake_speed)


    pygame.quit()
    quit()

game_loop()



