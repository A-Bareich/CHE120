"""
Andrea Bareich  ID: 20972966 Initials: AB
Faiven Anteneh  ID: 20949945 Initials: FA
Isabella Ristic ID: 20941943 Initials: IR
"""
"""
What we are changing
- add levels
- add lives (hit a bad guy lose life, hit a star gain life)
change characters
    - player: spaceship
    - baddie: aliens (multiple colours)
    - gain life: shooting star
- black background with white words for space theme
AB, FA, IR
"""
#imports -IR
import pygame, random, sys
from pygame.locals import *


WINDOWWIDTH = 1000          #original 600 variable for game screen width- FA
WINDOWHEIGHT = 700          #original 600, variable for game screen height (changed to fits screen better gives user more space to play) -FA
TEXTCOLOR = (255, 255, 255) #colour of text in RBG original (0,0,0) - black -FA
BACKGROUNDCOLOR = (0, 0, 0) #clolour of background in RGB original (255,255,255) - white -FA
FPS = 60                    #frame rate - 60frames per second - IR
#default level 1 values - AB
level = 1                   #set the level equal to 1 -added varaible for game levels- AB
BADDIEMINSIZE = 20          #minimum size for the bad guy in level 1-AB
BADDIEMAXSIZE = 40          #max size for bad guy in level 1 -AB
BADDIEMINSPEED = 1          #min speed of bad guy in level 1 -AB
BADDIEMAXSPEED = 5          #max speed of bad guy in level 1 -AB
ADDNEWBADDIERATE = 10       #original 8 -> amount of baddies in level 1 (1 baddie every x run throughs) -AB
PLAYERMOVERATE = 5          #rate the player moves -FA
#added variables for gain life character (star) -AB
GAINLIFESPEED = 7           #speed of gain life objects -AB
GAINLIFESIZE = 45           #size of gain life objects-AB
GAINLIFERATE = 25           #amount of gain lives created, larger number means less created (1 every 25 runs) -AB

def terminate():    #a function run when the game ends -IR
    pygame.quit()   #quit the game -IR
    sys.exit()      #system exits -IR

def waitForPlayerToPressKey(): 
    while True:                             #while we are waiting for the player to hit a key -FA
        for event in pygame.event.get():    #when an event happens (key is pressed, game is quit etc) -FA
            if event.type == QUIT:          #if the event type is quit - the user quits the game - FA
                terminate()                 #end the game -FA
            if event.type == KEYDOWN:       #if a button is pressed down -FA
                if event.key == K_ESCAPE:   #Pressing ESC key -FA
                    terminate()             #ends game -FA
                return 


def playerHasHitBaddie(playerRect, baddies):
    """
    A function to detect if the player has hit the bad guy -IR
    """
    for b in baddies: #for all the baddies - IR
        if playerRect.colliderect(b['rect']): #if the player has collided with the baddie's rectangle - IR
            baddies.remove(b) #add code to remove the baddie we hit (baddie(b)) so the player can continue playing (collision only happens once (lose 1 life)) - AB
            return True #return true (player has hit baddie) - IR
    return False # otheriwse player has not hit a baddie - return False - IR

#function below was added to detect when the player has hit the new star (gain life) object -AB
def playerHasHitLife(playerRect, gainLives): 
    """
    A function that detects if a player has hit a star (when the player hits this character they gain a life) -AB
    """
    for g in gainLives:                         #for all the star objects - AB
        if playerRect.colliderect(g['rect']):   #if the player has collided with the star (gainLives) rectangle -AB
            gainLives.remove(g)                 #removes the star character once collided so that the player can only hit it (and gain a life) once for each star - AB
            return True                         #the player has collided with a star, return true -AB
    return False                                #the player has not collided with a star, return false -AB

def drawText(text, font, surface, x, y):
    """
    A function that draws the text to the screen -IR
    """
    textobj = font.render(text, 1, TEXTCOLOR)   #creates a text object with the input text string and colour -IR
    textrect = textobj.get_rect()               #creates a rectangle for the text -IR
    textrect.topleft = (x, y)                   #draw the text x and y pixels from the top left -IR
    surface.blit(textobj, textrect)             #refresh the surface to see the text -IR

