##################################################
# Abby Chen
# archen
##################################################

#from CMU 112 Graphics in Tkinter notes:
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html#emptyCanvas
from cmu_112_graphics import *
from button import Button
from textEditor import Text
from page import Page
from addTask import ManualTask
from addTask import RecursiveTask
from assignment import Assignment

#main program that runs the app. starts in dashboard mode.

##################################################
#dashboard mode
##################################################

def appStarted(app):
    app.mode = 'dashboard'
    app.newPage = Button("+ add new page", [app.width - app.width / 10, 20,
                         app.width - 20, 60], "#aed1b5")
    app.weeklyAgenda = Button("weekly agenda", [50, app.height / 3, 400, 
                                                app.height / 3 + 50], "#aed1b5")
    app.masterToDo = Button("master to-do list", [50, app.height / 3 + 100,
                                                  400, app.height / 3 + 150],
                                                  "#aed1b5")
    app.back = Button("back", [app.width/2 - 70, 
                      app.height - app.height / 6 - 50, 
                      app.width / 2 - 20, 
                      app.height - app.height / 6 - 20], "#aed1b5")
    app.forward = Button("next", [app.width/2 + 50, 
                        app.height - app.height / 6 - 50, 
                        app.width / 2 + 100, 
                        app.height - app.height / 6 - 20], "#aed1b5")
    app.pressed = False
    app.clicks = 0
    app.pageList = [] #keep track of what pages there are
    app.taskLocations = {}
    app.page = Page(app.height, app.width)
    app.backgroundColor = "#f7f7e9"
    app.green = "#bfd9c4"
    app.backToDashboard = Button("back to dashboard", [20, 20, 200, 60], "#aed1b5")
    app.exit = Button('close', [app.width / 6 + 10, 
                                app.height / 6 + 10,
                                app.width / 6 + 150,
                                app.height / 4], "#aed1b5")
    app.listText = Text([50, app.height / 3], 20, 118, 'list')
    app.blankText = Text([50, app.height / 4], 30, 118, 'header')
    app.addTask = Button("add task", [app.width - app.width / 10, 10,
                         app.width - 20, 40], "#aed1b5")
    app.autoAddTask = Button("auto-add task", [app.width - app.width / 10, 60,
                         app.width - 20, 90], "#aed1b5")
    app.deleteTask = Button("delete task", [app.width - app.width / 10, 110,
                         app.width - 20, 140], "#aed1b5")
    app.clearCalendar = Button("clear calendar", [app.width - app.width / 10, 160,
                         app.width - 20, 190], "#aed1b5")
    app.calendar = [[''] * 24 for _ in range(7)]
    app.taskList = [] #list of all tasks on schedule
    app.deleteAssignment = Button("delete assignment", [app.width - app.width / 9, 
                           10, app.width - 20, 50], "#aed1b5")
    app.newAssignment = Button("+ new assignment", [app.width - app.width / 9, 60,
                         app.width - 20, 100], "#aed1b5")
    app.editAssignment = Button("edit assignment", [app.width - app.width / 9, 110,
                         app.width - 20, 150], "#aed1b5")
    app.edit = False
    app.editCourse = Button('edit course', [app.width / 6 + 20, 
                                            app.height / 2 - 100,
                                            app.width / 6 + 300, 
                                            app.height / 2 - 10], "#aed1b5")
    app.editName = Button('edit name', [app.width / 6 + 350, 
                                        app.height / 2 - 100, 
                                        app.width / 6 + 630, 
                                        app.height / 2 - 10], "#aed1b5")
    app.editType = Button('edit type', [app.width / 6 + 680,
                                        app.height / 2 - 100,
                                        app.width / 6 + 960,
                                        app.height / 2 - 10], "#aed1b5")
    app.editStatus = Button('edit status', [app.width / 3 - 35, 
                                            app.height / 2 + 40,
                                            app.width / 3 + 245,
                                            app.height / 2 + 130], "#aed1b5")
    app.editDueDate = Button('edit due date', [app.width / 3 + 290,
                                               app.height / 2 + 40,
                                               app.width / 3 + 570,
                                               app.height / 2 + 130], "#aed1b5")
    app.assignmentList = [] #list of all assignments in to-do list
    #from http://www.stickpng.com/img/comics-and-fantasy/hello-kitty/hello-kitty
    app.image = app.loadImage('hello kitty.png')
    app.image1 = app.scaleImage(app.image, 1/3)
    #from https://sanriopositivity.tumblr.com/post/190065853070
    app.image2 = app.loadImage('quote.png')
    app.image3 = app.scaleImage(app.image2, 1/3)
    #from https://weheartit.com/entry/338897637
    app.image4 = app.loadImage('kuromi.png')
    app.image5 = app.scaleImage(app.image4, 1/6)
    #from https://www.kindpng.com/imgv/ixhixm_transparent-sanrio-png-my-melody-sanrio-png-png/
    app.image6 = app.loadImage('melody.png')
    app.image7 = app.scaleImage(app.image6, 1/5)

