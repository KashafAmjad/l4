print("exam eligibility checker")
med=input("any medical cause for absentees?(yes/no):")
att=int(input("enter the attendance:"))
if med=="yes":
 print("you are eligible for exam")
else:
   if att>=75:
    print("you are eligible for exam")
   else:
     print("you are not eligible for exam")
