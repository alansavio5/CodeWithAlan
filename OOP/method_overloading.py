# if we define a method multiple times, the last definition will override the previous one. so python will generate an error

# to solve this we can use dispatch function using a third party module named multiple dispatch

# This module has a @dispatch decorator. It takes the number of arguments to be passed to the method to be overloaded

from multipledispatch import dispatch

class Example:

    @dispatch(int,int)
    def add(self,a,b):
        x = a+b
        return x

    @dispatch(int,int,int)
    def add(self,a,b,c):
        x = a+b+c
        return x

obj = Example()

print(obj.add(1,2,3))
print(obj.add(1,2))