def dashboard_mousePressed(app, event):
    #button becomes darker if user presses on it
    if app.newPage.onButton(event):
        app.newPage.buttonColor = "#78967e"
        app.pressed = True
    elif not app.newPage.onButton(event):
            app.newPage.buttonColor = "#aed1b5"
    if app.weeklyAgenda.onButton(event): #switches to weekly agenda page
        app.mode = 'weeklyAgenda'
    elif app.masterToDo.onButton(event): #switches to master to-do list
        app.mode = 'toDo'
    if app.back.onButton(event):
        app.back.buttonColor = "#78967e"
        if app.clicks == 1:
            app.clicks -= 1
    elif not app.back.onButton(event):
        app.back.buttonColor = "#aed1b5"
    if app.forward.onButton(event):
        app.forward.buttonColor = "#78967e"
        if app.clicks < 1:
            app.clicks += 1
    elif not app.forward.onButton(event):
        app.forward.buttonColor = "#aed1b5"
    if app.exit.onButton(event):
        app.pressed = False

def dashboard_keyPressed(app, event):
    if event.key == 'l':
        app.mode = 'list'
    elif event.key == 'b':
        app.mode = 'blank'

def dashboard_redrawAll(app, canvas):
    app.page.drawPage(canvas)
    canvas.create_text(300, app.height / 4, text = "dashboard･ﾟ✧*･ﾟ",
                       font = 'Courier 50 bold')
    app.newPage.drawButton(canvas)
    app.weeklyAgenda.drawButton(canvas)
    app.masterToDo.drawButton(canvas)
    canvas.create_image(app.width / 3 + 80, app.height / 6 + 25, 
                        image = ImageTk.PhotoImage(app.image1))
    canvas.create_image(app.width - 220, app.height - app.height / 4 - 20, 
                        image = ImageTk.PhotoImage(app.image3))
    if app.pressed == True:
        if app.clicks == 0:
            #creates option screen
            canvas.create_rectangle(app.width / 6, 
                                    app.height - app.height / 6, 
                                    app.width - app.width/6, app.height / 6,
                                    fill = "#f7f7e9")
            drawList(app, canvas)
            canvas.create_text(app.width / 2, app.height / 6 + 40,
                                text = "list - press 'l' to select this template", 
                                font = 'Courier 20')
            app.back.drawButton(canvas)
            app.forward.drawButton(canvas)
            app.exit.drawButton(canvas)
        else:
            canvas.create_rectangle(app.width / 6, 
                                    app.height - app.height / 6, 
                                    app.width - app.width/6, app.height / 6,
                                    fill = "#f7f7e9")
            drawBlank(app, canvas)
            app.back.drawButton(canvas)
            app.forward.drawButton(canvas)
            app.exit.drawButton(canvas)
            canvas.create_text(app.width / 2, app.height / 6 + 40,
                                text = "blank - press 'b' to select this template", 
                                font = 'Courier 20')

