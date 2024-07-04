import pygame
import time
import random

pygame.init()

snake_color=(216, 239, 211)
food_color=(250, 112, 112)
background_color=(69,71,75)
white=(255, 255, 255)
black=(0,0,0)

dis_width,dis_height=1000,600

dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Jyotsana')

clock=pygame.time.Clock()
snake_block, snake_speed=20,15

font_style=pygame.font.SysFont(None, 50)
score_font=pygame.font.SysFont(None, 35)

high_score=0

def display_score(score):
    value=score_font.render("Score:" + str(score),True,white)
    dis.blit(value, [0,0])
def display_high_score(high_score):
    value=score_font.render("High Score:" + str(high_score),True,white)
    dis.blit(value, [dis_width-200,0])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block], border_radius=4)
def message(msg, color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[dis_width/6, dis_height/3])
def game_over_animation():
    for _ in range(5):
        dis.fill(food_color)
        pygame.display.update()
        time.sleep(0.1)
        dis.fill(background_color)
        pygame.display.update()
        time.sleep(0.1)
def start_screen():
    while True:
        dis.fill(background_color)
        message("Press C to Start or Q to Quit", white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    return
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
def gameLoop():
    global high_score

    x1,y1=dis_width/2, dis_height/2
    x1_change, y1_change=0,0

    snake_List=[]
    Length_of_snake=1

    foodx=round(random.randrange(0,dis_width-snake_block)/20.0)* 20.0
    foody=round(random.randrange(0,dis_height-snake_block)/20.0)* 20.0

    score=0
    paused=False

    while True:
        while paused:
            message("Paused. Press P to Resume", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
                    paused=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x1_change==0:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT and x1_change==0:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP and y1_change==0:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN and y1_change==0:
                    y1_change=snake_block
                    x1_change=0
                elif event.key==pygame.K_p:
                    paused=True
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_over_animation()
            start_screen()
        x1 +=x1_change
        y1 +=y1_change
        dis.fill(background_color)
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block], border_radius=4)

        snake_Head=[x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x==snake_Head:
                game_over_animation()
                start_screen()
        
        our_snake(snake_block, snake_List)
        display_score(score)
        display_high_score(high_score)

        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, dis_width-snake_block)/20.0)*20.0
            foody=round(random.randrange(0, dis_height-snake_block)/20.0)*20.0
            Length_of_snake +=1
            score +=10
            if score > high_score:
                high_score=score

        clock.tick(snake_speed)

start_screen()
gameLoop()



