s1="Kolhapur"
s=s1.lower()
v=['a','e','i','o','u']
vowel=0
con=0
for i in s:
    if i in v:
        vowel+=1
    else:
        con+=1
print("vowels: ",vowel,"\nconsonats: ",con)