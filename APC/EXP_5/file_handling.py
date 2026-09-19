import os
def filehandle():
    file=open("example.txt",'x')
    file.close()

    file=open("new.txt",'x')

    with open("new.txt",'w') as file:
        file.write("This is a new.txt")
        
    with open("new.txt",'r') as file:
        b=file.read()
        print(b)
        
    with open("new.txt", "a") as file:
        file.write("\nThis is append.")
        
    with open("new.txt", "r+") as file:
        c = file.read() 
        file.seek(0)           
        file.write("this is r+ mode") 

    with open("new.txt", "a+") as file:
        print("Existing data:", file.read())
        file.write("\nthis is a+ mode")

    file=open("new.txt",'r')
    print("\n",file.read())
    file.close()

    file=open("new.txt",'r')
    print("\n",file.readline())
    file.close()

    file=open("new.txt",'r')
    print("\n",file.readlines())
    file.close()

    with open("new.txt") as file:
        print("current pointer:",file.tell())
        file.seek(5)
        print("after seek(5):",file.tell())
        
        
    os.remove('new.txt')
    os.unlink('example.txt')
    
    numbers = [65, 66, 67, 68]
    
    with open("numbers.bin", "wb") as file:
        file.write(bytes(numbers))
    
    with open("numbers.bin", "rb") as file:
        content = file.read()
        print("bytes:", content)
        
    os.remove('numbers.bin')
    
filehandle()
