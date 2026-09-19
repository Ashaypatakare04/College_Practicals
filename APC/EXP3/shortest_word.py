s=input("Enter a string: ").split()
min=s[0]
for i in s:
    if len(i)<len(min):
        min=i
print("shortest word: ",min)