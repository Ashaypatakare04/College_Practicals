class grandfather:
    def __init__(self):
        print("This is a grandparent constructor!!!")
    def g(self):
        print("Hello! this is grandfather!")

class father(grandfather):
    def __init__(self):
        grandfather.__init__(self)
        print("This is a parent constructor!!!")
    def f(self):
        print("this is father")

class son(father):
    def __init__(self):
        father.__init__(self)
        print("This is a child constructor!!!")
    def s(self):
        print("this is son of family.")

obj=son()
obj.g()
obj.f()
obj.s()
