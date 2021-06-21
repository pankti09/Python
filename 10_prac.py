#Title   : Program that Prepare grade sheet. For each of following subjects the marks should be given by user and grades should be calculated according to the given table and grade should be displayed for each subject.  
#Name    : Shah Pankti S.
#Roll No.: 17EC078
#Date    : 26/12/2019
#Time    : 19:45

Subject=["RF & Microwave","Python","Antenna","Microwave integrated circuit"]

RFM=int(input("Enter marks of RF and Microwave:"))
Py=int(input("Enter marks of Python:"))
An=int(input("Enter marks of Antenna:"))
MIC=int(input("Enter marks of Microwave integrated circuit:"))

final_grade_points=[]
letter_grade=[]
if(RFM>=80):
    l='AA'
    gp=10
elif(RFM>=75 and RFM<=80):
    l='AB'
    gp=9
elif(RFM>=70 and RFM<=75):
    l='BB'
    gp=8
elif(RFM>=65 and RFM<=70):
    l='BC'
    gp=7
elif(RFM>=60 and RFM<=65):
    l='CC'
    gp=6
elif(RFM>=55 and RFM<=60):
    l='CD'
    gp=5
elif(RFM>=50 and RFM<=55):
    l='DD'
    gp=4
else:
    l='FF'
    gp=0
final_grade_points.append(gp)
letter_grade.append(l)
if(Py>=80):
    l='AA'
    gp=10
elif(Py>=75 and Py<=80):
    l='AB'
    gp=9
elif(Py>=70 and Py<=75):
    l='BB'
    gp=8
elif(Py>=65 and Py<=70):
    l='BC'
    gp=7
elif(Py>=60 and Py<=65):
    l='CC'
    gp=6
elif(Py>=55 and Py<=60):
    l='CD'
    gp=5
elif(Py>=50 and Py<=55):
    l='DD'
    gp=4
else:
    l='FF'
    gp=0
final_grade_points.append(gp)
letter_grade.append(l)
if(An>=80):
    l='AA'
    gp=10
elif(An>=75 and An<=80):
    l='AB'
    gp=9
elif(An>=70 and An<=75):
    l='BB'
    gp=8
elif(An>=65 and An<=70):
    l='BC'
    gp=7
elif(An>=60 and An<=65):
    l='CC'
    gp=6
elif(An>=55 and An<=60):
    l='CD'
    gp=5
elif(An>=50 and An<=55):
    l='DD'
    gp=4
else:
    l='FF'
    gp=0
final_grade_points.append(gp)
letter_grade.append(l)
if(MIC>=80):
    l='AA'
    gp=10
elif(MIC>=75 and MIC<=80):
    l='AB'
    gp=9
elif(MIC>=70 and MIC<=75):
    l='BB'
    gp=8
elif(MIC>=65 and MIC<=70):
    l='BC'
    gp=7
elif(MIC>=60 and MIC<=65):
    l='CC'
    gp=6
elif(MIC>=55 and MIC<=60):
    l='CD'
    gp=5
elif(MIC>=50 and MIC<=55):
    l='DD'
    gp=4
else:
    l='FF'
    gp=0

final_grade_points.append(gp)
letter_grade.append(l)
j=0
for i in final_grade_points:
    print('Grade point in {}'.format(Subject[j]),'is',i)
    j=j+1
q=0
for k in letter_grade:
    print('Letter grade in {}'.format(Subject[q]),'is',k)
    q=q+1