#draws list template
def drawList(app, canvas):
    canvas.create_rectangle(app.width / 6 + 200,
                               app.height - app.height / 4,
                               app.width - app.width / 6 - 200,
                               app.height / 4)
    canvas.create_rectangle(app.width / 6 + 200, app.height / 4,
                            app.width - app.width / 6 - 200, app.height / 3 + 50,
                            fill = "#bfd9c4")
    canvas.create_text(app.width / 6 + 280, app.height / 3 + 50, text = 'list',
                       font = 'Courier 25 bold')
    canvas.create_text(app.width / 6 + 220, app.height / 3 + 80, text = '-',
                       font = 'Courier 20')

#draws blank page template
def drawBlank(app, canvas):
    canvas.create_rectangle(app.width / 6 + 200,
                               app.height - app.height / 4,
                               app.width - app.width / 6 - 200,
                               app.height / 4)
    canvas.create_rectangle(app.width / 6 + 200, app.height / 4,
                            app.width - app.width / 6 - 200, app.height / 3 + 50,
                            fill = "#bfd9c4")
    canvas.create_text(app.width / 6 + 280, app.height / 3 + 50, text = 'header',
                       font = 'Courier 25 bold')
    canvas.create_text(app.width / 6 + 240, app.height / 3 + 80, text = 'text',
                       font = 'Courier 15')

##################################################
#weekly agenda mode
##################################################

def weeklyAgenda_mousePressed(app, event):
    if app.backToDashboard.onButton(event):
        app.mode = 'dashboard'
    if app.addTask.onButton(event): #manually add task
        app.addTask.buttonColor = "#78967e"
        newTask = createManualTask(app)
        if newTask != None:
            addToCalendar(app, newTask)
    elif not app.addTask.onButton(event):
        app.addTask.buttonColor = "#aed1b5"
    if app.autoAddTask.onButton(event): #computer adds task
        autoTask = createTask(app)
        if autoTask != None:
            createCalendar(app)
        app.autoAddTask.buttonColor = "#78967e"
    elif not app.autoAddTask.onButton(event):
            app.autoAddTask.buttonColor = "#aed1b5"
    if app.deleteTask.onButton(event): #delete requested task
        app.deleteTask.buttonColor = "#78967e"
        deleteTask(app)
    elif not app.deleteTask.onButton(event):
        app.deleteTask.buttonColor = "#aed1b5"
    if app.clearCalendar.onButton(event): #clear whole agenda
        app.clearCalendar.buttonColor = "#78967e"
        clearCalendar(app)
    elif not app.clearCalendar.onButton(event):
        app.clearCalendar.buttonColor = "#aed1b5"
    for task in app.taskLocations:
        checkMousePressed(app, event, task)

#shows the name of the task if the user clicks on it on the agenda
def checkMousePressed(app, event, task):
    x = 75
    y = 290
    width = 58
    height = 60
    day = app.taskLocations[task][0]
    for hour in app.taskLocations[task]:
        xStart = x + width * hour
        xEnd = xStart + width
        yStart = y + height * day
        yEnd = yStart + height
        if xStart <= event.x <= xEnd and yStart <= event.y <= yEnd:
            for i in app.taskList:
                if i.name == task:
                    app.showMessage(f'this task is {i.name}')

#creates manual task object based on user input
def createManualTask(app):
    name = app.getUserInput("enter task name:")
    if name == None: 
        return
    taskLength = app.getUserInput("how long will the task take (in hrs): ")
    if taskLength == None: 
        return
    if validLength(taskLength):
        tLength = int(taskLength)
    else:
        app.showMessage("invalid input! try again :)")
        return
    day = app.getUserInput("day: ")
    if day == None: 
        return
    if validDay(day):
        d = day
    else:
        app.showMessage("invalid input! try again :)")
        pass
    hourStart = app.getUserInput("task time start: ")
    if hourStart == None: 
        return
    if validHour(hourStart):
        hStart = int(hourStart)
    else:
        app.showMessage("invalid input! try again :)")
        return
    task = ManualTask(name, tLength, d, hStart)
    app.taskList.append(task)
    return task

