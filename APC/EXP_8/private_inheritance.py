class Year:
    def __init__(self, y):
        self._year = y

class Month(Year):
    def __init__(self, m, y):
        super().__init__(y)
        self.__month = m
        
    def display(self):
        print(f"This is {self.__month} of year {self._year}!")
  
print("This is an example of single inheritance with private variable-->")      
obj = Month("December", "2026")
obj.display()