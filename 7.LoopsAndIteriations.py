nums = [1, 2, 3, 4, 5,]

# for num in nums:
# 	print(num)

# -------------------------------THE BREAK STATEMENT: OH GOD GET ME OUT-----------------------

# for num in nums:
# 	if num == 3:
# 		print('Found it!')
# 		break   #  If the break statement would have been above the conditional on ln 9, it would have printed the 3.
# 	print(num)

# --------------------------CONTINUE: SURE, I DONT CARE ABOUT INFINITES------------------------
# for num in nums:
# 	if num == 3:
# 		print('Found it!')
# 		continue 
# 	print(num)
#----------------------------LOOPS IN LOOPS:  THE ELECTRIC JIGGALO---------------------
#
#
#
# for num in nums:
# 	for letter in'abc':
# 		print(num, letter)

#  This loops through every letter in the string, then moves on.  1a, 1b, 1c, 2a, 2b, 2c...

#--------------------------RUNNING THROUGH A LOOP A CERTAIN # OF TIMES----------------------------
# for i in range(1, 11): 
# 	print(i)

 # This would start at 1, and go up to 10.
# -------------------------------------WHILE LOOPS------------------------------------

x = 0

#EXAMPLE 1:
#
# while x < 10:
# 	print(x)
# 	x += 1

#  OUTPUT:  Counts to 9 from 0.
#
#EXAMPLE 2:

# while x < 10:
# 	if x == 5:
# 		break
# 	print(x)
# 	x += 1

#  OUTPUT:  Counts to 5, then breaks out.

while True:
	if x == 100099:
		print("PlsStop.png")
	if x == 10010000:
		break
	print(x)
	x+=1