#deletes task based on the name of the task the user enters
def deleteTask(app):
    name = app.getUserInput("name of task to delete:")
    for task in app.taskList:
        if task.name == name:
            app.taskList.remove(task)
            L = findIndex(app.calendar, task.name)
            for i in L:
                index, num = i
                app.calendar[index][num] = ''
            return
    app.showMessage("this task doesn't exist :(")

#returns 2D list of the indices of the value v
def findIndex(L, v):
    res = []
    for row in range(len(L)):
        for i in range(len(L[0])):
            if L[row][i] == v:
                res.append([row, i])
    return res

#checks if a task is valid in the calendar
def isValidCalendar(calendar, row, col, task):
    if type(task) == RecursiveTask:
        if col < task.earliestHour or col > task.latestHour:
            return False
        else:
            if calendar[row][col] == '':
                return True
    else:
        if calendar[row][col] == '':
            return True
    return False

#returns a list of the hours a task takes
def createHourList(length, hourStart):
    result = []
    end = hourStart + length
    for hour in range(hourStart, end):
        result.append(hour)
    return result

#converts the str day into a number from 0-6
def convertToDay(day):
    if day == "Sunday" or day == 'sunday':
        num = 0
    elif day == "Monday" or day == 'monday':
        num = 1
    elif day == "Tuesday" or day == 'tuesday':
        num = 2
    elif day == "Wednesday" or day == 'wednesday':
        num = 3
    elif day == "Thursday" or day == 'thursday':
        num = 4
    elif day == "Friday" or day == 'friday':
        num = 5
    elif day == "Saturday" or day == 'saturday':
        num = 6
    return num

#adds task to calendar destructively
def addToCalendar(app, task):
    day, length, hourStart, name = task.day, task.length, task.hourStart, task.name
    hourList = createHourList(length, hourStart)
    dayNum = convertToDay(day)
    app.taskLocations[task.name] = [dayNum]
    app.taskLocations[task.name].extend(hourList)
    for hour in range(len(app.calendar[dayNum])):
        if ((hour in hourList) and 
            isValidCalendar(app.calendar, dayNum, hour, task)):
            app.calendar[dayNum][hour] = name
        elif not isValidCalendar(app.calendar, dayNum, hour, task):
            app.showMessage('invalid task; try again!')
            return
    return app.calendar

#creates RecursiveTask object based on user input
def createTask(app):
    name = app.getUserInput("enter task name:")
    if name == None: return
    taskLength = app.getUserInput("how long will the task take (in hrs): ")
    if taskLength == None: return
    if validLength(taskLength):
        tLength = int(taskLength)
    else: 
        app.showMessage("invalid input! try again :)")
        return
    deadlineDay = app.getUserInput("deadline day: ")
    if deadlineDay == None: return
    if validDay(deadlineDay):
        dDay = str(deadlineDay)
    else: 
        app.showMessage("invalid input! try again :)")
        return
    priority = app.getUserInput("priority level (1-3): ")
    if priority == None: return
    if validPriority(priority):
        p = int(priority)
    else:
        app.showMessage("invalid input! try again :)")
        return
    earliestHour = app.getUserInput("earliest hour to start task: ")
    if earliestHour == None: return
    if validHour(earliestHour):
        eHour = int(earliestHour)
    else:
        app.showMessage("invalid input! try again :)")
        return
    latestHour = app.getUserInput("latest hour to finish task: ")
    if latestHour == None: return
    if validHour(latestHour):
        lHour = int(latestHour)
    else:
        app.showMessage("invalid input! try again :)")
        return
    task = RecursiveTask(str(name), tLength, dDay, p, eHour, lHour)
    app.taskList.append(task)
    return task

