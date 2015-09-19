# Abdulaziz Jamal ID :200745537

import random
import pygame
import sys
from pygame.locals import *

Snakespeed= 16
Window_Width= 800 # Windows Width
Window_Height= 500 # Windows Hight
Cell_Size = 20 # Width and height of the cells
assert Window_Width % Cell_Size == 0, "Window width must be a multiple of cell size." # Ensuring that the cells fit perfectly in the window. eg if cell size was 10 and window width or windowheight were 15 only 1.5 cells would fit.
assert Window_Height % Cell_Size == 0, "Window height must be a multiple of cell size."  # Ensuring that only whole integer number of cells fit perfectly in the window.
Cell_W= int(Window_Width / Cell_Size) # Cell Width 
Cell_H= int(Window_Height / Cell_Size) # Cell Height

#Color 
White= (255,255,255)
Black= (0,0,0)
Red= (255,0,0) # Defining element colors for the program.
Green= (0,255,0)
Dark_Green= (0,155,0)
Dark_Gray= (40,40,40)
Yellow= (255,255,0)
Red_Dark= (150,0,0)
Blue= (0,0,255)
Blue_Dark= (0,0,150)



Background = Black # Background color


UP = 'up'
DOWN = 'down'      # Defining keyboard keys.  
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # Syntactic of the snake head.

# Codes in top are step up of constant variable.
#_______________________________________________________________________________

def main(): # Main function called def Startgame() because we want to show the start screen when program starts.
    global SnakespeedCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    SnakespeedCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((Window_Width, Window_Height)) 
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18) # Font type and size.
    pygame.display.set_caption('Snake !') # Display function. 

    Startscreen()
    while True: # This loop will countine running untile the program terminates.
        Startgame()
        gameover()


def Startgame(): # Main part of code.
    # Set a random start point for the snake but not close to the edges.
    startx = random.randint(5, Cell_W - 6) # Random coordinates for snake to start.
    starty = random.randint(5, Cell_H - 6)
    snakeCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT # Direction where the snake is going to start.

    # Start the red apple in a random point.
    apple = Randomlocationforapple()

    while True: # Main game loop
        for event in pygame.event.get(): # Event handling loop
            if event.type == QUIT: # If user quit using the x on pygame go to function terminate()and shut down.
                terminate() 
            elif event.type == KEYDOWN: # Check the keys is pressed down.
                if (event.key == K_LEFT ) and direction != RIGHT: # If user press left on keyboard turn left.
                    direction = LEFT
                elif (event.key == K_RIGHT ) and direction != LEFT: # If user press right on keyboard turn right.
                    direction = RIGHT
                elif (event.key == K_UP ) and direction != DOWN: # If user press up on keyboard turn up.
                    direction = UP
                elif (event.key == K_DOWN ) and direction != UP: # If user press down on keyboard turn down.
                    direction = DOWN
                elif event.key == K_ESCAPE: # If user press ESC in keyboard go to function terminate() and shut down.
                    terminate()

        # Check if the Snake has hit itself : GAME OVER
        for snakeBody in snakeCoords[1:]:
            if snakeBody['x'] == snakeCoords[HEAD]['x'] and snakeBody['y'] == snakeCoords[HEAD]    ['y']: 
                return 

        # Check if Snake has eaten an apple 
        if snakeCoords[HEAD]['x'] == apple['x'] and snakeCoords[HEAD]['y'] == apple['y']:
            apple = Randomlocationforapple() # Select any new apple in random location on the screen. 
        else:
            del snakeCoords[-1] 

        # Move the snake by adding a segment in the direction it is moving
        if direction == UP:
            if snakeCoords[HEAD]['y'] == -1: 
                newHead = {'x': snakeCoords[HEAD]['x'], 'y': Cell_H-1}
            else:
                newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] - 1}

        elif direction == DOWN:  
            if snakeCoords[HEAD]['y'] == Cell_H: # If lower wall then move the head to emerge from upper wall
                newHead = {'x': snakeCoords[HEAD]['x'], 'y': 0}
            else:
                newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] + 1}

        elif direction == LEFT:
            if snakeCoords[HEAD]['x'] == -1: # If left wall then move the head to emerge from right wall
                newHead = {'x': Cell_W-1, 'y': snakeCoords[HEAD]['y']}
            else:
                newHead = {'x': snakeCoords[HEAD]['x'] - 1, 'y': snakeCoords[HEAD]['y']}

        elif direction == RIGHT:
            if snakeCoords[HEAD]['x'] == Cell_W: # If right wall then move the head to emerge from left wall
                newHead = {'x': 0, 'y': snakeCoords[HEAD]['y']}
            else:
                newHead = {'x': snakeCoords[HEAD]['x'] + 1, 'y': snakeCoords[HEAD]['y']}
        snakeCoords.insert(0, newHead)

        DISPLAYSURF.fill(Background)
        BackgroundGrid()
        snakedesign(snakeCoords)
        Appledesign(apple)
        PointsDisplay(len(snakeCoords) - 3)
        pygame.display.update()
        SnakespeedCLOCK.tick(Snakespeed)

