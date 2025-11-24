import pygame #Using pygame
import random #Using Random
pygame.init()

#Colors
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

#Move
speed = 50
ballSpeed = 5

#FPS
fps = 60
clock = pygame.time.Clock()

#Game title
pygame.display.set_caption("Test Game")

#Game Screen
displayW=800
displayH=600
gameScreen=pygame.display.set_mode((displayW,displayH))
gameScreen.fill(white)

#Load image
paddle=pygame.image.load("ImageForLearn/paddle.png")
ball=pygame.image.load("ImageForLearn/ball.png")

#Resiize image
paddle=pygame.transform.scale(paddle,(150,50))
ball=pygame.transform.scale(ball,(50,50))

#Setup Image
#Paddle's Image
paddle_Rect=paddle.get_rect()
paddle_Rect.centerx = displayW/2
paddle_Rect.centery = displayH-100
print(paddle_Rect)
#Ball object
ball_Rect=ball.get_rect()
ball_Rect.x=random.randint(0,displayW-50)
ball_Rect.y=10

#Score system
score = 0
font = pygame.font.Font("Fonts/Coiny.ttf",30)
scoreText = font.render("Score : " + str(score),True,white)
score_Rect = scoreText.get_rect()
score_Rect.topleft = (10,10)

#------------------Game event----------------------#
#If the player quits the game, the game will close.
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning=False

        #Keybord event
        #Movement and border limit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]and paddle_Rect.left>30: #or keys[pygame.K_a]:
            paddle_Rect.x-=speed
            #print("ArrowLeft")
        if keys[pygame.K_RIGHT]and paddle_Rect.right<displayW-30: #or keys[pygame.K_d]:
            paddle_Rect.x+=speed
            #print("ArrowRight")

    #Colider check
    if paddle_Rect.colliderect(ball_Rect):
        score+=10
        ball_Rect.x=random.randint(0,displayW-50)
        ball_Rect.y=10
        scoreText = font.render("Score : " + str(score),True,white)
        #print(score)

    #Ball Falling
    if ball_Rect.y<displayH:
            ball_Rect.y+=ballSpeed
    else:
        ball_Rect.x=random.randint(0,displayW-50)
        ball_Rect.y=10


    #Game screen
    gameScreen.fill(black) #Fill the game screen with white before drawing the player image.
    gameScreen.blit(paddle,paddle_Rect)
    gameScreen.blit(ball,ball_Rect)
    gameScreen.blit(scoreText,score_Rect)

    #Draw collider
    pygame.draw.rect(gameScreen,green,paddle_Rect,2)
    pygame.draw.rect(gameScreen,green,ball_Rect,2)

    pygame.display.update() #Update display

    #FPS
    clock.tick(fps)
pygame.quit()