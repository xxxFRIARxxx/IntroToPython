#-------------------------------------------------FUNCTIONS-------------------------------------------------

import webbrowser
import os

# webbrowser.open("https://www.youtube.com/watch?v=9Os0o3wzS_I")

#-----------------------------------PASS:  NO ERRORS FOR A BLANK FUNCTION-----------------------------------

# def hello_func():
# 	pass  # allows to fill in this function later.  Will not throw errors for leaving it blank.

# print(hello_func())

#OUTPUT:  None

#def hello_func():
#	print('Hello Function!')

# hello_func()
# hello_func()
# hello_func()
# hello_func()

#  Functions are basically a machine to concatanate things into one location, to be updated easily.  KEEP YOUR CODE DRY.
#                    MAKE YOUR CODE EASY TO UPDATE, UNLESS YOU VALUE YOUR JOB SECURITY

#--------------------------------------RETURN:  WHEN RECALLING FOR LATER-------------------------------------

#def hello_func():
#	return 'Hello Function!'  #return allows us to recall data, and pass along the result to whatever called our function.

#---------------------------TREAT AN EXECUTED FUNCTION LIKE A STRING/INT/LIST...ETC---------------------------

#  You can treat the return value exactly like the data type it is.  String, intiger, list...etc...
#print(hello_func().upper())

#-------------------------------------PASSING ARGUMENTS TO OUR FUNCTION---------------------------------------

# def hello_func(greeting):
#  	return '{} Function.'.format(greeting)
# print(hello_func('Hi'))

# Passes in 'Hi' into our function, with the 'greeting' variable equal to the string 'Hi', then returned:
# Hi Function.

# ---------------------------------------MULTVARIABLE ARGUMENTS-------------------------------------

# def hello_func(greeting, name = 'You'):  #make it so if no value is in, it returns You.
# 	return '{}, {}'.format(greeting, name)


# ARGS NEEDS TO COME BEFORE KWARGS (Functional arguments (greeting) need to come before keyword argument (name))


# print(hello_func('Hi', name = 'Tom'))


#-----------------------ARGS/KWARGS, POSITIONAL RELATIONS IN TUPLES AND DICTIONARIES-------------------
# def student_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)

# student_info('Math', 'Art', name='John', age=22)

#  This prints a TUPLE of all of our POSITIONAL arguments (args), and a DICTIONARY of all
#  of our KEYWORD arguments (kwargs)

#--------------------------------UNPACKING ARGS AND KWARGS INTO A FUNCTION------------------------------

#STARS OR DOUBLE STARS UNPACK A SEQUENCE OR A DICTIONARY, AND PASS THEM TO THE FUNCTION INDVIDUALLY 

# def student_info(*args, **kwargs): #<----if the stars are here, for accepting an arbitrary nunber
#                                          of positional keywords or values.
# 	print(args)
# 	print(kwargs)

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

# student_info(*courses, **info)  # <---Equivilant to previous execution. Unpacks the values.

# *args = key values from our list we've unpacked 
# **kwargs = dictionary values we've unpacked

#-----------------------------------HOW MANY DAYS ARE IN A MONTH EXAMPLE---------------------------------

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
# 	"""Return True for Leap Years.  False for Non Leap."""

# 	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year, month):
# 	"""Return # of days in that month in that year"""

# 	if not 1 <= month <= 12:
# 		return 'Invalid Month'

# 	if month == 2 and is_leap(year):
# 		return 29

# 	return month_days[month]  #  NOTICE THE MOTHFUCKING BRACKETS BLOWING MY MIND.
# 	                          #  PARENTHETESIS DOESNT WORK.  


# print(days_in_month(2017, 2))

