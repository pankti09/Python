#Title : WAP to find factorial of given number

n=int(input("Enter a integer:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
