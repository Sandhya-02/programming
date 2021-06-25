
#! oka pillodu unnadu exam raasadu marks occhaay
#! we're creating a system
#! that pillodu will enter his marks as input 
#! and his grade will be shown in the output

#* 80 - 100 you got A+
#* 70 - 80 you got A grade
#* 50 - 70 you got B grade
#* 30 - 50 you got c grade
#* less than 30 fail
marks = int(input("enter the marks" ))
if(marks >=80 and marks <100):
     print("you got A+ grade")
elif(marks >= 70 and marks <80):
     print("you got A grade")
elif (marks>=50 and marks <70):
     print("you got B grade")
elif (marks>=30 and marks <50):
     print("you got C grade")
else:
     print("you failed")



