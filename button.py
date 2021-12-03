##################################################
# Abby Chen
# archen
##################################################

#from CMU 112 Graphics in Tkinter notes:
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html#emptyCanvas
from cmu_112_graphics import *

#class that creates a button object that can be pressed

##################################################
#button class
##################################################

class Button(object):
    def __init__(self, title, location, color):
        self.title = title
        self.location = location
        self.buttonColor = color
        self.textColor = 'black'
        self.buttonFont = 'Courier 14'
    
    #checks if cursor clicks on button
    def onButton(self, event):
        if (self.location[0] <= event.x < self.location[2] and
            self.location[1] <= event.y < self.location[3]):
            return True
        else:
            return False
    
    #draws the Button object
    def drawButton(self, canvas):
        canvas.create_rectangle(self.location[0], self.location[1],
                                self.location[2], self.location[3],
                                fill = self.buttonColor, 
                                outline = self.textColor)
        canvas.create_text(self.location[0] +
                          (self.location[2] - self.location[0]) / 2,
                          self.location[1] + 
                          (self.location[3] - self.location[1]) / 2,
                          text = self.title, font = 'Courier 14',
                          fill = self.textColor)