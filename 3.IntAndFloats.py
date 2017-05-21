#------------LESSON 2:  INTEGERS AND FLOATS-------------

#  INTEGERS ARE WHOLE NUMBERS.  2.  57.  2354.  
#  FLOATS ARE NUMBERS LIKE PI, WITH DECIMALS.  3.14.  5.1992455.

#--------------ARITHMETIC OPERATORS----------
#  Addition:		3 + 2
#  Subtraction:		3 - 2
#  Multiplication:	3 * 2
#  Division:		3 / 2
#  Floor Division:	3 // 2  DROPS THE DECIMAL FROM REGULAR DIVISION
#  Exponent:		3 ** 2  THIS EXAMPLE IS 3 SQUARED
#  Modulus:			3 % 2   THIS GIVES US THE REMAINDER AFTER DIVISION.  2 GOES INTO 3 ONCE, WITH 1 LEFT OVER.
#                           USE A MODULUS TO FIND OUT IF A NUMBER IS EVEN OR ODD.  
#                           EVEN = 0, ODD = 1 AFTER A MOD 2.
# 

# -----------INCREMENTING A VARIABLE--------------

#  num  = 1
#  num = num + 1
#  OR just num +1=
#  WORKS WITH ALL OTHER OPERATIONS

# ------------OTHER FUNCTIONS THAT CAN HELP WITH NUMBERS----------
#
#  1:  ABS - Absolute Value
#
#  Removes the sign from any negative numbers
#  AS AN EXAMPLE:  print(abs(-3))
#
#  2:  round - Rounds to the nearest value.  Up or down.
#
#  AS AN EXAMPLE:  print(round(3.75)) would round to 4.
#
#  You can also round to second arguments to tell how many digits to round to.
#
#  print(round(3.75 , 1)) would round to the first decimal
#
#
# ----------------SECTION 2:  COMPARISON OPERATORS---------------
#
#  Comparisons:
#  Equal:				3 == 2
#  Not Equal:			3 != 2
#  Greater Than:		3 > 2
#  Less Than:			3 < 2
#  Greater or Equal:	3 >= 2
#  Less or Equal:		3 <= 2
#
# -----------------------------------------------------------------

#  num_1 = 3
#  num_2 = 2

#  print(num_1 == 2)
#  Would show FALSE, because 1 !=2
#
# ------------------------------------------------------------------
#
#  It's possible to have variables that LOOK like numbers.
#  
#  num_1 = "100"
#  num_2 = "200"

#  print(num_1 + num_2)
#  Would show "100200" because it's printing the variable or string, not the INTIGER.
#
#  You need to do what's known as CASTING:
#
#  ---------------CASTING A NUMBER INTO AN INTEGER-----------------------
#  num_1 = "100"
#  num_2 = "200"
#
#  num_1 = int(num_1)
#  num_2 = int(num_2)
#
#  print(num_1 + num_2)
#  Would show "300" becasuse it's converting the variable or string into an INTIGER!


