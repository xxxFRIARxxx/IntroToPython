#Comparisons:

# Equal:		==
# Not Equal:	!=
# Greater Than: >
# Less Than:	<
# Greater or Equal: >=
# Less or Equal:	<=
# Object Identity:  is  #CHECKS TO SEE IF IT'S THE SAME ID IN MEMORY
# ----------------------------------------EXAMPLE--------------------------------
# language = 'Java'

# if language == 'Python':
# 	print('Language is Python')
# elif language == 'Java':
# 	print('Language is Java')
# elif language == 'JavaScript':
# 	print('Language is JavaScript')
# else:
# 	print('No Match')
# ----------------------------------------------------------------------------------
#  Python does NOT have a SWITCH-CASE statement.  This is a way to check multiple values.
#
#  The reason is that IF, ELIF, and ELSE are plenty clear already.
#
#--------------------------AND/OR/NOT:  BOOLEAN OPERATIONS------------------------------
#                       AND needs all criteria.  OR needs only 1
# user = 'Admin'
# logged_in = False

# if user == 'Admin' and logged_in:
# 	print('Admin Page')
# else:
# 	print('Bad Creds')

# OUTPUT:  Bad Creds
#
#---------------------------NOT:  TURNS A TRUE TO A FALSE---------------------------
# user = 'Admin'
# logged_in = False

# if not logged_in:
# 	print('Please log in')
# else:
# 	print('Welcome')
#
#OUTPUT:  Please log in
#
#---------------------------IS:  CHECKING THE ID IN MEMORY-----------------------------
a = [1, 2, 3]
b = [1, 2, 3]

# print(a == b)

# OUTPUT:  True

# print(id(a))
# print(id(b))

# print(a is b)

# OUTPUT:  False, because their ID's in memory don't match.
#
#                     is == 
#               print(id(a) == id(b))
#
# --------------------------------WHAT PYTHON EVALUATES TO FALSE-----------------------------
# 	* False
# 	* None
# 	* Zero of any numeric type   <-----DONT ACCIDENTALLY PASS ALONG A 0, THAT YOU INTERPRET AS FALSE.
# 	* Any empty sequence.  EXAMPLE:  '', (), [].
# 	* Any empty mapping.  EXAMPLE: {}.

# condition = 'Test'
# if condition:
# 	print('Evaluated to True')
# else:
# 	print('Evaluated to False')
