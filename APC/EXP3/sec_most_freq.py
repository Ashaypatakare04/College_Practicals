s=input("Enter a string: ")
max=s[0]
sec=s[1]
for i in s:
    if s.count(i)>s.count(max):
        sec=max
        max=i
    elif s.count(i)>s.count(sec):
        sec=i
print(max,": ",s.count(max))
print(sec,": ",s.count(sec))