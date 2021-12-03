##################################################
# Abby Chen
# archen
##################################################

#from CMU 112 Graphics in Tkinter notes:
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html#emptyCanvas
from cmu_112_graphics import *
import random

#assignment class that creates assignment object used in to do mode for master to-do list

##################################################
#assignment class
##################################################

class Assignment(object):
    def __init__(self, course, name, assignmentType, status, dueDate):
        self.course = course
        self.colors = ['#FFB0B0', '#FFD8B0', '#FFFFB0', '#DBF6CD', '#CDF6E8',
                       '#CDEFF6', '#CDDBF6', '#D3CDF6', '#FEDDF8', '#DACBB0']
        self.courseColor = self.colors[random.randint(0,9)]
        self.name = name
        self.assignmentType = assignmentType
        self.status = status
        self.dueDate = dueDate
    
    def __repr__(self):
        return f'course: {self.course}, color: {self.courseColor}, name: {self.name}, type: {self.assignmentType}, status: {self.status}, due date: {self.dueDate}'