import webbrowser
import os

# webbrowser.open("https://www.youtube.com/watch?v=daefaLgNkw0") #<--- open to follow along

#-----------------------------LESSON 5: DICTIOINARIES AND KEY-VALUE PAIRS----------------------------------

# Dictioniaries, aka HASH MAPS, or ASSOCIATIVE ARRAYS, allow us to work with key-value pairs.
# These are two linked values, where the key is the unique identifier to the data, and the value IS that data.
# In a physical dictionary example, each physical word would be the key, and each definition would be the value.

# REMEMBER TO USE CURLEY BRACES FOR A DICTIONARY

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#print(student['name'])
#print(student['courses'])


#  This would show you the value of the 'name' key in the dictionary above, which outputs to 'John'.
#  As shown above, dictionaries can hold just about anything:  
#  Our name is a string, the age is an integer, and the courses is a list.

#  Keys too can be any IMMUTABLE data type.  Example:  Instead of 'name', you could use the integer 1:

#student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#print(student[1]) would still output John.

#  ---------------------RETURNING NONE INSTEAD OF AN ERROR ON A NON-EXISTING KEY--------------

#print(student['phone']) # <---- Errors out due to the key not existing

#  Use the built-in .get METHOD:

#print(student.get('phone'))
# OUTPUT:  'None'

#  You can also supply a default value for KEYS THAT DON'T EXIST with a SECOND ARGUMENT to the GET METHOD:

#print(student.get('phone', 'Not Available'))
# OUTPUT:  'Not Available'

# --------------------------ADDING ENTRIES THAT DONT EXIST IN THE DICTIONARY-------------------------

#       v       V    NOTE THE BRACKETS
#student['phone'] = '555-5555'
#print(student.get('phone', 'Not Available'))  #OUTPUT:  555-5555

#-----------------------------UPDATING ENTRIES THAT ALREADY EXIST---------------------------------

#student['name'] = 'Jane'
#print(student)

#  You can also update values using the .UPDATE METHOD.  Useful for UPDATING MULTIPLE VALUES at a time.

#student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
#print(student)

#OUTPUTS: {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}  Updates all 3 at once.


# --------------------------------------REMOVING A KEYWORD-------------------------------------------

#  Say we want to delete a specific key and it's value.  Use the del KEYWORD:

#del student['age']
#print(student)

#OUTPUT:  Deletes the student's age.

#----------------------------REMOVING A KEYWORD WITH THE POP METHOD-------------------------------------

#                   Reminder:  The .pop METHOD retains the information!

# age = student.pop('age')
# print(age)
# print(student)

# OUTPUT:  25
#{'name': 'John', 'courses': ['Math', 'CompSci']}

#------------------------LOOPING THROUGH KEYS AND VALUES IN THE DICTIONARY---------------------------

# To see how many keys are in the dictionary, just use the LENGTH function:
#print(len(student))

# To see the NAMES of the keys, use the .KEYS method:
#print(student.keys())

# To see the VALUES of the kyes, use the .VALUES method:
#print(student.values())

# To see the keys AND the values, use the .ITEMS method:
#print(student.items(())

#----------------------------------FOR LOOPS THROUGH DICTIONARIES------------------------

#  If you try to use a for loop through a dictionary, it'll just give you the KEYS:

#for value in student:
#	print(value)

# OUTPUTS:  name
# age
# courses

#  Instead, you have to use the .ITEMS METHOD we just saw above:

#for key, value in student.items():
#	print(key, value)

# You need to access the 'key' as well, because the .items METHOD comes in a PAIR of 2 values!
