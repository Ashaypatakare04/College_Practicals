class year:
    def __init__(self, y):
        self._year = y

class month(year):
    def __init__(self, m, y):
        year.__init__(self, y)
        self._month = m

    def display(self):
        print("This is ", self._month, "of year", self._year, "!")
 
print("This is an example of single inheritance with protected variables-->")      
obj = month("August", "2026")
obj.display()