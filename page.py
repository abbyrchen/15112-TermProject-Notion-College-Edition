##################################################
# Abby Chen
# archen
##################################################

#from CMU 112 Graphics in Tkinter notes:
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html#emptyCanvas
from cmu_112_graphics import *

#basic template of pages

##################################################
#page class
##################################################

class Page(object):
    def __init__(self, height, width):
        self.pageBackground = "#f7f7e9"
        self.color = "#bfd9c4"
        self.outline = "#f7f7e9"
        self.height = height
        self.width = width
    
    def drawPage(self, canvas):
        canvas.create_rectangle(0, self.height, self.width, 0, 
                                fill = self.pageBackground)
        canvas.create_rectangle(0, self.height / 4, self.width, 0, 
                                fill = self.color, outline = self.outline)