#returns True if n is a valid length in the calendar
def validLength(n):
    if n.isdigit():
        if int(n) <= 24:
            return True
    return False

#returns True if day is a valid day in the week
def validDay(day):
    days = {"sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"}
    if str(day) in days: 
        return True
    return False

#returns True if hr is valid
def validHour(hr):
    if hr.isdigit():
        if 0 <= int(hr) < 24:
            return True
    return False

#returns True if priority is 1-3
def validPriority(p):
    if p.isdigit():
        if 1 <= int(p) <= 3:
            return True
    return False

#returns list of how many days and how many hours to schedule task based on priority
def findLengthOfTime(app, deadlineStrDay, priority):
    now = datetime.datetime.now()
    currDay = convertToDay(now.strftime("%A"))
    deadlineDay = convertToDay(deadlineStrDay) #converts the str to int
    totalDayLength = abs(deadlineDay - currDay) #how many days the user has to do the task
    if totalDayLength == 0:
        app.showMessage('no time for this task!')
        return
    elif totalDayLength <= 2:
        return 1 #must complete the task day of
    elif totalDayLength == 3:
        if priority == 1: return 1
        else: return 2
    if priority == 1:
        totalDayLength = 1
    elif priority == 2:
        totalDayLength = deadlineDay - 2
    elif priority == 3:
        totalDayLength = deadlineDay - 1
    return totalDayLength

#gets the next possible start of a task
def getStart(app, task, row, hour):
    count = 0
    for _ in range(task.length):
        if app.calendar[row][hour] == '':
            count += 1
        hour += 1
    if count == task.length:
        return hour
    return getStart(app, task, row, hour)

#creates best calendar
def createCalendar(app):
    for task in app.taskList:
        if type(task) == RecursiveTask:
            days = findLengthOfTime(app, task.deadlineDay, task.priority)
    return optimalCalendar(app, days, task)

#finds best solution
def optimalCalendar(app, days, task):
    now = datetime.datetime.now()
    currDay = convertToDay(now.strftime("%A"))
    numOfDays = days + currDay - 1
    for hour in range(24):
        if isValidCalendar(app.calendar, numOfDays, hour, task):
            hrList = daySchedule(app, numOfDays, task)
            app.taskLocations[task.name] = [numOfDays]
            app.taskLocations[task.name].extend(hrList)
    return app.calendar

#adds the task into the day
def daySchedule(app, currDay, task):
    hourStart = getStart(app, task, currDay, task.earliestHour)
    hourList = createHourList(task.length, hourStart)
    for hour in range(hourStart, task.latestHour):
        if hour in hourList:
            app.calendar[currDay][hour] = task.name
    return hourList

#draws the day titles to the left of the calendar
def drawDays(app, canvas, x, y):
    for day in range(7):
        days = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
        curr = days[day]
        canvas.create_text(x, y + 60 * day, text = curr, font = 'Courier 18')

#draws hours above calendar
def drawHours(app, canvas, x, y):
    for hour in range(24):
        text = f"{hour}"
        canvas.create_text(x + 58 * hour, y, text = text, font = 'Courier 18')

#draws cells of calendar
def drawCells(app, canvas):
    x = 75
    y = 290
    width = 58
    height = 60
    for day in range(7):
        for hour in range(24):
            xStart = x + width * hour
            xEnd = xStart + width
            yStart = y + height * day
            yEnd = yStart + height
            task = app.calendar[day][hour]
            if task == '':
                boxColor = "#f7f7e9"
            elif checkTaskInList(app, task):
                boxColor = "#bfd9c4"
            else: boxColor = "#f7f7e9"
            canvas.create_rectangle(xStart, yStart, xEnd, yEnd, fill = boxColor)