# Set up pygame, the window, and the mouse cursor.
pygame.init()                                                           #initialize pygame -IR
mainClock = pygame.time.Clock()                                         #create a clock object with pygame clock fucntion -IR
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))    #create the game screen -IR
pygame.display.set_caption('Dodger')                                    #show the word dodger on the screen -IR
pygame.mouse.set_visible(False)                                         #set it so you can not see the mouse cursor in the game screen -IR

# Set up the fonts.
font = pygame.font.SysFont(None, 48) #set the font to a size of 48 -IR

# Set up sounds.
gameOverSound = pygame.mixer.Sound('gameover.wav')  #set the gameover sound to be 'gameover.wav' -AB
pygame.mixer.music.load('background.mid')           #set the game background song to be 'background.mid' -AB

# Set up images.
playerImage = pygame.image.load('rocketship.png')          # change character for player (used to be 'player.png') - FA
playerRect = playerImage.get_rect()                         #a varaible for the player rectangle -FA
#original baddie Image = pygame.image.load('baddie.png')    #create a baddie character -IR
baddieImagepink = pygame.image.load('pinkbaddie.png')       #a character for the pink version of the bad guy -IR
baddieImageblue = pygame.image.load('bluebaddie.png')       #a character for the blue version of the bad guy -IR
baddieImagegreen = pygame.image.load('greenbaddie.png')     #a character for the green version of the bad guy -IR
baddieImagepurple= pygame.image.load('purplebaddie.png')    #a character for the purple version of the bad guy -IR
gainLifeImage = pygame.image.load('gain_lives.png')         #add gain live character - FA


# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR) #fill the background with the background colour defined at the top - AB
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3 +75), (WINDOWHEIGHT / 3)) #draw the dodger title on the screen -AB
#text below was added when levels were added, text centered on the screen -AB
drawText('Press 1 to play level 1 (default)', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50) #write press 1 for level 1 on the screen -AB
drawText('Press 2 to play level 2', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 80) #write press 2 for level 2 on the screen  -AB
drawText('Press 3 to play level 3', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 110) #write press 3 for level 3 on the screen -AB
#original(before adding levels): drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update() #update the screen to display text -AB

waitForPlayerToPressKey() #run the wait for player to press a key function - FA

