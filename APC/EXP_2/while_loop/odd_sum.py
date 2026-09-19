n=int(input("Enter a number: "))
sum=0
i=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i=i+1
print("The sum of odd numbers from 0 to", n, "is:", sum)
