class Parent:
    def father(self):
        print("this is a parent.")


class eldest_son(Parent):
    def eldest(self):
        print("this is elder child, Vinayak!")


class youngest_son(Parent):
    def youngest(self):
        print("this is younger son, Abhinav!")

class brother(eldest_son,youngest_son):
    def bro(self):
        print("Two brothers are close.")
        
obj=brother()
obj.bro()
obj.youngest()
obj.eldest()
obj.father()