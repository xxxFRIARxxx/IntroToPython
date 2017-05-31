

# This function takes in 2 arguments:  a list to_search, and a target to look for.
# This finds the index of a value in a sequence.

print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
	for i, value in enumerate(to_search):
		if value == target:
			return i
	return -1