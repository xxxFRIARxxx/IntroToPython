courses = ["History", "Math", "Physics", "CompSci"]  #  NOTE THE SQUARE BRACKETS.  THESE ARE LISTS.  MODIFYABLE.
courses_2 = ["History", "Math", "Art", "Design"]   #  NOTE THE SQUARE BRACKETS.  THESE ARE LISTS.  MODIFYABLE.
nums = [1, 5, 2, 4, 3]

#  [] = List -		Modifyable
#  () = Tuple -		NOT Modifyable
#  {} = Set -		Unordered, and HAVE NO DUPLICATES

#  To find the first value of the 'courses' list above, you'd enter:  
# print(courses[0])

#  Negative indexes [-1] start from the end of the list.  (CompSci, in this example)
#  A range of values can be found with:  print(courses[0:2]).   FIRST INDEX IS INCLUSIVE, LAST IS EXCLUSIVE.
#  You can also leave the 0 off of the [0:2].  

#  ---------------------SECTION 3A:  SLICING VALUES FROM LISTS/SETS/TUPLES-----------------

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

#         SYNTAX =   list[start:end:step]

# EXAMPLES:		In the list above, if you want 0-5, you'd put [0:6]
#				If you want 3-7, you could do [-7:-2].  Or you can mix and match:  [3:-2]

# WHAT IS A STEP? ("C", in [A:B:C]):	The amount it "steps over" to count:
#
# EXAMPLE: 		print(my_list[2:-1:2]) would show:  [2, 4, 6, 8] because it's counting from 2-8, stepping by 2.
#
# ---------------------------------ITERIATING BACKWARDS THROUGH LISTS--------------------

# Start from the negative and go to the positive, USING A NEGATIVE STEP.
#  EXAMPLES:
#print(my_list[-1:0:-1])  This would print 9 through 1, in reverse.
#print(my_list[::-1])     This would print the entire list, in reverse.


# NOTE:						The end index is exclusive, EVEN WHEN GOING IN REVERSE!


# ----------------------SECTION 3B:  SLICING STRINGS FROM LISTS/SETS/TUPLES-------------------------

sample_url = 'http://google.com'

# EXERCISE 1:  Reverse the url:
# print(sample_url[::-1])

# EXERCISE 2:  Get the top-level domain only (.com)
# print(sample_url[-4:])

# EXERCISE 3:  Print URL w/o the http://
# print(sample_url[7:])

# EXERCISE 4:  Print url w/o the http:// or the domain.
# print(sample_url[7:-4])
#
#-------------------------------------------------------------------------------------------------
#                                  BACK TO LISTS, TUPLES, AND SETS
#
# Refer back to "courses", and "courses_2" up top.
#
#-------------------------APPEND, INSERT, AND EXTEND: ADDING THINGS TO LISTS-----------------------


#                        APPEND AND INSERT DO NOT NEST MULTIPLE VALUES PROPERLY
#                    *****EXTEND NESTS PROPERLY, STILL REPEATS DUPLICATES THO*****


# HOW TO ADD SOMETHING TO THE END OF A LIST:   .append
# courses.append('Gym')

# HOW TO ADD SOMETHING TO A SPECIFIC LOCATION IN A LIST:   .insert
# courses.insert(0, 'Gym')

# HOW TO ADD MULTIPLE VALUES TO A LIST THAT *NESTS PROPERLY*:  .extend
#courses.extend(courses_2)

#courses.insert(0, courses_2)
#print(courses)
#
#------------------------------REMOVE AND POP:  REMOVING THINGS FROM LISTS---------------------------

#  .remove
#  courses.remove('Math')  would remove 'Math' from the 'courses list', duh.

#  HOW TO REMOVE FROM THE END OF A LIST AS IF IN A STACK OR QUEUE.  RETURNABLE VALUES:
#  .pop
   
#popped = courses.pop()
#courses.pop() #would remove 'CompSci' from the 'courses' list, but ALLOWS IT TO BE A RETURNED VALUE.

#print(popped)
#print(courses)   #copy-paste all 3 lines from 89-91 to see an example

#----------------------------------SORTING LISTS: ALTERING THE ORIGINAL--------------------------------


# IN REVERSE:  .reverse
#courses.reverse()

# SORTING YOUR LIST:  .sort
#courses.sort()   sorts in alphabetical order, numbers in ascending.
#nums.sort()      ascending (numbers)

# SORTING YOUR LIST, DESCENDING: 
# Yes, you can use the .reverse method on the list when they're sorted, but EASEIER:
# THERES A REVERSE ARGUMENT TO THE SORT METHOD:
#courses.sort(reverse=True)
#nums.sort(reverse=True)

#------------------HOW TO SORT A LIST, WITHOUT ALTERING THE ORIGINAL:  sorted() function-----------------

#sorted(courses)  

#  returns a sorted version of the list in place.  To get the sorted list, you need to get a new variable
#  and set it to the return value of the function, up top, like this:

