# load program
# fit model to current dataset
# draw pygame screen
# input RGB color and expected
# log input and add to dataset
# test input to the current model
    # model.predict
# print the prediction to cmd
# accept a new RGB value


import numpy as np
import pygame
import tensorflow as tf
import random
import os

# CLASSES TO USE THROUGHOUT ############################################

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

# FUNCTIONS TO USE THROUGHOUT ##########################################

# pygame functions
def rect(x, y, w, h, color, thickness=0):
    pygame.draw.rect(gameDisplay, color, (x, y, w, h), thickness)

def newColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

# model to test the prediction
# FOR DEBUGGING NOT TRUE OUTPUT
def testModel(testID, color, expected):
    correct = -1
    if (expected in names):
        testVal = np.array([color])
        testVal = tf.keras.utils.normalize(testVal, axis=1)

        pred = model.predict_classes(testVal)
        pred = (names[pred[0]])

        print('---------------------------------')
        print('RGB: ', color)
        print('expected: ', expected)
        print('prediected: ', pred)
        

        if expected == pred:
            correct = 1
        else:
            correct = 0
    else:
        print('---------------------------------')
        print('ERROR - Test #', testID)
        print('expected color not in database of potential predictions')

    return correct

# check the results of the test function
# FOR DEBUGGING NOT TRUE OUTPUT
def checkResults(res):
    correct = 0
    total = 0
    for i in res:
        if i == 1:
            correct += 1
            total += 1
        if i == 0:
            total += 0
        

    print('\n')
    print('===== RESULTS =====')
    print('\n')

    print('correct: ', correct)    
    print('accurancy: ', correct, '/', total)

# function to perform the testing
# place tests in here
def performTests():
    results = []
    print('\n')
    print('===== TESTING =====')
    print('\n')

    # 150, 200, 32
    # green/ yellow
    currTest = [150, 200, 32]
    results.append(testModel(1, currTest, 'green'))

    # 0, 102, 204
    # blue
    currTest = [0, 102, 204]
    results.append(testModel(2, currTest, 'blue'))

    # 204, 0, 255
    # purple
    currTest = [204, 0, 255]
    results.append(testModel(3, currTest, 'purple'))

    # 204, 102, 153
    # purple/red/white
    currTest = [204, 102, 153]
    results.append(testModel(4, currTest, 'purple'))

    # 0, 204, 102
    # green
    currTest = [0, 204, 102]
    results.append(testModel(5, currTest, 'green'))

    # failed test
    currTest = [150, 200, 32]
    results.append(testModel(5, currTest, ' green'))

    checkResults(results)

# predict input values
def prediction(color):
    testVal = np.array([color])
    testVal = tf.keras.utils.normalize(testVal, axis=1)

    pred = model.predict_classes(testVal)

    return pred[0]

#     LOAD PROGRAM     ####################################################


# Reading in Data

filename = 'testingData.txt'

if not os.path.exists(filename):
    file = open(filename, 'w')

    file.write('(255, 255, 255) : 8\n')
    file.close()

file = open(filename, 'r')

# possible classifications
names = ['', 'blue', 'red', 'green', 'yellow', 'purple', 'orange', 'black', 'white']

values = []
labels = []
for line in file:
    value = []
    labels.append(int(line.split(' : ')[1][:-1]))
    RGB = line.split(':')[0][1:-2]
    for i in RGB.split(', '):
        value.append(int(i))
    values.append(value)

data = [values, labels]
file.close()

# hyper parameters
numClassifications = len(names)-1
numEpochs = 100

#     FIT MODEL TO CURRENT DATA SET     ########################################

# set up data from dataset file
x_train = np.array(data[0])
y_train = np.array(data[1])

# normalize 0-255 -> 0-1
x_train = tf.keras.utils.normalize(x_train, axis=1)

# create model
model = tf.keras.models.Sequential()
# try and get rid of flatten, want to see what it does
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(16, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(16, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(numClassifications+1, activation=tf.nn.softmax))

# complile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# fit the model to the dataset
model.fit(x_train, y_train, epochs=numEpochs)

### TESTING OUTPUTS #################################################################

# UNCOMMNENT FOR DEBUGGING OUTPUT
#performTests()

#     SET UP PYGAME SCREEN    #######################################################

pygame.init()
    
gameDisplay = pygame.display.set_mode((progVars.width, progVars.height))
pygame.display.set_caption(progVars.title)

clock = pygame.time.Clock()

# reopen file for pygame to interact with
filename = 'testingData.txt'
file = open(filename, 'a')

#     DRAW PYGAME SCREEN     ######################################################

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

        #    CHECK THE PREDICTION OF THE CURRENT COLOR #####
        colorArray = []
        for color in currColor:
            colorArray.append(color)

        p = prediction(colorArray)
        #print(p)

        #    PLACE A GRAY BOX ON THE COLOR THAT THE COMPUTER THINKS IT IS     #####

        for button in buttons:
            if button.id == str(p):
                rect(button.x+10, button.y+10, button.w-20, button.h-20, colors.darkGray)

        #    CHANGE THE COLOR AND LOG THE USER'S INPUT    ######
        
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

#pyinstaller -w -F colorPicker.py