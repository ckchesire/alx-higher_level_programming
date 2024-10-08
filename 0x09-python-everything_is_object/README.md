# 0x09. Python - Everything is object

In Python, everything is an object, which is an instance of a class. Classes 
serve as blueprints for creating objects, while objects represent the actual 
data in memory.Immutable objects, like `int`, `str`, and `tuple`, cannot be 
changed after creation, whereas mutable objects, like `list`,`dict`, and `set`,
can be modified. Python variables hold references to objects, and multiple 
variables can reference the same object, known as aliasing. The `is` operator 
checks if two variables refer to the same object, and `id()` returns an 
object's memory address. Pythonpasses variables to functions by reference, 
meaning mutable objects can be changed within the function, while immutable 
objects create new instances if modified.