def PressKey(): # Apppear "press any key to start the game" on the screen.
    pressKeySurf = BASICFONT.render('Press any key to start the game.', True, White) # Press any key text and the location where it will appear in the in the screen.
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (Window_Width - 200, Window_Height - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def Keycheck(): # Checking for key for any events that quits if not the function will return back to be empty list.
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def Startscreen(): # This appear before the player start the game which is an new screen where the snake title routate around these are the font and color and size of the text as well as it gives a chance for the player to start the game.
    titleFont = pygame.font.Font('freesansbold.ttf', 100) # Title font with type font and font size.
    Title1 = titleFont.render('Snake!', True, White, Dark_Green) # Text "snake!" as well as the color of the font.
    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(Background)
        rotatedSurf1 = pygame.transform.rotate(Title1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (Window_Width / 2, Window_Height / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        PressKey()

        if Keycheck():
            pygame.event.get() # Clear event queue
            return
        pygame.display.update() # Redraws the display if argument list is empty.
        SnakespeedCLOCK.tick(Snakespeed)
        degrees1 += 3 # Rotate by 3 degrees each frame.
        degrees2 += 7 # Rotate by 7 degrees each frame.


def terminate(): # Using this function to shutdown the program correctly wthout errors.
    pygame.quit()
    sys.exit()
    pygame.init()
    quit()

def Randomlocationforapple(): # Deciding Where the red apple appers in random places.
    return {'x': random.randint(0, Cell_W - 1), 'y': random.randint(0, Cell_H - 1)} # Selecting new coordinates for the red apple onces the sanke eats it which means this function will returns dictionary with keys x and y with vaule set in XY coorinates. 


def gameover(): # This function describes the Game-Over word appear when the player hit any part of the snake. 
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)# Main font and size of the fornt.
    gameSurf = gameOverFont.render('Game', True, White)
    overSurf = gameOverFont.render('Over', True, White)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (Window_Width / 2, 10) # Location of the text appear in the screen.
    overRect.midtop = (Window_Width / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    PressKey()
    pygame.display.update()
    pygame.time.wait(500)
    Keycheck() # Clear out any key presses in the event.

    while True:
        if Keycheck():
            pygame.event.get() # Clear event to get list of the events that occurred sinc ethe last time was called.
            return

def PointsDisplay(Points): # Point display appear in the top right on the screen when the game starts.
    PointsSurf = BASICFONT.render('Points: %s' % (Points), True, White) # Linking the points scores with the snake when it eates the apple.
    PointsRect = PointsSurf.get_rect()
    PointsRect.topleft = (Window_Width - 120, 10)
    DISPLAYSURF.blit(PointsSurf, PointsRect)


def snakedesign(snakeCoords): # Snake design.  
    for coord in snakeCoords:
        x = coord['x'] * Cell_Size
        y = coord['y'] * Cell_Size
        snakeSegmentRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(DISPLAYSURF, Dark_Green, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, Cell_Size - 8, Cell_Size - 8)
        pygame.draw.rect(DISPLAYSURF, White, snakeInnerSegmentRect)


def Appledesign(coord): # Apple design.
    x = coord['x'] * Cell_Size # Cell size in pixels coordinates of X and Y.
    y = coord['y'] * Cell_Size
    appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
    pygame.draw.rect(DISPLAYSURF, Red, appleRect)


def BackgroundGrid(): # Designing BackgroundGrid for player so the snake move with the grid in order to eat the apple.
    for x in range(0, Window_Width, Cell_Size): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, Dark_Gray, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, Dark_Gray, (0, y), (Window_Width, y))




if __name__ == '__main__': # This the main function to start the game when every global variable defined.
    try:
        main()
    except SystemExit:
            pass
    
