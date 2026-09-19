arr=list(map(int,input("Enter the elements in array").split(" ")))
search=int(input("Element to be found"))
loc=0
for i in arr:
    if(search==arr[i]):
        print(f"Element {arr[i]} found  at index {i}")
        loc=1
        break
if(loc==0):
    print(f"Element {search} not found")
