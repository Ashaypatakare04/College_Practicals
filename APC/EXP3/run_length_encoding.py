s=input("Enter a string: ")
s1=""
for i in s:
    if i not in s1:
        s1+=i
for i in s1:
    print(i,s.count(i),end="")