import pygame
import sys
import time
import random
import sys
from pygame.locals import *
#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]

snake_body = [[100,50],[90,50],[80,50]]
snake_length=3
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [200,120]
food_spawn = True

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
    global direction
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and direction!='RIGHT':
                direction='LEFT'
            if event.key == K_RIGHT and direction!='LEFT':
                direction='RIGHT'
            if event.key == K_UP and direction!='DOWN':
                direction='UP'
            if event.key == K_DOWN and direction!='UP':
                direction='DOWN'


def create_food():
    global food_pos
    global food_spawn
    global game_window
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    if food_spawn == True:
        food_pos[0]=random.randint(20,700)
        food_pos[1]=random.randint(20,460)
        food_spawn = False
    pygame.draw.rect(game_window,(120,120,0),pygame.Rect(food_pos[0],food_pos[1],10,10))




            

def update_snake():
    global score
    global food_spawn
    global snake_pos
    global snake_body
    global direction
    global game_window
    global snake_length
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    if direction== 'LEFT':
        snake_pos[0] = snake_pos[0]-10
    if direction== 'RIGHT':
        snake_pos[0] =snake_pos[0]+ 10
    
    if direction== 'UP':
        snake_pos[1] =snake_pos[1]- 10
    
    if direction== 'DOWN':
        snake_pos[1] =snake_pos[1]+ 10
    snake_body.append([snake_pos[0], snake_pos[1]])
    #snake eats
    if pygame.Rect(snake_pos[0], snake_pos[1], 10, 10).colliderect(food_pos[0], food_pos[1], 10, 10):   
        food_spawn = True
        score += 10
        snake_length+=1
    else:
        snake_body.pop(0)

    
    for i in snake_body:
        pygame.draw.rect(game_window, (255, 0, 0),
                         pygame.Rect(i[0],i[1], 9, 9))
    

    #snake goes out of frame, game ends     
    if snake_pos[0] <= 10 or snake_pos[0] >= frame_size_x - 10 or snake_pos[1] <= 10 or snake_pos[1] >= frame_size_x - 10:
        game_over()
    #for block in snake_body:
     #   pygame.draw.rect(game_window, (255, 0, 0), pygame.Rect(block[0], block[1], 9, 9))
    #if touches own body
    #for bodypart in snake_body[1:]:
     #   if snake_pos[0]==bodypart[0] and snake_pos[1]==bodypart[1]:
      #      game_over()
    for bodypart in snake_body[:-1]:
        if pygame.Rect(snake_pos[0], snake_pos[1], 10, 10).colliderect(pygame.Rect(bodypart[0], bodypart[1], 10, 10)):
            game_over()



    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    





    # End the game if the snake collides with the wall or with itself. 
    







def show_score():
    global score
    global game_window
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score:"+str(score), True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (80, 40)
    game_window.blit(text, textRect)






def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    game_window.fill((0, 0, 0))
    show_score()
    create_food()
    update_snake()
    pygame.display.flip()





def game_over():
    global frame_size_x
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    font=pygame.font.Font('freesansbold.ttf',36)
    game_ = font.render("GAME OVER!! Your score is "+str(score),True,(250,0,0))
    textRect1 = game_.get_rect()
    textRect1.center = (frame_size_x/2, 150)
    game_window.blit(game_,textRect1)  
    pygame.display.update()
    time.sleep(3)
    sys.exit()






# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run

    check_for_events()
    update_screen()

    

    # To set the speed of the screen
    fps_controller.tick(25)
