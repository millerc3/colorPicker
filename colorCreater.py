import pygame
import random

def rect(x, y, w, h, color, thickness=0):
    pygame.draw.rect(gameDisplay, color, (x, y, w, h), thickness)

def newColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
    

class progVars:
    width = 400
    height = 550
    margin = 50
    title = 'color-creater'

class colors:
    black = (0,0,0)
    gray = (192, 192, 192)
    darkGray = (32, 32, 32)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)
    yellow = (255, 255, 0)
    orange = (255, 128, 0)
    

class Button:
    def __init__(self, x, y, w, h, color, id):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.id = id
    
    def draw(self):
        rect(self.x, self.y, self.w, self.h, self.color)

pygame.init()
    
gameDisplay = pygame.display.set_mode((progVars.width, progVars.height))
pygame.display.set_caption(progVars.title)

clock = pygame.time.Clock()

filename = 'testingData.txt'
file = open(filename, 'a')


def gameLoop():
    done = False
    pressed = False

    currColor = newColor()
    while not done:
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                file.close()
                done = True

        # add background
        gameDisplay.fill(colors.gray)

        # add color window
        colorWidth = progVars.width - 2*progVars.margin
        borderSize = 2
        rect(progVars.margin-borderSize, progVars.margin-borderSize, colorWidth+borderSize*2, colorWidth + borderSize*2, colors.darkGray)
        rect(progVars.margin, progVars.margin, colorWidth, colorWidth, currColor)

        buttonWidth = 60
        buttonHeight = 30

        buttonDiffX = (progVars.width - 4*buttonWidth)/5
        buttonDiffY = buttonHeight/2
        buttonStartX = buttonDiffX
        buttonStartY = colorWidth + 2*progVars.margin
        

        # add buttons
        buttons = []
        # ROW 1
        blueButton = Button(buttonStartX, buttonStartY, buttonWidth, buttonHeight, colors.blue, '1')
        blueButton.draw()
        buttons.append(blueButton)

        redButton = Button(buttonStartX + buttonWidth + buttonDiffX, buttonStartY, buttonWidth, buttonHeight, colors.red, '2')
        redButton.draw()
        buttons.append(redButton)

        greenButton = Button(buttonStartX + 2*(buttonWidth + buttonDiffX), buttonStartY, buttonWidth, buttonHeight, colors.green, '3')
        greenButton.draw()
        buttons.append(greenButton)

        yellowButton = Button(buttonStartX + 3*(buttonWidth + buttonDiffX), buttonStartY, buttonWidth, buttonHeight, colors.yellow ,'4')
        yellowButton.draw()
        buttons.append(yellowButton)

        # ROW 2
        purpleButton = Button(buttonStartX + 0*(buttonWidth + buttonDiffX), buttonStartY + 1*(buttonHeight + buttonDiffX), buttonWidth, buttonHeight, colors.purple, '5')
        purpleButton.draw()
        buttons.append(purpleButton)

        orangeButton = Button(buttonStartX + 1*(buttonWidth + buttonDiffX), buttonStartY + 1*(buttonHeight + buttonDiffX), buttonWidth, buttonHeight, colors.orange ,'6')
        orangeButton.draw()
        buttons.append(orangeButton)

        blackButton = Button(buttonStartX + 2*(buttonWidth + buttonDiffX), buttonStartY + 1*(buttonHeight + buttonDiffX), buttonWidth, buttonHeight, colors.black ,'7')
        blackButton.draw()
        buttons.append(blackButton)

        whiteButton = Button(buttonStartX + 3*(buttonWidth + buttonDiffX), buttonStartY + 1*(buttonHeight + buttonDiffX), buttonWidth, buttonHeight, colors.white, '8')
        whiteButton.draw()
        buttons.append(whiteButton)

        

        if pygame.mouse.get_pressed()[0]:
            if not pressed:
                for button in buttons:
                    if (mouseX > button.x and mouseX < button.x+buttonWidth and mouseY > button.y and mouseY < button.y + buttonHeight):
                        file.write(str(currColor) + ' : ' + button.id + '\n')
                        currColor = newColor()
            pressed = True
        else:
            pressed = False
                    
        # draw screen
        pygame.display.update()


gameLoop()
pygame.quit()
file.close()
quit()