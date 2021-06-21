#Title   : Program to check given number is Armstrong number 
#Name    : Shah Pankti S.
#Roll No.: 17EC078
#Date    : 26/12/2019
#Time    : 22:25

n=int(input('Enter any number: '))
g=str(n)
s=0
for i in g:
    s+=int(i)**3
if(int(s)==n):
    print("Armstrong no")
else:
    print("Not an armstrong no")
