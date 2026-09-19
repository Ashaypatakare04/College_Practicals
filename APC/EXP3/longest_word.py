s=input("Enter a string: ").split()
max=''
for i in s:
    if len(i)>len(max):
        max=i
print("Longest word: ",max)