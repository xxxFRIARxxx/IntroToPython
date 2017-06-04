import webbrowser
import os

webbrowser.open("https://www.youtube.com/watch?v=tJxcKyFMTGo")
#----------------------------------------THE OS MODULE--------------------------------------

# Navigate the file system, get file system, look up and change environment variables,
# move files around...etc

# WHEN WORKING W/ A NEW MODULE, IF YOU PRINT THE DIR FUNCTION OF THE MODULE 
# WE'RE WORKING WITH, IT'LL SHOW YOU ALL OF THE ATTRIBUTES AND METHODS WE CAN RUN
# ON THE MODULE:

#print(dir(os))

# -------------------------------GETTING THE CURRENT DIRECTORY------------------------------

#print(os.getcwd())

#--------------------------------NAVIGATING TO ANOTHER LOCATION-----------------------------

# enable the print statement on line 18

os.chdir('C:\\Users\\Anon\\Desktop\\')
#  chdir stands for CHANGE DIRECTORY

#print(os.getcwd())

#------------------WHAT FILES AND FOLDERS ARE IN THE CURRENT WORKING DIRECTORY--------------

#print(os.listdir())

# You can pass a path into this ^^^, but by default, will display the CWD

#-------------------------------CREATING A NEW FOLDER IN THE CWD----------------------------

#  Say we want to create a folder called OS-Demo-2 in the CWD:

#  2 WAYS:

# os.mkdir('OS-Demo-2')               #  Will NOT create subdirectories  
# os.makedirs('OS-Demo-2/Sub-Dir-1')  #  Creates Directories automatically
#                                      for any Subdirectories you supply.

#---------------------------------------DELETING FOLDERS------------------------------------

#os.rmdir('OS-Demo-2')                 # WILL NOT remove intermediate directories.
#os.removedirs('OS-Demo-2/Sub-Dir-1')  # WILL REMOVE INTERMEDIATE DIRECTORIES

#-----------------------------------RENAMING A FILE OR FOLDER-------------------------------

#                       CREATE A FILE ON YOUR DESKTOP CALLED test.txt

#os.rename('test.txt', 'demo.txt')  
#  ORIGINAL file name FIRST, DESIRED second

#--------------------------------PRINTING OUT INFO ABOUT A FILE-----------------------------

# print(os.stat('demo.txt'))

# SIZE OF THE FILE, AND MUCH MORE

#print(os.stat('demo.txt'))
#print(os.stat('demo.txt').st_size)  #  SIZE OF THE FILE
#print(os.stat('demo.txt').st_mtime) #  RETURNS THE LAST MODIFICATION TIME

#   ^^^^    THAT RETURNS A TIMESTAMP.  TO GET IT READABLE:

from datetime import datetime

# mod_time = os.stat('demo.txt').st_mtime

# print(datetime.fromtimestamp(mod_time))

# -------------LOOKING AT THE ENTIRE DIRECTORY TREE (all the files on the desktop)----------

#os.walk()   
# This is a generator that makes a tupple of 3 values of the directory tree:

#  For each directory it sees:  the path, the directories in the path, and the files
#  in the path

#  Starts from the top down.

for dirpath, dirnames, filenames in os.walk('C:\\Users\\Anon\\Desktop\\'):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()

#  Say you have a file on the desktop, but don't know where it is:

# USE os.walk, like above:

#-----------ACCESSING THE HOME DIRECTORY LOCATION FROM THE HOME ENVRIONMENT VARIABLE---------

#print(os.environ.get('HOME'))

#  Say you want to use this to create a file in your home directory:

#'test.txt'

# file_path = os.environ.get('HOME') + 'text.txt'
#print(file_path)

# To get around the slash/double slash, use the .path module

#file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
#print(file_path)

# print(os.path.basename('/tmp/test.txt'))  #prints the base name of the directory
#print(os.path.dirname('/tmp/test.txt'))  # prints the directory name
#print(os.path.split('/tmp/test.txt'))   #  prints both the directory first, and base name 2nd
#print(os.path.exists('/tmp/test.txt'))   #Checks the existence of the path on the file system
#print(os.path.isdir('/tmp/test.txt'))    #returns TRUE if it's a directory
#print(os.path.isfile('/tmp/test.txt'))   #returns TRUE if it's a file
#print(os.path.splitext('/tmp/test.txt'))  #will split the file root and the path of the extention
#                                              ^^^ last one here very useful for file manipulation

#print(dir(os.path))



