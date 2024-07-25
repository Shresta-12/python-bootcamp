class Cal:
    def add(self,*args):
        return sum(args)
 #take inputs:
obj1=Cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
print(obj1.add(1,2,3,4,5))   