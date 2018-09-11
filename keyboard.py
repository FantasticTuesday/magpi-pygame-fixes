import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# Pygame Variables
pygame.init()
clock = pygame.time.Clock()

windowWidth = 800
windowHeight = 800

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Keyboard!')

# Square Variables
playerSize = 20
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 0.0
playerVY = 0.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False

#test variables
printkeypress = False

def move():

        global playerX, playerY, playerVX, playerVY, haveJumped, gravity

        moveX = False
        # Move left 
        if leftDown and not rightDown:
                #flag that we will move in x, set speed if not in left-wards motion
                moveX = True
                if playerVX > -moveSpeed:
                        playerVX = -moveSpeed

        # Move right
        if rightDown and not leftDown:
                #flag that we will move in x, set speed if not currently moving left
                moveX = True
                if playerVX < moveSpeed:
                        playerVX = moveSpeed

        #will this move cause clipping? set move to false and put box at edge of window
        if playerX + playerVX <= 0.0:
                playerX = 0
                playerVX = 0.0
                moveX = False
        if playerX + playerVX >= windowWidth - playerSize:
                playerX = windowWidth - playerSize
                playerVX = 0.0
                moveX = False

        if playerVY > 1.0:
                playerVY = playerVY * 0.9
        else :
                playerVY = 0.0
                haveJumped = False

        # Is our square in the air? Better add some gravity to bring it back down!
        if playerY < windowHeight - playerSize:
                playerY += gravity
                gravity = gravity * 1.1
        else :
                playerY = windowHeight - playerSize
                gravity = 1.0

        playerY -= playerVY
        
        if moveX:
                playerX += playerVX
                moveX = False

        if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
                if haveJumped == False:
                        playerVX = playerVX * 1.1

# How to quit our program
def quitGame():
        pygame.quit()
        sys.exit()
        
print(leftDown,rightDown,haveJumped)
while True:

        surface.fill((0,0,0))

        pygame.draw.rect(surface, (255,0,0), (playerX, playerY, playerSize, playerSize))



        # Get a list of all events that happened since the last redraw
        for event in GAME_EVENTS.get():

                if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_LEFT:
                                leftDown = True
                                if printkeypress:
                                        print("Key left down.")
                        if event.key == pygame.K_RIGHT:
                                rightDown = True
                                if printkeypress:
                                        print("Key right down.")
                        if event.key == pygame.K_UP:
                                if not haveJumped:
                                        haveJumped = True
                                        playerVY += jumpHeight
                                if printkeypress:
                                        print("Key up down.")
                        if event.key == pygame.K_ESCAPE:
                                quitGame()

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                                leftDown = False
                                playerVX = 0.0
                                if printkeypress:
                                        print("Key left up.")
                        if event.key == pygame.K_RIGHT:
                                rightDown = False
                                playerVX = 0.0
                                if printkeypress:
                                        print("Key right up.")

                if event.type == GAME_GLOBALS.QUIT:
                        quitGame()

        move()

        clock.tick(60)
        pygame.display.update()