#checks if task is in calendar
def checkTaskInList(app, task):
    for day in range(len(app.calendar)):
        for hour in range(len(app.calendar[0])):
            if app.calendar[day][hour] == task:
                return True
    return False

#makes calendar empty and removes all tasks from that week
def clearCalendar(app):
    app.calendar = [[''] * 24 for _ in range(7)]
    app.taskList = []

#draws calendar
def drawCalendar(app, canvas):
    drawHours(app, canvas, 108, 270)
    drawDays(app, canvas, 40, 323)
    drawCells(app, canvas)

#draws all buttons in weekly agenda mode
def drawWeeklyAgendaButtons(app, canvas):
    app.backToDashboard.drawButton(canvas)
    app.addTask.drawButton(canvas)
    app.autoAddTask.drawButton(canvas)
    app.deleteTask.drawButton(canvas)
    app.clearCalendar.drawButton(canvas)

def weeklyAgenda_redrawAll(app, canvas):
    app.page.drawPage(canvas)
    drawCalendar(app, canvas)
    canvas.create_text(300, app.height / 4 - 5, text = "weekly agenda",
                       font = 'Courier 50 bold')
    canvas.create_image(app.width / 3 + 85, app.height / 6, 
                        image = ImageTk.PhotoImage(app.image5))
    drawWeeklyAgendaButtons(app, canvas)
    
##################################################
#master to-do list mode
##################################################

def toDo_mousePressed(app, event):
    if app.backToDashboard.onButton(event):
        app.mode = 'dashboard'
    if app.deleteAssignment.onButton(event):
        deleteAssignment(app)
    if app.newAssignment.onButton(event):
        newAssignment(app)
    if app.editAssignment.onButton(event):
        app.edit = True
    #makes screen for choosing what cateogires to edit
    if app.edit == True:
        if app.editCourse.onButton(event):
            current = None
            assignment = app.getUserInput("name of assignment to edit:")
            current = editAssignment(app, assignment)
            if current == None: return
            course = app.getUserInput('edit course name to:')
            current.course = str(course)
        elif app.editName.onButton(event):
            current = None
            assignment = app.getUserInput("name of assignment to edit:")
            current = editAssignment(app, assignment)
            if current == None: return
            name = app.getUserInput('edit assignment name to:')
            current.name = str(name)
        elif app.editType.onButton(event):
            current = None
            assignment = app.getUserInput("name of assignment to edit:")
            current = editAssignment(app, assignment)
            if current == None: return
            aType = app.getUserInput('edit assignment type to:')
            current.type = str(aType)
        elif app.editStatus.onButton(event):
            current = None
            assignment = app.getUserInput("name of assignment to edit:")
            current = editAssignment(app, assignment)
            if current == None: return
            status = app.getUserInput('edit status to (not started, in progress, completed):')
            current.status = str(status)
        elif app.editDueDate.onButton(event):
            current = None
            assignment = app.getUserInput("name of assignment to edit:")
            current = editAssignment(app, assignment)
            if current == None: return
            dueDate = app.getUserInput('edit due date to:')
            current.dueDate = str(dueDate)
    if app.exit.onButton(event):
        app.edit = False

#draws titles of categories above the table
def drawTitles(app, canvas):
    x = 108
    y = 175
    for i in range(5):
        titles = ['course', 'name', 'type', 'status', 'due date']
        title = titles[i]
        canvas.create_text(x + 310 * i, y, text = title, font = 'Courier 20')

