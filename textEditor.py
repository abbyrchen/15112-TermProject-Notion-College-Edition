##################################################
# Abby Chen
# archen
##################################################

#from CMU 112 Graphics in Tkinter notes:
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html#emptyCanvas
from cmu_112_graphics import *

#text class that creates a text editor object

##################################################
#text class
##################################################

class Text(object):
    def __init__(self, location, maxLines, maxLineLength, type):
        self.input = ''
        self.type = type #list or normal
        self.location = location #where the user starts typing
        self.maxLines = maxLines
        self.maxLineLength = maxLineLength
        self.lineLength = 0
        self.firstLine = True
        self.lineNum = 0
        self.masterList = [['' for j in range(1)] for i in range(maxLines)]
        self.charList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d',
                   'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
                   't','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
                   'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
                   'X','Y','Z','!','"','#','$','%','&','(',')','*','+',',','-',
                   '.','/',':',';','<','=','>','?','@','[',']','^','_','{','}',
                   '`','|','\'']
        self.isHeader = False
                   
    def typing(self, event):
        bulletIndex = self.charList.index("-")
        bullet = self.charList[bulletIndex]
        if self.firstLine: 
            if self.type == 'header':
                self.isHeader = True
            x, y = self.location
            self.location = [x, y]
            if self.type == 'list': #and len(self.masterList[self.lineNum]) == 1:
                self.masterList[self.lineNum].append([bullet])
        self.firstLine = False #user started typing (increment location)
        if event.key in self.charList: 
            if not self.lineLength >= self.maxLineLength:
                charIndex = self.charList.index(event.key)
                value = self.charList[charIndex]
                #appends regular text
                self.masterList[self.lineNum].append([value]) #starts the row
                self.lineLength += 1
            else:
                self.lineNum += 1
                #restart new line
                self.lineLength = 0
                charIndex = self.charList.index(event.key)
                value = self.charList[charIndex]
                self.masterList[self.lineNum].append([value])
                self.lineLength += 1
        elif event.key == 'Space':
            self.masterList[self.lineNum].append(' ')
            if not self.lineLength >= self.maxLineLength:
                self.masterList[self.lineNum].append(' ')
                self.lineLength += 1
            else: #past max line length
                self.lineNum += 1 
                self.masterList[self.lineNum].append(' ')
                self.lineLength += 1
        elif event.key == 'BackSpace': 
            if self.masterList[0] == ['']:
                self.firstLine = True #restarts the line
                if self.type == 'header':
                    self.isHeader = True
                self.lineNum = 0
                self.lineLength = 0
                #line is gone so move to the one before
            elif ((self.masterList[self.lineNum] == [''] or 
                 self.masterList[self.lineNum] == ['-']) and self.lineNum != 0):
                self.lineNum -= 1
            else:
                self.lineLength -= 1
                #delete the last letter/element
                self.masterList[self.lineNum].pop()
        elif event.key == 'Return':
            self.lineNum += 1
            if self.type == 'list':
                if self.lineNum < self.maxLines:
                    self.masterList[self.lineNum].append([bullet])
                    self.lineLength = 1
            self.lineLength = 1
            if self.type == 'header' and not self.firstLine:
                self.isHeader = False
        elif event.key == 'Tab':
            self.masterList[self.lineNum].append(' ' * 4)
            self.lineLength += 4
    
    def drawText(self, canvas):
        dx, dy = 0, 0
        xLocation = self.location[0]
        yLocation = self.location[1]
        for line in range(len(self.masterList)):
            if line == 0 and self.type == 'header':
                self.isHeader = True
                textFont = 'Courier 50 bold'
            else: 
                textFont = 'Courier 18'
            for letter in self.masterList[line]:
                canvas.create_text(xLocation + dx, yLocation + dy,
                                text = letter, font = textFont)
                if letter == ' ':
                    dx += 5
                elif textFont == 'Courier 50 bold':
                    dx += 28
                else: dx += 12
            if textFont == 'Courier 50 bold': dy += 20
            dy += 25
            dx = 0