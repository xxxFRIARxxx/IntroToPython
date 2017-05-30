
#-------------------------------------LESSON 1:  STRINGS/FORMATTING--------------------------------


greeting = "Hello" #BY CONVENTION, ALL NAMES FOR VARIABLES ARE LOWERCASE, AND DESCRIPTIVE AS POSSIBLE.  
name = "Michael"   #"GREETING", or "NAME" FOR EXAMPLE
greeting2 = "Hi"
name2 = "Thomas"

# SETTING A VARIABLE TO AN ALTERED VERSION OF ITSELF IS OK, AND YOU'LL USE IT OFTEN.
# Example:  
# message = 1
# message = 2
#print (message) would output 2
 
# USE DOUBLE QUOTES IN STRINGS WHERE SINGLE QUOTES ARE IN STRING, AND VICAVERSA.  YOU CAN ALSO BACKSLASH
# \ TO ESCAPE THE SINGLE QUOTE.  "Bobby's World"  FOR EXAMPLE

# THINK OF "name" "greeting" above as full STRINGS and you can access the STRINGS INDIVIDUALLY

# The FIRST CHARACTER OF THIS STRING IS 0.  

#---------------------------------------MULTI-LINE STRINGS---------------------------------

# MULTI-LNIE STRINGS ARE 3 QUOTES ON BOTH SIDES OF THE STRING.  DOUBLE OR SINGLE QUOTES.  3 OF THEM.

multi_line_string = """THIS TEXT
THAT SPANS
3 LINES"""

#--------------------------------FINDING RANGES OF STRINGS IN LINE--------------------------------

message_length = "An example is print(name[11])."  
# This would print the 11th character of the string.

# Ranges can be found with colons.  [0:4] as an example.  You can also leave off the 0 of the beginning...
# ...*****BUT NOT THE END******

length_of_a_string = "An example is: print(len(name))"

#---------------------------F STRINGS AND STRING FORMATTING (same thing)------------------------------

fstringmessage = f"{greeting}, {name.upper()}. Welcome to the Server!" 

# THESE ^^ ARE F STRINGS.  THEY'RE LIKE STRING FORMATTING BELOW, BUT SIMPLER. JUST PUT A FUCKING "f".  
# THEY ALLOW YOU TO WRITE CODE INTO THE PLACEHOLDER AS WELL, AS IN THE EXAMPLE ABOVE

# STRING FORMATTING"

string_formatting_message = "{}, {}. Welcome Number 2!".format(greeting2, name2)  # THIS IS STRING FORMATTING.  
# SAME THING AS ABOVE, ONLY LONGER, BUT ALLOWS SPECIFIC FORMATTING.


#-----------------------FINDING OTHER FUNCTION/METHODS TO WORK WITH:  THE HELP FUNCTION----------------------

message_dir_help = print(dir(name))  

# THE "DIR" FUNCTION SHOWS ME ALL ATTRIBUTES AND METHODS AVIALABLE IN THAT VARIABLE

#print(help(str)) 
# EXPLAINS IN *EXTREME* DETAIL OF WHAT THESE METHODS DO, AND WHAT ARGUMENTS THEY HAVE.  EXTREMELY USEFUL.
#   ALSO MODIFYABLE LIKE "str.lower", FOR EXAMPLE.



 
