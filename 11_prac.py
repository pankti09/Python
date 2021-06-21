#Title   : Program to prompt the user for hours and rate per hour to compute gross pay. Company will give the employee 1.5 times the Hourly rate for hours worked above 40 hours.
#Name    : Shah Pankti S.
#Roll No.: 17EC078
#Date    : 26/12/2019
#Time    : 20:00

hours=int(input('Enter the number of hours: '))

rate_per_hour=int(input('Enter the rate per hour: '))

if(hours>40):
    k=hours-40
    gross_pay=40*rate_per_hour+1.5*rate_per_hour*k
else:
    gross_pay=rate_per_hour*hours
print('Gross Pay:',gross_pay)