#sorted_courses = sorted(courses)
#print(sorted_courses)

#--------------------------------MIN, MAX, AND SUM---------------------------------

#  If you want the minimum value of the numbers list way up top:  MIN
#print(min(nums))

#  If you want the maximum value of the list:  MAX
#print(max(nums))

#  If you want the sum of the list:  SUM
#print(sum(nums))

#--------------------------------FINDING THE INDEX OF A VALUE--------------------------------

#  Finds the index number of a value in the list.  
#print(courses.index('CompSci'))

#  If you try to search for a value that isn't in the list, you'll receive a VALUE ERROR.
#  TRUE OR FALSE OPERATORS if something is in a list or not:  use the IN operator:

#print('Art' in courses)  returns FALSE
#print('Math' in courses) returns TRUE

#-----------------------------------BRIEF INTRO TO FOR LOOPS---------------------------------

for ABCDEF1234 in courses:
	print(ABCDEF1234)
#  
#------------------------------FINDING THE INDEX NUMBER ALSO---------------------------------

#  USE THE ENUMERATE FUNCTION.  ENUMERATE RETURNS 2 VALUES:  THE INDEX AND THE VALUE.

# for index, course in enumerate(courses):
# 	print(index, course)   

# RETURNS:  
# 0 History
# 1 Math
# 2 Physics
# 3 CompSci
#-------------------------WHAT IF YOU DONT WANT TO START ON 0?------------------------------

# for index, course in enumerate(courses, start=1):
# 	print(index, course)

# Starts list on 1.  Uses the START ARGUMENT.

#--------------------------HOW TO TURN LISTS INTO A STRING-------------------------------

  
#                     CSV, or HYPEN SEPARATED VALUES
#  We're going to use .JOIN METHOD to join the values of this list in the string.

course_str = ' - '.join(courses)  
#print(course_str)

#--------------------------HOW TO TURN STRINGS INTO A LIST-------------------------------


new_list = course_str.split(' - ')
#print(course_str)
#print(new_list)    #TURNS IT BACK INTO THE ORIGINAL LIST.  HOLY FUCK.  I GET IT NOW.

#------------------------------------TUPLES--------------------------------------------------

#  TUPLES ARE IMMUTABLE.  THEY ARE *NOT* MODIFYABLE

#  Take the following lists as example:
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

#print(list_1)
#print(list_2)

# Obviously, list 1 and 2 have the same values.

# But if we change a value in list 1, it changes them both.  This is good if you're changing lists together:
list_1[0] = 'Art'

#print(list_1)
#print(list_2)

#-------------------------------------------TUPLE EXAMPLE-----------------------------------------------

#  If you want a list of values that you know will NOT CHANGE, use a TUPLE:
tuple_1 = ('History', 'Math', 'Physics', 'CompScience')  
#NOTE THE ^PARENTHESIS INSTEAD OF THE BRACKETS FOR THE^ ARRAY ABOVE
tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# #tuple_1[0] = 'Art'  #IF YOU CHANGE IT, LIKE UNCOMMENTING THIS LINE, YOU'LL RECEIVE AN ERROR.
# print(tuple_1)
# print(tuple_2)

# -------------------------------SETS AND HOW TO COMPARE THEM---------------------------------------

# SETS are values that are UNORDERED and HAVE NO DUPLICATES
# If you continually run this below, the order can change with each execution.  SETS do NOT care about ORDER.
# SETS test if VALUES are PART OF A SET.  SETS ALSO DISCARD DUPLICATES.

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}
# NOTE THE    ^ DUPLICATE MATH, AND CURLEY BRACES INSTEAD OF OTHERWISE

#print(cs_courses)
#This will NOT print both 'Math' courses.  SETS also have MEMBERSHIP TESTS with other sets.

#print('Math' in cs_courses)
# OUTPUTS:  True, because 'Math' is in both art_courses and cs_courses.

#------------------------------------COMPARING SETS-------------------------------------------

#FINDING THE INTERSECTION OF SETS:  Use the .intersection METHOD on the cs_courses SET.
#print(cs_courses.intersection(art_courses))

#FINDING THE DIFFERENCE OF SETS:  Use the .difference METHOD on the cs_courses SET.
#print(cs_courses.difference(art_courses))

#COMBINING SETS AND SHOWING ALL OFFERED:  Use the .union METHOD on the cs_courses SET.
#print(cs_courses.union(art_courses))

#---------------------------CREATING EMPTY LISTS, TUPLES, AND SETS-----------------------------

#              YOU CAN NOT CREATE AN EMPTY SET.  IT WILL BE AN EMPTY DICTIONARY

# empty_list = []
# empty_list = list()   #Built in list class

# empty_tuple = ()
# empty_tuple = tuple()  #Built in tuple class

# empty_set = {}  #  **THIS IS NOT RIGHT** THIS WILL CREATE AN EMPTY DICTIONARY.
# empty_set = set()  <---------- This is the proper method for an EMPTY SET.  You need to use the Built-in set CLASS.
