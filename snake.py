import pygame
import random

pygame.init()

list_five_num = [i for i in range(5, 1000, 5)]

white = (255, 255, 255)
red = (255, 0, 0)
full_red = (255, 0, 0)
green = (49, 214, 77)
black = (0, 0, 0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("", 25)
score_font = pygame.font.SysFont("", 35)


def Your_score(score):
    value = score_font.render(str(score), True, white)
    dis.blit(value, [0, 0])


def our_snake(snakeblock, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snakeblock, snakeblock])


def message(msg, color, num, num2):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / num, dis_height / num2])


def gameStart():
    global red
    v = random.randint(140, 255)
    t = random.randint(140, 255)
    s = random.randint(140, 255)
    random_color = (v, t, s)
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            dis.fill(black)
            message("GAME OVER! "
                    "Press SPACE-Play Again, press ESC to end", full_red, 8, 2)
            message(f'You score: {Length_of_snake - 1}', red, 8, 3)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameStart()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width:
            x1 = 0
        elif x1 == -10:
            x1 = dis_width - 10
        elif y1 >= dis_height:
            y1 = 0
        elif y1 == -10:
            y1 = dis_height - 10
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, random_color, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if snake_Head == x:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if snake_Head[0] == foodx and snake_Head[1] == foody:
            foodx, foody = round(random.randrange(10, dis_width - snake_block) / 10.0) * 10.0, \
                           round(random.randrange(10, dis_height - snake_block) / 10.0) * 10.0
            v = random.randint(140, 255)
            t = random.randint(140, 255)
            s = random.randint(140, 255)
            random_color = (v, t, s)
            if Length_of_snake - 1 in list_five_num:
                Length_of_snake += 2
            else:
                Length_of_snake += 1
                red = random_color
            pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()


gameStart()
