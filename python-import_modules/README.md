## Import modules
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:
-   Definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).
- The dir() function in python is an inbuilt function used on an object to look at all the properties / attributes and methods of that object, without its values (if any). It is used as dir({object}) and takes only one optional parameter
## The dir():
- function returns all properties and methods of the specified object, without the values.
- This function will return all the properties and methods, even built-in properties which are default for all object.