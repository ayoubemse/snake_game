import pygame
import random
import sys

pygame.init()

game_over = False
screen_length = 700
screen_width = 500
disp = pygame.display.set_mode((screen_length, screen_width))
initial_length = 10
initial_width = 10
x0 = 350
y0 = 250
x=0
y=0
x_target = 400
y_target = 350

green = (0, 255, 0)
white = (255,255,255)
blue = (0,0,255)
cian = (0,0,100)
black = (0,0,0)
red = (255,0,0)
game_speed = 10
clock = pygame.time.Clock()
pygame.display.update()
pygame.display.set_caption("Snake game by Ayoub")

font = pygame.font.Font('freesansbold.ttf', 32)
font_score = pygame.font.Font('freesansbold.ttf', 18)
pause_font = pygame.font.Font('freesansbold.ttf', 20)
# create a text surface object,
# on which text is drawn on it.
text = font.render('Game Over', True, red, black)
textRect = text.get_rect()

textRect.center = (350, 250)

scoreG = 0
Pause_text = pause_font.render('Paused', True, white, black)
textRectPause = Pause_text.get_rect()
textRectPause.center = (350, 250)

def displayScore(score):

    score_text = font_score.render(f'Score : {score}', True, white, black)
    textRectScore = score_text.get_rect()

    textRectScore.center = (45, 30)
    disp.blit(score_text, textRectScore)

# score = font_score.render(f'{s}', True, white, black)
# surfaceScore = score.get_rect()

# surfaceScore.center = (45, 30)

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

list_coordinates = [[x0, y0]]
length_of_snake = 1

pause = False

startGame = False
easy_mode = True
quit_game = False

def unpause():
    global pause
    pause = False

def paused():
    global pause
    
    disp.fill(black)
    
    disp.blit(Pause_text, textRectPause)
    pygame.display.update()
    pause = True

def end_game():
    global game_over
    # disp.fill(black)
    disp.blit(text, textRect)
    disp.fill(black)
    pygame.display.update()
    # pygame.time.delay(600)
    game_over = True

objects = []
class Button():
    def __init__(self, x, y, width, height, button_text = "Easy", function=None, onePress = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_text = button_text
        self.function = function
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(button_text, True, cian)

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos): # if the mouse is above the button
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.function()
                elif not self.alreadyPressed:
                    self.function()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        
        disp.blit(self.buttonSurface, self.buttonRect)

def easyButton():
    global startGame
    global game_speed

    game_speed = 10
    startGame = True

def mediumButton():
    global startGame
    global game_speed
    global easy_mode

    easy_mode = False
    game_speed = 16
    startGame = True

def hardButton():
    global startGame
    global game_speed
    global easy_mode

    easy_mode = False
    game_speed = 22
    startGame = True

game_restarted = False

def restartButton():
    global game_over
    global startGame
    global left_pressed
    global right_pressed
    global up_pressed
    global down_pressed
    global x0
    global y0
    global x
    global y
    global length_of_snake
    global quit_game
    global list_coordinates
    global game_restarted
    game_restarted = True
    x0 = 350
    y0 = 250

    #for coord in list_coordinates:
    #   del coord
    # x=0
    # y=0
    # length_of_snake =1
    list_coordinates = [[x0, y0]]
    left_pressed = False
    right_pressed = False
    up_pressed = False
    down_pressed = False
    game_over = False
    quit_game = False
    startGame = True

def quitButton():
    global quit_game
    quit_game = True
    # pygame.quit()
    # quit()  

easyBut = Button(100, 250, 100, 60, "Easy", easyButton)
medBut = Button(250, 250, 150, 60, "Medium", mediumButton)
hardBut = Button(450, 250, 100, 60, "Hard", hardButton)


while not startGame:

    fontDiff = pygame.font.SysFont("comicsansms", 72)
    difficulty = fontDiff.render('Choose difficulty', True, (255,255,0), black)
    textRectScore = difficulty.get_rect()

    textRectScore.center = (340, 180)
    disp.blit(difficulty, textRectScore)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()
    
    pygame.display.flip()
    clock.tick(60)


while not game_over or not quit_game:


    if startGame:
        # displayScore(scoreG)
        pygame.draw.rect(disp, blue, (x_target, y_target, 10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not right_pressed:
                        x= -10
                        y = 0
                        left_pressed = True
                        right_pressed = False
                        up_pressed = False
                        down_pressed = False
                elif event.key == pygame.K_RIGHT:
                    if not left_pressed:
                        x= 10
                        y=0
                        left_pressed = False
                        right_pressed = True
                        up_pressed = False
                        down_pressed = False
                elif  event.key == pygame.K_UP:
                    if not down_pressed:
                        y= -10
                        x=0
                        left_pressed = False
                        right_pressed = False
                        up_pressed = True
                        down_pressed = False
                elif  event.key == pygame.K_DOWN:
                    if not up_pressed:
                        y= 10
                        x=0
                        left_pressed = False
                        right_pressed = False
                        up_pressed = False
                        down_pressed = True
                elif event.key == pygame.K_p:
                    paused()
                
        
        while pause:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_p:
                        unpause()

        x0+=x
        y0+=y
        #print(f"{x}, {y}", end="\n")
        l = [x0, y0]

        if game_restarted:
            x0 = 350
            y0=250
        if l in list_coordinates and len(list_coordinates) > 1: #check if snake bites itself after the game has started
            game_over = True
            startGame = False

        list_coordinates.append(l)

        if not easy_mode:
            if x0 < 0 or x0 >= screen_length or y0 < 0 or y0 >= screen_width:
                game_over = True

        else:
            if x0 < 0:
                x0 = screen_length
            elif x0 > screen_length:
                x0 = 0
            elif y0 < 0:
                y0 = screen_width
            elif y0 > screen_width:
                y0 = 0


        if x0 == x_target and y0 == y_target:
            scoreG+=1
            # displayScore(scoreG)
            pygame.draw.rect(disp, black, (x_target, y_target, 10, 10))
            x_target = random.randint(1,69) * 10
            y_target = random.randint(1,49) * 10
            length_of_snake+=1

        if length_of_snake < len(list_coordinates):
            del list_coordinates[0]


        if game_restarted:
            list_coordinates = [[x0, y0]]
            pygame.draw.rect(disp, green, (x0, y0, initial_length, initial_length))
            game_restarted = False
        else:
            for coord in list_coordinates:
                pygame.draw.rect(disp, green, (coord[0], coord[1], initial_length, initial_length))
        pygame.display.update()
        disp.fill(black)
        clock.tick(game_speed)

    if game_over:

        # disp.fill(black)
        pygame.draw.rect(disp, black, (x_target, y_target, 10, 10))
        pygame.display.update()
        pygame.display.flip()
        # disp.fill(black)
        
        restartButt = Button(250, 250, 130, 60, "Resume", restartButton)
        quitButt = Button(450, 250, 100, 60, "QUIT", quitButton)

        for object in objects[3:]:
            object.process()
        
        # pygame.display.update()
        # clock.tick(60)

disp.fill(black)
score_text = font.render(f'Your Score is : {scoreG}', True, white, black)
textRectScore = score_text.get_rect()

textRectScore.center = (screen_length/2, screen_width/2)
disp.blit(score_text, textRectScore)
pygame.display.update()
pygame.time.delay(600)
pygame.quit()
quit()