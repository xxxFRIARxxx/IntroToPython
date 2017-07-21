import os

#------------------PARSING AND RENAAMING OF MULTIPLE FILES--------------------

# os.chdir("C:\\PATH\\TO\\THE\\FILE\\")

# for f in os.listdir():  # lists everything in the current working directory
#     print(f)

#------------------SPLITTING THE EXTENTION FROM THE REST OF THE FILENAME---------------
# for f in os.listdir():
#     print(os.path.splitext(f))  # os.path.splitext gives us a TUPLE, splitting off the extention.

# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     print(file_name)            # These 3 lines would print out the filename of the file, without extention.

#-----------------RENAMING THE FILE WITH THE NUMBERS AT THE BEGINNING (say they're at the end)----------------

# for f in os.listdir():
#     f_name, f_ext = os.path.splittext(f)
#---------------------------------------STRIP AND SPLIT TO RENAME THE FILE BY RULES----------------------------------

# for f in os.listdir():
#     f_name, f_ext = os.path.splittext(f)

    # f_title, f_course, f_num = f_name.split('-')

    # f_title = f_title.strip()
    # f_course = f_course.strip()
    # f_num = f_num.strip()

    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
#----------------------------------TO RENAME AFTER EVERYTHING LOOKS GOOD IN PRINT---------------------------

# Take the print statement on line 29, and replace with a new variable:

# for f in os.listdir():
    # f_name, f_ext = os.path.splittext(f)
    # f_title, f_course, f_num = f_name.split('-')

    # f_title = f_title.strip()
    # f_course = f_course.strip()
    # f_num = f_num.strip()
    # new_name = '{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext)

    # os.rename(f, new_name)  # Renames the original file 'f' to the 'new_name' variable.



