import webbrowser
import os

# webbrowser.open("https://www.youtube.com/watch?v=Uh2ebFW8OYM")

os.chdir('C:\\Users\\Anon\\Desktop\\')  #changes the current working directory to the desktop
print(os.getcwd()) #prints the current working diriectory to prove the above function and method worked

try:   # Use TRY and FINALLY to have document-close redundancy.  Not needed, encouraged.
	myfile = open('demo.txt', 'w')
	myfile2 = open('test.txt', 'w')

	myfile.write('This is Line 1\nThis is line 2\nThis is line 3\nThis is Line 4')
	myfile2.write('This is a test document creation')
finally:
	myfile.close()
	myfile2.close()

# WITH and AS to open files as a temporary VARIABLE in the WITH statement:

with open('demo.txt') as f:
	print(f.read())
	# The file is AUTOMATICALLY CLOSED using the WITH statement.  Even if EXCEPTIONS occur!

