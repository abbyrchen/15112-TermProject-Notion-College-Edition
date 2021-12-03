##################################################
# Abby Chen
# archen
##################################################

#from CMU 112 Graphics in Tkinter notes:
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html#emptyCanvas
from cmu_112_graphics import *
from datetime import date

#classes that create tasks(recursively or manually by the user) for the weekly agenda

##################################################
#manual task class
##################################################

class ManualTask(object):
    def __init__(self, name, length, day, hourStart):
        self.name = name
        self.length = length
        self.day = day
        self.hourStart = hourStart
    
    def __repr__(self):
        return f'task name: {self.name}, length: {self.length}, day: {self.day}, hourStart: {self.hourStart}'

##################################################
#recursive task class
##################################################

class RecursiveTask(object):
    def __init__(self, name, length, deadlineDay, priority,
                 earliestHour, latestHour):
        self.name = name
        self.length = length
        self.deadlineDay = deadlineDay
        self.priority = priority
        self.earliestHour = earliestHour
        self.latestHour = latestHour
    
    def __repr__(self):
        return f'name: {self.name}, length: {self.length}, deadlineDay: {self.deadlineDay}, priority: {self.priority}, earliest hour: {self.earliestHour}, latest hour: {self.latestHour}'