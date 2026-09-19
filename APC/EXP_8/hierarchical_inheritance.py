class Parent:
    def father(self):
        print("this is a parent.")


class eldest_son(Parent):
    def eldest(self):
        print("this is elder child, Vinayak!")


class youngest_son(Parent):
    def youngest(self):
        print("this is younger son, Abhinav!")


obj_a = eldest_son()
obj_a.eldest()    
obj_a.father()  

obj_b = youngest_son()
obj_b.father()    
obj_b.youngest()  
