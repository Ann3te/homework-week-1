#!/usr/bin/python

import sys

# argv is part of the sys module
# argument vector a.k.a the list of parameters or inputs to the program

argc = len(sys.argv)


# 'if' is called a condition expression
if argc> 1:
    print('Too many args')
else:
    # where is a variable whose value is a string 'World'
    where = 'World'
    print("Hello", where)

print('Goodbye from ' + sys.argv[0])
