"""
Andrea Bareich ID: 20972966 Initials: AB

"""
"""
What we are changing
- add levels or lives
change characters
- player: spaceship
- baddie: asteroides and aliens
- lives: gas or food <-
background
"""
import pygame, random, sys
from pygame.locals import *


WINDOWWIDTH = 600 #1000
WINDOWHEIGHT = 600#700 fits screen better gives user more space to play
TEXTCOLOR = (0, 0, 0) #colour of text in RBG = black
BACKGROUNDCOLOR = (255, 255, 255) # clolour of background in RGB = white
FPS = 60 # frame rate - 60frames per second
BADDIEMINSIZE = 10#minimum size for the bad guy
BADDIEMAXSIZE = 40#max size for bad guy
BADDIEMINSPEED = 1#min speed of bad guy
BADDIEMAXSPEED = 8#max speed of bad guy
ADDNEWBADDIERATE = 6#8 #amount of baddies higher numer means less baddies
PLAYERMOVERATE = 5#rate the player moves

def terminate(): #when the game ends
    pygame.quit() # quit the game
    sys.exit() #system exits

def waitForPlayerToPressKey(): #
    while True:#while we are waiting for the player to hit a key
        for event in pygame.event.get(): 
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
def getLevel():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                if event.key == K_1:
                    BADDIEMINSIZE = 20#minimum size for the bad guy
                    BADDIEMAXSIZE = 40#max size for bad guy
                    BADDIEMINSPEED = 1#min speed of bad guy
                    BADDIEMAXSPEED = 5#max speed of bad guy
                    ADDNEWBADDIERATE = 10#8 #amount of baddies higher numer means less baddies

                elif event.key == K_2:
                    BADDIEMINSIZE = 5#minimum size for the bad guy
                    BADDIEMAXSIZE = 20#max size for bad guy
                    BADDIEMINSPEED = 3#min speed of bad guy
                    BADDIEMAXSPEED = 5#max speed of bad guy
                elif event.key == K_3:
                    BADDIEMINSIZE = 20#minimum size for the bad guy
                    BADDIEMAXSIZE = 40#max size for bad guy
                    BADDIEMINSPEED = 5#min speed of bad guy
                    BADDIEMAXSPEED = 10#max speed of bad guy 
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# Set up images.
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')
baddieImage2 = pygame.image.load('baddie.png')


# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press 1 to play level 1', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
drawText('Press 2 to play level 2', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 70)
drawText('Press 3 to play level 3', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 90)

#drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
getLevel()

#waitForPlayerToPressKey()

topScore = 0
while True:
    # Set up the start of the game.
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing.
        score += 1 # Increase score.

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where to the cursor.
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            randomCharacter = random.choice([baddieImage,baddieImage2])
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(randomCharacter, (baddieSize, baddieSize)),
                        }

            baddies.append(newBaddie)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the baddies down.
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie.
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
