def rem():
    b=int(input("Enter elements to remove: "))
    arr.remove(b)
    print("After remove:", arr)

def add():
    a=int(input("Enter elements to add: "))
    arr.append(a)
    print("After append:", arr)
    
def ins():
    a=int(input("Enter elements to insert: "))
    b=int(input("Position to enter: "))
    arr.insert(b,a)
    print("After insert:", arr)

def sorted():
    arr.sort()
    print("Sorted:", arr)
    
def rev():
    arr.reverse()
    print("Reverse:", arr)
    
def minmax():
    print("Maximum:", max(arr))
    print("Minimum:", min(arr))

def sm():
    print("Sum:", sum(arr))
    
    
print("Array: ")
arr=[]
for i in range(5):
    a=int(input("Enter elements: "))
    arr.append(a)
    
print("Array:", arr)

print("Length:", len(arr))

add()
ins()
rem()
sorted()
rev()
minmax()
sm()





