import webbrowser
import os

#webbrowser.open("https://www.youtube.com/watch?v=Uh2ebFW8OYM")

os.chdir('C:\\Users\\Anon\\Desktop\\')  #changes the current working directory to the desktop
print(os.getcwd()) #prints the current working diriectory to prove the above function and method worked

#--------------------------------------OPENING, WRITING, AND CLOSING FILES--------------------------------

# If we don't specify an argument, it defaults to opening the file for reading...but for explicities sake:

# open('text.txt', 'r')

# r would read the file
# w would write to the file
# a would append to the file
# r+ would read AND write to the file

#--------------------------------------------

# print(f.name) would print the name of the file
# print(f.mode) would print the mode of the file (read, write...)
# print(f.read) would print the file itself (best for small files)
# print(f.readlines) prints every line in the file as an element of a list
# print(f.readline) prints the NEXT line in the file.  (1 at a time)
# 

# try:   # Use TRY and FINALLY to have document-close redundancy.  Not needed, encouraged.
# 	myfile = open('demo.txt', 'w')
# 	myfile2 = open('test.txt', 'w')

# 	myfile.write('This is Line 1\nThis is line 2\nThis is line 3\nThis is Line 4')
# 	myfile2.write('This is a test document creation')
# finally:
# 	myfile.close()
# 	myfile2.close()



#----------------------------------USING A CONTEXT MANAGER:  WITH-----------------------------------------

# WITH and AS to open files as a temporary VARIABLE in the WITH statement:
# They allow us to work with files in this block of code.  When we exit the block of code, it:
# CLOSES it for us.

# with open('demo.txt') as f:
# 	f_contents = f.read()
# 	print(f_contents)
	# The file is AUTOMATICALLY CLOSED using the WITH statement.  Even if EXCEPTIONS occur!

#----------------------------------HOW TO READ FROM AN EXTREMELY LARGE FILE---------------------------------

# Iterate over the lines in a file by:

# with open('demo.txt') as f:

# 	f_contents = f.read(100)  #prints the first 100 characters of our file
# 	print(f_contents, end='')

# 	f_contents = f.read(100)  #prints the next 100 characters of the file
# 	print(f_contents, end='')

# When we hit the end of the file, READ will just return empty strings.

# Use this with a while loop, like:

# with open('demo.txt') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)  
# 	while len(f_contents) > 0:
# 		print(f_contents, end='*')  # Astrisks here to show where it breaks the 10 characters above.
# 		f_contents = f.read(size_to_read)  # We want to read-in the next chunk of characters, so it
# 										   # reruns the loop.


#-----------------------------FINDING THE CURRENT POSITON OF THE READ METHOD ------------------------------
# f.tell = shows you where the current position is in the advance in the loop.  (10 in this case)

# with open('demo.txt') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)  
# 	while len(f_contents) > 0:
# 		print(f_contents, end='*')  # Astrisks here to show where it breaks the 10 characters above.
# 		f_contents = f.read(size_to_read)

#-----------------------------STARTING A READ AT A SPECIFIC POINT IN A FILE---------------------------------


	# size_to_read = 10

	# f_contents = f.read(size_to_read)  
	# print(f_contents, end='')

	# f.seek(0)

	# f_contents = f.read(size_to_read)  
	# print(f_contents)


#-------------------------------------SECTION 2:  WRITING TO FILES-------------------------------------------

# Just using OPEN with the WRITE mode alone creates the file.  Nothing needs to be written.

# with open('test2.txt', 'w') as f:
# 	pass



# with open('test2.txt', 'w') as f:
# 	f.write('Test Line 1')
# 	f.write('Test Line 2')

# Does NOT put line separators in automatically


# To overwrite, use SEEK:  (seek(0))

# with open('test2.txt', 'w') as f:
# 	f.write('Test Line 1')
# 	f.seek(0)
# 	f.write('Test Line 2')

# 'Test Line 2' overwrites 'Test Line 1', but it ONLY OVERWRITES WHAT IT NEEDS TO:


# with open('test2.txt', 'w') as f:
# 	f.write('Test Line 1')
# 	f.seek(0)
# 	f.write('R')

#Writes "Rest Line 1" into the txt file.

#------------------------------READING AND WRITING TO FILES AT THE SAME TIME-------------------------------

# with open('demo.txt','r') as rf: # We have the original file open, reading it.
# 	with open('demo_copy.txt','w') as wf: # Then we have a file that doesn't exist yet, writing to it.
# 		for line in rf: # Then, for each line in our original file, 
# 			wf.write(line) # Write that line to WF


#------------------------HOW TO DO SOMETHING SIMILAR, ONLY COPY A LARGE IMAGE FILE-------------------------

# Open in binary mode (reading/writing bytes, instead of text) , rb and wb

# with open('test.jpg','rb') as rf:
# 	with open('test_copy.jpg','wb') as wf:
# 		for line in rf:
# 			wf.write(line) 
  
#----------------------SOMETIMES YOU WANT MORE CONTROL OVER WHAT YOU'RE READING/WRITING---------------------

# with open('demo.txt','r') as rf:
# 	with open('demo_copy.txt','w') as wf: 
# 		chunk_size = 4096
# 		rf_chunk = rf.read(chunk_size) # Read-in a chunk of your read file
# 		while len(rf_chunk) > 0: # Writes these chunks to our copy until there's nothing left of the original.
# 			wf.write(rf_chunk)
# 			rf(chunk) = rf.read(chunk_size) 