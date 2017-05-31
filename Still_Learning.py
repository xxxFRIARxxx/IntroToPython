# Objects are created using classes.  Classes are actually the focal point of OOP

# The CLASS describes what the OBJECT will be, but is separate from the object itself.

# AKA:  A CLASS is an object's "blueprint", description, or definition.
import sys

# class Cat:
# 	def __init__(self, color, legs):
# 		self.color = color
# 		self.legs = legs

# felix = Cat("ginger", 4)
# rover = Cat("dog-colored", 4)
# stumpy = Cat('brown', 3)

# The code above defines a CLASS named "Cat", which has 2 attributes: color and legs.
# Then, the CLASS is used to create 3 separate objects of that class.

print(help("__init__"))

# ---------------------------------THE __INIT__ METHOD--------------------------------------

# This is called when an instance (object) of the class is created, using the CLASS name as a function.

# All methods must have "self" as their first paramater, although it's not explicititly passed, Python adds
# the "self" argument to the list for you.  You do not need to include it when you call the methods..

# Within a method definition, self refers to the instance calling the method.

#--------------------------------------------------------------------------------------------

# Instances of a class have ATTRIBUTES, which are pieces of data associated with them.

# In this example above on line 13, Cat instances have atttributes "color" and "legs".
# These can be accessed by putting a DOT, and the ATTRIBUTE NAME after an instance.

# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's
# attributes.

