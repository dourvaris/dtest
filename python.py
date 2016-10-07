from __future__ import unicode_literals
from module import function, new_function
import something

def function(arg1, arg2, arg3=False, arg4=1, arg5="string", arg6='string'):
     '''
     Multi
     Line
     Docstring! 
     '''
     for i in range(arg1):
         variable = something.somefunction(arg2, arg3)
         variable = variable + arg4
         variable += 45 # comment this line
         variable += 0x9
         print 6
         arg6 += ("a string" "more string")
         bool(5 + 5)
         print 5
     return 9

def otherfunction(arg, *args, **kwargs):
     """ Doc string !!! """ # comment
     while arg: # comment
         arg = arg - 1
         yield arg
         function(1, 2, True, 5, "hello")

# these lines
# are commented

if __name__ == '__main__':
    print 'okay then'
    import os
    import sys
    sys.exit(3)
