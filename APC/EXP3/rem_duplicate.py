s=input("Enter a string: ")
s1=""
for i in s:
    if i not in s1:
        s1+=i
print("string after removing duplicate: ",s1)