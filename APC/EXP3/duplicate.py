s=input("Enter a string: ")
s1=''
print("Duplicate char: ")
for i in s:
    if i in s1:
        print(i,end=' ')
    else:
        s1+=i