s=input("Enter a string: ")
max=s[0]
for i in s:
    if s.count(i)>s.count(max):
        max=i
print(max,": ",s.count(max))