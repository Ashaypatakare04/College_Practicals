class Demo:
    def __init__(self, name, id, branch):
        print("Constructor is called!")
        self.__name = name
        self.__id = id
        self.__branch = branch

    def __info(self):
        print("Name:",self.__name,"\nRoll NO.:" ,self.__id,)
        
    def branch(self):
        print("Branch:",self.__branch)
    
    def __del__(self):
        print("Destructor is called!")

obj = Demo("ABC", 56, "CSE")
obj.branch()
obj._Demo__info()
