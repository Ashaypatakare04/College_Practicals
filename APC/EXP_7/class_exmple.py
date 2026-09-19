class demo:
    def __init__(self):
        print("Constructor is called!")
    def fun(self,n):
        self.name=n
        print("Hi",self.name)
    def __del__(self):
        print("destructor is called!")
obj=demo()
obj.fun("Ashay")