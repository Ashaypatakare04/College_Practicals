class year:
    def __init__(self,y):
        self.year=y
class month(year):
    def __init__(self,m,y):
        year.__init__(self,y)
        self.month=m
    def display(self):
        print("This is ",self.month,"of year",self.year,"!")
 
print("This is an Demo of single inheritance-->")       
obj=month("September","2026")
obj.display()
