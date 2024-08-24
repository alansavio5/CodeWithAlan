#<<<<<<<< here is a solution for method overloading >>>>>>>>>
# we can use conditional statements to solve it

class Example:

    def add(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:
            x = a+b+c
        
        elif a!=None and b!=None and c==None:
            x = a+b
        
        return x

obj = Example()

print(obj.add(1,2,3))
print(obj.add(1,2))