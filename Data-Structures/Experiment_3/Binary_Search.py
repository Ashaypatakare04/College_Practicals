arr=list(map(int,input("Enter the elements in array").split(" ")))
search=int(input("Element to be found"))
loc=0
beg=0
end=len(arr)-1
while(beg<=end):
    mid=((beg+end)//2)
    if(search==arr[mid]):
        print(f"Element {search} found  at index {mid}")
        loc=1
        break
    elif(search<arr[mid]):
        end=mid-1
    else:
        beg=mid+1
if(loc==0):
    print(f"Element {search} not found")
    