#draws the list
def drawTable(app, canvas):
    x = 30
    y = 195
    width = 287
    height = 40
    for n in range(len(app.assignmentList)):
        for title in range(5):
            xStart = x + width * title
            xEnd = xStart + width
            yStart = y + height * n
            yEnd = yStart + height
            canvas.create_rectangle(xStart, yStart, xEnd, yEnd, fill = "#f7f7e9")
            if title == 0:
                canvas.create_text((xStart + xEnd) / 2, (yStart + yEnd) / 2,
                                    text = str(app.assignmentList[n].course),
                                    font = 'Courier 15')
            elif title == 1:
                canvas.create_text((xStart + xEnd) / 2, (yStart + yEnd) / 2,
                                    text = str(app.assignmentList[n].name),
                                    font = 'Courier 15')
            elif title == 2:
                canvas.create_text((xStart + xEnd) / 2, (yStart + yEnd) / 2,
                                    text = str(app.assignmentList[n].assignmentType),
                                    font = 'Courier 15')
            elif title == 3:
                canvas.create_text((xStart + xEnd) / 2, (yStart + yEnd) / 2,
                                    text = str(app.assignmentList[n].status),
                                    font = 'Courier 15')
            elif title == 4:
                canvas.create_text((xStart + xEnd) / 2, (yStart + yEnd) / 2,
                                    text = str(app.assignmentList[n].dueDate),
                                    font = 'Courier 15')

#deletes assignment requested
def deleteAssignment(app):
    name = app.getUserInput("name of assignment to delete:")
    for assignment in app.assignmentList:
        if assignment.name == name:
            app.assignmentList.remove(assignment)

#gets user input for new assignment
def newAssignment(app):
    course = app.getUserInput("course title:")
    name = app.getUserInput("name of assignment: ")
    assignmentType = app.getUserInput("type of assignment (quiz, lab, etc.):")
    status = app.getUserInput("status (incomplete, in progress, completed)")
    dueDate = app.getUserInput("due date:")
    assign = Assignment(str(course), str(name), str(assignmentType), 
                        str(status), str(dueDate))
    app.assignmentList.append(assign)
    return assign

#finds assignment that the user wants to edit
def editAssignment(app, name):
    for assignment in app.assignmentList:
        if assignment.name == name:
            app.edit = True
            return assignment
    app.showMessage("this assignment does not exist :(")

def toDo_redrawAll(app, canvas):
    canvas.create_rectangle(0, app.height, app.width, 0, 
                            fill = "#f7f7e9")
    canvas.create_text(300, app.height / 7, text = "master to-do list",
                       font = 'Courier 50 bold')
    app.deleteAssignment.drawButton(canvas)
    app.editAssignment.drawButton(canvas)
    drawTitles(app, canvas)
    drawTable(app, canvas)
    canvas.create_image(app.width / 3 + 150, app.height / 7 - 30, 
                        image = ImageTk.PhotoImage(app.image7))
    app.newAssignment.drawButton(canvas)
    app.backToDashboard.drawButton(canvas)
    if app.edit == True:
        canvas.create_rectangle(app.width / 6, 
                                    app.height - app.height / 6, 
                                    app.width - app.width/6, app.height / 6,
                                    fill = "#f7f7e9")
        app.exit.drawButton(canvas)
        app.editCourse.drawButton(canvas)
        app.editName.drawButton(canvas)
        app.editType.drawButton(canvas)
        app.editStatus.drawButton(canvas)
        app.editDueDate.drawButton(canvas)

##################################################
#list mode
##################################################

def list_mousePressed(app, event):
    if app.backToDashboard.onButton(event):
        app.mode = 'dashboard'

def list_keyPressed(app, event):
    app.listText.typing(event)

def list_redrawAll(app, canvas):
    app.page.drawPage(canvas)
    canvas.create_text(300, app.height / 4, text = "list",
                       font = 'Courier 50 bold')
    app.backToDashboard.drawButton(canvas)
    app.listText.drawText(canvas)

##################################################
#blank mode
##################################################

def blank_mousePressed(app, event):
    if app.backToDashboard.onButton(event):
        app.mode = 'dashboard'

def blank_keyPressed(app, event):
    app.blankText.typing(event)

def blank_redrawAll(app, canvas):
    app.page.drawPage(canvas)
    app.backToDashboard.drawButton(canvas)
    app.blankText.drawText(canvas)

runApp(width = 1500, height = 800)