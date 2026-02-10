h=float(input("Enter hight in meters:"))
w=int(input("Enter weight in kg:"))
bmi=w/(h*h)
print("BMI is:",bmi)
if bmi<18.5:
    print("person in underweight") 
elif bmi>=18 and bmi<25:
     print("person have normal weight")    
elif bmi>=25 and bmi<30:  
     print("person is overweight")
else:
     print("person is obese")
