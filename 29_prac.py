#Title   : Program to make scientific calculator
#Name    : Shah Pankti S.
#Roll No.: 17EC078
#Date    : 26/12/2019
#Time    : 22:55

import math
a=int(input('Enter any number: '))
n=int(input('Enter any number: '))
op=input('Enter the operation: ')
if(op=='sin'):
    print('sin({})'.format(a),'=',math.sin(a))
elif(op=='cos'):
    print('cos({})'.format(a),'=',math.cos(a))
elif(op=='tan'):
    print('tan({})'.format(a),'=',math.tan(a))
elif(op=='log'):
    print('log({})'.format(a),'=',math.log(a))
elif(op=='%'):
    print(a,'%',n,'=',a%n)
elif(op=='square'):
    print('Square of a','=',a**2)
elif(op=='cube'):
    print('Cube of a','=',a**3)
else:
    print('Invalid operation')

