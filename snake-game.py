import pygame
import random
import os
# initialise pygame
pygame.init()
pygame.mixer.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)

# Screen Variables
screen_width = 900
screen_height = 600

# creating game window
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game With Prasanna")
pygame.display.update()

bgimg1 = pygame.image.load("image/bck.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()
bgimg2 = pygame.image.load("image/Welcome.PNG")
bgimg2 = pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30)

def screen_score(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,slist,ssize):
    for x,y in slist:
        pygame.draw.rect(gamewindow, color, [x, y, ssize, ssize])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimg2, (0, 0))
        # screen_score("Welcome to Snake Land",black,screen_width/3,screen_height/3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('music/bckgrd.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(30)

# creating a game loop:
def gameloop():
    # declaring game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 10
    fps = 30
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    score = 0
    snake_list = []
    snake_length = 1
    food_x = random.randint(30, screen_width / 2)
    food_y = random.randint(30, screen_height / 2)
    if (not os.path.exists("hscore.txt")):
        f.write("0")
    with open("hscore.txt","r") as f:
        hscore = f.read()

    while not exit_game:
        if game_over:
            with open("hscore.txt", "w") as f:
                f.write(str(hscore))
            gamewindow.fill(white)
            screen_score("Game Over! Press Enter to Continue",red,screen_width/3,screen_height/3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('music/Welcome.mp3')
                        pygame.mixer.music.play()
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_t:
                        score += 10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score = score + 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length += 5
                if score > int(hscore):
                    hscore = score
            gamewindow.fill(white)
            gamewindow.blit(bgimg1,(0,0))
            screen_score("Score: "+str(score)+"  High Score: "+str(hscore),blue,5,5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('music/over.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('music/over.mp3')
                pygame.mixer.music.play()
            plot_snake(gamewindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
pygame.mixer.music.load('music/Welcome.mp3')
pygame.mixer.music.play()
welcome()