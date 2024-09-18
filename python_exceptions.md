# Python Exceptions🐍

![Exceptions](exception.webp)

In Python, exceptions are errors that occur during the execution of a program, typically caused by unexpected conditions. They can range from syntax errors to issues that occur while a program is running. Python has a wide variety of built-in exceptions to handle these errors effectively. Here are some common types of exceptions:

**IndexError:** Occurs when trying to access an index that is out of range in a list or a sequence.

**KeyError:** Raised when trying to access a dictionary with a key that doesn’t exist.

**ValueError:** Happens when a function gets an argument of the correct type but inappropriate value (e.g., passing letters to a function expecting numbers).

**TypeError:** Raised when an operation or function is applied to an object of inappropriate type (e.g., adding a string and an integer).

**ZeroDivisionError:** Occurs when a number is divided by zero.

**AttributeError:** Happens when an attribute reference or assignment fails (e.g., trying to call a method on an object that doesn't have it).

**ImportError and ModuleNotFoundError:** These appear when Python is unable to load a module.

**FileNotFoundError:** Raised when trying to open a file that doesn't exist.

**MemoryError:** Raised when an operation runs out of memory.

**StopIteration:** Raised to signal the end of an iteration.

**SyntaxError:** Raised when Python encounters incorrect syntax in the code.

These exceptions help in debugging and allow developers to write more robust code by handling potential errors using try-except blocks.
