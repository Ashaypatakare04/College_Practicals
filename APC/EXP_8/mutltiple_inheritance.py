class father:
    def __init__(self,f):
        self.father=f

class mother:
    def __init__(self,m):
        self.mother=m
        
class child(father,mother):
    def __init__(self,c,f,m):
        father.__init__(self,f)
        mother.__init__(self,m)
        self.child=c
    def display(self):
        print("Your Name:",self.child)
        print("Father's Name:",self.father)
        print("Mother's Name:",self.mother)
        
print("This is an example of multiple inheritance-->")       
obj=child("Ashok Patil","Amar Patil","Gouri Patil")
obj.display()