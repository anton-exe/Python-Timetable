#! /usr/bin/python

from math import ceil, floor
from random import choice
# import time

# Class class (confusing right?)
class Class():
    def __init__(self, subject, teacher, room):
        self.subject   = subject
        self.teacher   = teacher
        self.room      = room
        self.colorcode = choice((31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97)) # Pick a random color for the text

# All Classes
maths       = Class("Maths",       "Mr. ______",     "B1-30")
english     = Class("English",     "Ms. ________",   "B1-24")
irish       = Class("Irish",       "Ms. __________", "B1-30")
german      = Class("German",      "Mr. ____",       "B1-24")
science     = Class("Science",     "Mr. ______",     "B1-24")
geography   = Class("Geography",   "Mr. _______",    "B1-24")
history     = Class("History",     "Ms. ______",     "B1-24")
phys_ed     = Class("PE",          "Mr. _______",    "B1-Court")
graphics    = Class("Graphics",    "Mr. _______",    "B3-??")
wood_tech   = Class("Woodwork",    "Mr. _______",    "B1-WW")
religion    = Class("Religion",    "",               "B1-24")
sphe        = Class("SPHE",        "",               "B1-24")
cspe        = Class("CSPE",        "Mr. ______",     "B1-24")
life_skills = Class("Life Skills", "",               "B1-24")
tenminbreak = Class("Break",       "",               "")
lunch       = Class("Lunch",       "",               "")
end         = Class("Home Time",   "",               "")
null        = Class("",            "",               "")
null.colorcode = 97

# Timetable class
class Timetable():
    def __init__(self, times, classes):
        self.times = times
        self.classes = classes
    
    # The function to print the table
    def drawTable(self):
        print("\033[0m┌───────────────┬───────────────┬───────────────┬───────────────┬───────────────┬───────────────┐")
        print("│     Time      │    Monday     │    Tuesday    │   Wednesday   │   Thursday    │    Friday     │")
        for i in range(len(self.times)): # For every time row
            print("├───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼───────────────┤") # Top-divider

            output = "│" + 15 * " " + "│"
            # Subject Name
            for classslot in self.classes[i]:
                length = float(len(classslot.subject))
                text = f"\033[0;{classslot.colorcode}m" + (floor((15 - length) / 2) * " ") + classslot.subject + (ceil((15 - length) / 2) * " ") + f"\033[0m"
                output = output + text + "│" # Right Divider
            print(output)
            
            output = "│     " + self.times[i] + "     │"
            # Teacher Name
            for classslot in self.classes[i]:
                length = float(len(classslot.teacher))
                text = f"\033[0;{classslot.colorcode}m" + (floor((15 - length) / 2) * " ") + classslot.teacher + (ceil((15 - length) / 2) * " ") + f"\033[0m"
                output = output + text + "│" # Right Divider
            print(output)
            
            output = "│" + 15 * " " + "│"
            # Room Number
            for classslot in self.classes[i]:
                length = float(len(classslot.room))
                text = f"\033[0;{classslot.colorcode}m" + (floor((15 - length) / 2) * " ") + classslot.room + (ceil((15 - length) / 2) * " ") + f"\033[0m"
                output = output + text + "│" # Right Divider
            print(output)
        print("└───────────────┴───────────────┴───────────────┴───────────────┴───────────────┴───────────────┘")

# The time every segment starts
times = ("08:50", "09:30", "10:10", "10:20", "11:00", "11:40", "12:20", "13:00", "13:30", "14:10", "14:50", "15:30")

# 2D Tuple of classes which acts as the timetable layout
classes = (
    (science, english, science, english, wood_tech),
    (irish, german, cspe, life_skills, wood_tech),
    (tenminbreak, tenminbreak, tenminbreak, tenminbreak, tenminbreak),
    (maths, history, english, history, irish),
    (english, maths, irish, geography, english),
    (phys_ed, german, history, graphics, maths),
    (phys_ed, irish, wood_tech, graphics, graphics),
    (lunch, lunch, lunch, lunch, end),
    (geography, science, geography, german, null),
    (german, science, sphe, irish, null),
    (graphics, religion, wood_tech, maths, null),
    (end, end, end, end, null)
)

TimeTable = Timetable(times, classes)
TimeTable.drawTable()
