#Title   : Program to print the pattern 'G'.
#Name    : Shah Pankti S.
#Roll No.: 17EC078
#Date    : 26/12/2019
#Time    : 22:35

g=''
for i in range(7):
    for j in range(7):
        if((j==1 and i!=0 and i!=6) or ((i==0 or i==6) and j>1 and j<6) or(i==3 and j>3 and j<6) or (j==5 and i!=0 and i!=1 and i!=2) or(j==6 and i==3)):
            g+='*'
        else:
            g+=' '
    g+='\n'
print(g)
