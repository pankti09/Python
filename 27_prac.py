#Title   : Program to print the inverted star pattern.
#Name    : Shah Pankti S.
#Roll No.: 17EC078
#Date    : 26/12/2019
#Time    : 22:40

for i in range(6):
    for j in range(1,i+1):
        print(' ',end=' ') 
    for j in range(6,i,-1):
        print('*',end=' ')
    print()
    
