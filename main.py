# imorting pygame 
import pygame
# initialising pygame
pygame.init()
# settign the display 
display=pygame.display.set_mode((1400,800))
# importign time 
import time

# settign teh initial position for the arrow
arrowcount = 0
arrowx = 80
arrowy = 397
arrowmove =0 

# setting the initial value for the board 
rectx = 1380
recty = 10
recty_move=0

# settign the score and the state of the game 
a_score =0 
score = 0
state = 'ready'


run=True 
while run:
    #  fiiling the dispaly with the colour sky blue as background 
    display.fill((0,150,150)) 
    for event in pygame.event.get():
        # condition to close the window 
        if event.type ==pygame.QUIT: 
            run = False
        if state=='ready':
            #  lettign the board to move after pressing the space key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    recty_move = 1
                    state = 'inprocess'
        # settign the s key to shoot te arrow when required
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                #  setting the movement speed of the arrow 
                arrowmove = 5
                arrowcount+= 1


    # drawing the board on the right side of the window with the coordinates  
    rectangle1 = pygame.draw.rect(display,(0,0,225),(rectx,recty,10,120))
    rectangle2 = pygame.draw.rect(display,(0,0,0),(rectx-10,recty+30,10,60))
    rectangle3 = pygame.draw.rect(display,(225,0,0),(rectx-20,recty+45,10,30))
    # moveing the board up and down 
    recty += recty_move

    # drawign the arrow shooter 
    arrowbox = pygame.draw.rect(display,(225,225,0),(0,380,80,40))

    # drawign the arrow at the initial posiiton 
    arrow = pygame.draw.rect(display,(225,0,225),(arrowx,arrowy,60,6))
    # deciding the movement of teh arrow 
    arrowx += arrowmove
    pygame.draw.rect

    # setting the boundary condition for the board  
    if recty==0 or recty+120 == 800:
        recty_move = -recty_move
    
    # setting the arrow to the initial position after crossign the window 
    if arrowx == 1400:
        arrowx = 80
        arrowmove = 0
    
    # checking arrow whether it strike at blue region
    if (recty<arrowy+3<recty+120)  and (arrowx+50 == rectx) :
        a_score = 5
        arrowmove = 0
        time.sleep(1)
        arrowx = 80
    # checking the arrow whether it strike at black region 
    if (recty+30<arrowy+3<recty+30+60) and (arrowx+50 == rectx-10):
        a_score = 7
        arrowmove= 0
        time.sleep(1)
        arrowx = 80
    # checking the arrow whether it strike at red region
    if (recty+45<arrowy+3<recty+45+30) and (arrowx+50 == rectx-20):
        a_score = 10
        arrowmove=0 
        time.sleep(1)
        arrowx = 80
    # incrimenting the score
    score+= a_score
    a_score = 0
    # quiting the game after hitting 10 arrows
    if arrowcount ==11:
        run = False



    pygame.display.update()
print(score)
