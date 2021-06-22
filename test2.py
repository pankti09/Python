#Title : WAP to find given number is prime or not

n=int(input("Enter a integer:"))


if (n==1):
    print("1 is neither prime nor composite")
elif ( n % 2 ==1):
    print("Prime number")
else :
    print("Composite number")
