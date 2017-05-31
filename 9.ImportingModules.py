#----------------------------------------IMPORTING MODULES--------------------------------------------

import my_module
# ^ This imports the 'my_module' module also supplied.  Put 'my_module.py' in the same folder as this file.

#------------------------------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']

# Say we want to use the 'find_index' function from 'my_module':

index = my_module.find_index(courses, 'Math')
#print(index)

#---------------------------------SHORTCUTTING NAMES TO MODULES: AS--------------------------------------
# Typing in my_module.find_index is a pain in the ass, so you can type:

#import my_module as mm

# So now you can just type "mm.find_index..." instead because we've abbreviated it

#--------------------------------ONLY IMPORTING THE FUNCTION:  FROM--------------------------------------

# From my_module import find_index  <--- as line 1 of this code
# Only gives access to the find_index function.  Nothing else

#from my_module import find_index, test
#print(test)
# The code above shows that you can print the test variable from my_module.py

# FROWNED UPON, but to import everything:  from my_module import *
# The reason it's frowned upon is because you can't track down what's imported

#--------------------------------FINDING MODULES IN DIFFERENT FILE PATHS---------------------------------

import sys
#print(sys.path)
# In the list printed above:

# First listed is the current directory of the script we're running
# Second is the Python Path Environment Variable. 
# Third is the Standard Library Directories
# Last is the Site Packages Directory for 3rd party packages

#--------------------IMPORTING A MODULE NOT IN A SET PATH: .APPEND, OR MANUAL EDIT-----------------------

# 1:  You can add the directory to sys.path

#sys.path.append('Users\Anon\Desktop\Python Scripts')  <-- Would add my 'Desktop\\Python Scripts' folder to the path

# 2:  You can add it to the Python Path Environment Variable
#  ctrl+break
#  Advanced system settings
#  Environment variables at the bottom
#  Click new
#  Name it "Python Path"
#  Location:  C:\Users\Anon\Desktop\IntroToPython

# 3:  You can find out how Sublime Texts Python Path Variables are set, and set those

#--------------------------------USING THE STANDARD LIBRARY FOR PYTHON-----------------------------------

# Say we want to grab a random value from a list of values.  We could make it, or 
# use it from the standard library
import random

#random_course = random.choice(courses)
#print(random_course)

# ---------------------------OTHER USEFUL MODULES TO IMPORT FROM STANDARD LIB-----------------------------

# Math imports
import math

#rads = math.radians(90)
#print(math.sin(rads))

import datetime
import calendar

# Datetime and calendar are very similar, but have different functionalities:

today = datetime.date.today()
#print(today)

#print(calendar.isleap(2017))

#----------------------------------------THE MOTHERFUCKING OS MODULE---------------------------------------


# THE MOTHERFUCKING OS MODULE - Gives us access to the underlying OS
# Scan the file system, modify files, move, delete, rename files...
import os

#print(os.getcwd())

# ^^^prints current working directory, 

# These modules are python files themselves!  We can view the location
# by printing out it's dunder-file attribute
# DUNDER FILES ARE DOUBLE UNDERSCORES

print(os.__file__)

# ^^^print out the location of this file on our filesystem
# if we open up the diriectory above on our system, we can see the
# ENTIRE STANDARD LIBRARY

#print(dir(os))  

#print(help(os))
