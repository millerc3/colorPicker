# Color Identifier

Using python, tensorflow/keras, and pygame, this color identifier will generate random colors for the user to decide what base color that it is and begin to learn to identify the randomly generated colors.

The machine learning algoritm used is a convolutional neural network that will continue to train itself as the user inputs more predictions.  Each time that the program is loaded, the model will fit to the current available data and attempt to classify the given color to the best of its abilities.

As the program is ran more times, the model will become better at identifying the colors shown to the user.  Restart the program to refit the model to the new dataset.  

## Getting Started

Python Version: 3.6.7
3rd Party libraries:
*  numpy
*  tensorflow/keras
*  pygame

Feel free to download the script and run it in the command line: python3 colorPicker.py, or download the zip file and run the executable "colorPicker.exe"

link to executable:
https://www.dropbox.com/s/ormyot2e731eac9/colorPicker.zip?dl=0

## Running the program

Upon running the program, a pygame window will open with the current random color to be classified.  On first run, the program will be unable to identify any colors other than white.  Click the colored buttons under the color window to teach the computer how to classify the colors.  Once the user has supplied the program with sufficient learning material, they can close the program and restart it.  The program will re-fit the new data to better classify the colors.

The computer identifies which class that it thinks the given color is by the gray rectangle on top of one of the buttons.

## Acknowledgments

This program is based on the tensorflow.js tutorial program by "The Coding Train" who created a similar project using javascript and processing.js

I had seen the YouTube playlist of him doing his project a few months ago and decided to attempt the project using tensorflow and pygame in python.  I did not consult his videos for help or advice, as I wanted to see what I could come up with on my own.  I simply used his general idea of a color classifier.

