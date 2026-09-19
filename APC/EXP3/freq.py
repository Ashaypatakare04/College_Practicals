s=input("Enter a string: ")
freq={}
for i in s:
    freq[i]=s.count(i)
print(freq)