topScore = 0 #set the top score to 0 when the game first begins - FA
while True:
    # Set up the start of the game.
    baddies = []                                                #create a list for the bad guy characters -FA
    gainLives = []                                              #create a list for the gain life star -FA
    score = 0                                                   #set the score to zero at the beginning of the game -FA
    lives = 3                                                   #set the lives to be 3 at the beginning of the game -FA
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)   #spawn the player character to the bottom center of the screen when game begins -FA
    moveLeft = moveRight = moveUp = moveDown = False            #set all varaible to false - the player is not moving when the game begins -IR
    reverseCheat = slowCheat = False                            #set the reverse cheat and slow cheat to false - they are not using the cheats when the game begins - IR
    baddieAddCounter = 0                                        #set the baddie counter to zero when the game starts (no bad guys have been created) -IR
    gainLivesAddCounter = 0                                     #set the gain lives counter to zero when the game starts (the player has not gained any lives) -IR
    pygame.mixer.music.play(-1, 0.0)                            #play the background music in a loop 0- IR
    #below choosing a level added to code -AB
    for event in pygame.event.get():                #while an event is happening (key is pressed/let go) -AB
            if event.type == pygame.locals.KEYUP: #if a key is released (after being pressed) -AB
                
                if event.key == pygame.locals.K_2:  #if the key released is 2 -AB
                    level = 2                       #set level equal to 2 -AB
                    BADDIEMINSIZE = 20              #minimum size for the bad guy in level 2 -AB
                    BADDIEMAXSIZE = 60              #max size for bad guy in level 2 -AB
                    BADDIEMINSPEED = 5              #min speed of bad guy in level 2 -AB
                    BADDIEMAXSPEED = 8              #max speed of bad guy in level 2 -AB
                    ADDNEWBADDIERATE = 8            #amount of baddies in level 1 (higher number means less baddies) -AB
                    GAINLIFERATE = 45               #ammount of gain lives created, larger number means less created (larger number = less spawned) -AB
                    PLAYERMOVERATE = 5              #rate the player moves -IR
                    break                           #leave the for loop, the level has been selected -AB
                if event.key == pygame.locals.K_3:  #if the key being released is 3 -AB
                    level = 3                       #set the level equal to 3 - AB
                    BADDIEMINSIZE = 20              #minimum size for the bad guy in level 3 -AB
                    BADDIEMAXSIZE = 80              #max size for bad guy in level 3 -AB
                    BADDIEMINSPEED = 8              #min speed of bad guy in level 3 -AB
                    BADDIEMAXSPEED = 11             #max speed of bad guy in level 3 -AB
                    ADDNEWBADDIERATE = 5            #amount of baddies in level 1 (higher number means less baddies) -AB
                    GAINLIFERATE = 65               #amount of gain lives created, larger number means less created (larger number = less spawned) -AB
                    PLAYERMOVERATE = 4              #rate the player moves -IR
                    break                           #leave the for loop, the level has been selected -AB
                if event.key == pygame.locals.K_1:  #if the key released is 1 -AB
                    level = 1                       #set the level equal to 1 -AB
                    BADDIEMINSIZE = 20              #minimum size for the bad guy in level 1 -AB
                    BADDIEMAXSIZE = 40              #max size for bad guy in level 1 -AB
                    BADDIEMINSPEED = 1              #min speed of bad guy in level 1 -AB
                    BADDIEMAXSPEED = 5              #max speed of bad guy in level 1 -AB
                    ADDNEWBADDIERATE = 10           #8 #amount of baddies in level 1 (higher number means less baddies) -AB
                    GAINLIFERATE = 25               #amount of gain lives created, larger number means less created (larger number = less spawned) -AB
                    PLAYERMOVERATE = 6              #rate the player moves -IR
                    break                           #leave the for loop, the level has been selected -AB
                    #above values choosen by full group (FA, IR, AB)

    while True:     #The game loop runs while the game part is playing -FA
        score += 1  #Increase score by 1 -FA

        for event in pygame.event.get():    #for an event in the game (key pressed, game quit etc) -IR
            if event.type == QUIT:          #if the event type is quit -IR
                terminate()                 #run the terminate function to end the game -IR

            if event.type == KEYDOWN:                           #if the event type is that a key was pressed -IR
                if event.key == K_z:                            #if the key pressed is z -IR
                    reverseCheat = True                         #set reverse cheat to true (characters move in reverse) -IR
                if event.key == K_x:                            #if the key that was pressed is x -IR
                    slowCheat = True                            #set slow cheat to true (characters move slowly) -IR
                if event.key == K_LEFT or event.key == K_a:     #if the left arrow key or the letter a was clicked move -AB
                    moveRight = False                           #set move to the right to false (player not moving right) -AB
                    moveLeft = True                             #set move to the left to true (player moving to the left) -AB
                if event.key == K_RIGHT or event.key == K_d:    #if the key pressed was the up arrow or d -AB
                    moveLeft = False                            #set move left to false (player not movin gto the left) -AB
                    moveRight = True                            #set move to the right to true (player moving to the right) -AB
                if event.key == K_UP or event.key == K_w:       #if the up arrow key or w was pressed -AB
                    moveDown = False                            #set move down to false (player is not moving down) -AB
                    moveUp = True                               #set move up to true (the player is moving up) -AB
                if event.key == K_DOWN or event.key == K_s:     #if the down arrow or s was pressed -AB
                    moveUp = False                              #set move up to false (the character is not moving up) -AB
                    moveDown = True                             #set move down to true (player moving down) -AB

            if event.type == KEYUP:       # if the event is a key is released -FA
                if event.key == K_z:      #if the key released was z -FA
                    reverseCheat = False  #reverse cheat = false (characters no longer moving in reverse) -FA
                    score = 0             #reset the score to zero -FA
                if event.key == K_x:      #if the key released was x -FA
                    slowCheat = False     #set slow cheat to false (characters no longer moving slower) -FA
                    score = 0             #reset the score to zero -FA
                if event.key == K_ESCAPE: #if the event was clicking escape -FA
                        terminate()       #runt he terminate function to end the game -FA

                if event.key == K_LEFT or event.key == K_a:     #if the left arrow or a key is released -AB
                    moveLeft = False                            #set move left to false (the player no longer moving left) -AB
                if event.key == K_RIGHT or event.key == K_d:    #if the right arrow or d is released -AB
                    moveRight = False                           #set move right to false (the player is no longer moving right) -AB
                if event.key == K_UP or event.key == K_w:       #if the up arrow or w is released -AB
                    moveUp = False                              #set move up to false (the player is no longer moving up) -AB
                if event.key == K_DOWN or event.key == K_s:     #if the down arrow or s is released -AB
                    moveDown = False                            #set move down to false (the player is no longer moving down) -AB

            if event.type == MOUSEMOTION:           #if the mouse is moving -AB
                # If the mouse moves, move the player where to the cursor.
                playerRect.centerx = event.pos[0]   #set the center of the x values of the player rectangle to the x position of the mouse -AB
                playerRect.centery = event.pos[1]   #set the center of the y values of the player rectangle to the y position of the mouse -AB
        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:   #if the reverse cheat or slow cheat is not happening -IR
            baddieAddCounter += 1                #add one baddie to the baddie counter -IR
            gainLivesAddCounter += 1             #add one gain life (star) to the gain life counter -AB (added when lives added)
        if baddieAddCounter == ADDNEWBADDIERATE: #if the add baddie counter variable is equal to the baddie rate -FA
            baddieAddCounter = 0                 # set the baddie counter to zero -FA
            randomCharacter = random.choice([baddieImagepink,baddieImageblue, baddieImagegreen, baddieImagepurple])                 #pick a random chracter from 4 alien options -IR
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)                                                               #pick a random integer between the min and max baddie sizes for the baddie size -IR
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),  #set the baddie rectangle to a random spot at the top of the screen -IR
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),                                                    #set the speed of the baddie to a random integer between min and max baddie speeds -IR
                        'surface':pygame.transform.scale(randomCharacter, (baddieSize, baddieSize)),                                #scale the chracter to fit the given size -IR
                        }
            baddies.append(newBaddie) # add the baddie to the end of the list of baddies -IR
            
        #if statement below added when lives were added to the game -AB
        if gainLivesAddCounter == GAINLIFERATE:     #if the gain lives counter is equal to gain life rate (time to add new star) -AB
            gainLivesAddCounter = 0                 #reset gain lives counter to zero -AB
            newGainLife = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - GAINLIFESIZE), 0 - GAINLIFESIZE, GAINLIFESIZE, GAINLIFESPEED),   #set the star rectangle to a random spot at the top of the screen -AB
                           'speed': GAINLIFESPEED, 'surface':pygame.transform.scale(gainLifeImage, (GAINLIFESIZE,GAINLIFESIZE))                 #set the star speed to the determined speed (defined at the top) and scale the image to fit -AB
                           }
            gainLives.append(newGainLife) #add the new gain life character (star) to the end of the gain lives list -AB
            
        # Move the player around.
        if moveLeft and playerRect.left > 0:                #if the player is trying to move left and it is not at the left end of the screen -FA
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)      #move the player to the left by their move rate -FA
        if moveRight and playerRect.right < WINDOWWIDTH:    #if the player is trying to move to the right and it is not at the right end of the screen -FA
            playerRect.move_ip(PLAYERMOVERATE, 0)           #move the player to the right by their move rate -FA
        if moveUp and playerRect.top > 0:                   #if the player is trying to move up and is not at the top of the screen -FA
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)      #move the player up by their move rate -FA
        if moveDown and playerRect.bottom < WINDOWHEIGHT:   #if the player is trying to move down and is not at the bottom of the screen -FA
            playerRect.move_ip(0, PLAYERMOVERATE)           #move the player down by the move rate -FA
        #the move rate is defined when choosing a level -FA

        # Move the baddies down
        for b in baddies:                           #for all the baddie characters
            if not reverseCheat and not slowCheat:  #if reverse cheat or slow cheat are not active (characters moving normally) -AB
                b['rect'].move_ip(0, b['speed'])    #move the baddie down by the specified speed -AB
            elif reverseCheat:                      #otherwise if it is reverse cheat -AB
                b['rect'].move_ip(0, -5)            #move the baddie upwards at 5 speed -AB
            elif slowCheat:                         #otherwise if it is slow cheat -AB
                b['rect'].move_ip(0, 1)             #move the baddie down slowly (speed = 1) -AB
         
        #for loop below was added when lives were added to the game
        for g in gainLives:                         #for all the gain life stars -AB
            if not reverseCheat and not slowCheat:  #if reverse cheat or slow cheat are not active (characters moving normally) -AB
                g['rect'].move_ip(0, g['speed'])    #move the gain life character down by the specified speed -AB
            elif reverseCheat:                      #otherwise if it is reverse cheat -AB
                 g['rect'].move_ip(0, -5)           #move the star upwards at 5 speed -AB
            elif slowCheat:                         #otherwise if it is slow cheat -AB
                g['rect'].move_ip(0, 1)             #move the star down slowly (speed = 1) -AB
                
        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:                    #for all the baddies in the list of baddies -AB
            if b['rect'].top > WINDOWHEIGHT:    #if their top os greater than the height of the window (below visible area) -AB
                baddies.remove(b)               #remove the baddie from the screen -AB
                
        #for loop below added when lives added to the game
        for g in gainLives[:]:                  #for all the stars(gain lives) in the gain life list -AB
            if g['rect'].top > WINDOWHEIGHT:    #if the top of the star is greater than the window height (below visible area) -AB
                gainLives.remove(g)             #delete the star from the screen -AB
                
        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR) #fill the background with the backgroung colour defined above -FA

        # Draw the score and top score.
        drawText('Level: %s' % (level), font, windowSurface, 10, 0)             #draw the level onto the screen -IR 
        drawText('Score: %s' % (score), font, windowSurface, 10, 40)            #draw the current score onto the screen -IR
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 80)     #draw the top score onto the screen -IR
        drawText('Lives: %s' % (lives), font, windowSurface, 10, 120)           #draw the number of lives on the screen -IR

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)     #draw the player on the screen -IR

        # Draw each baddie.
        for b in baddies:                               #fore all the baddies -FA
            windowSurface.blit(b['surface'], b['rect']) #draw the baddie on the screen -FA
        for g in gainLives:                             #for all the gain life stars -FA
            windowSurface.blit(g['surface'], g['rect']) #draw the star on the screen -FA

        pygame.display.update() #update the display with the new baddies and star (gain life characters) -FA

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            #originally game ends and code now in if lives == 0 was run -AB
            lives = lives-1 #changed when lives added, if player hit baddie, decrease their lives by 1 -AB
        
        #if statement below was added when lives were added -AB
        if playerHasHitLife(playerRect, gainLives): #if the function playerHasHitLife is true (they collided with a star) -AB
            lives += 1                              #add one life
            
        #original if PlayerHasHitBaddie == True
        if lives == 0:                                                          #if the number of lives equals zero (added when added lives - player has lost) -AB
            windowSurface.fill(BACKGROUNDCOLOR)                                 #fill the background with the backgroud colour defined at the top -AB
            drawText('Level: %s' % (level), font, windowSurface, 10, 0)         #write the level on the screen -AB
            drawText('Score: %s' % (score), font, windowSurface, 10, 40)        #write the current score to the screen -AB
            drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 80) #write the top score on the screen -AB
            drawText('Lives: %s' % (lives), font, windowSurface, 10, 120)       #write the number of lives to the screen -AB
            #above text is located in the top left corner of the screen -AB
            pygame.display.update()     #update the display to show the text -AB
            if score > topScore:        #if the score is larger than the top score -FA
                topScore = score        #set new top score -FA
            break                       #break out of loop - FA

        mainClock.tick(FPS) #limits game runtime to be the amount of frames (defined by FPS at the top) per second - AB

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()   #stop the background music -FA
    gameOverSound.play()        #play the game over sound -FA

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3 +40), (WINDOWHEIGHT / 3))                           #write game over to the screen - IR
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 40, (WINDOWHEIGHT / 3) + 50)    #write press a key to play again to the screen -IR
    pygame.display.update()             #update the display to show the text -IR
    waitForPlayerToPressKey()           #run wait for player to press key function -FA
    gameOverSound.stop() #stop the game over sound for the game - IR
