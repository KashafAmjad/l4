def add(P, Q):
    return P+Q
def substract (P,Q):
    return P-Q

print("Please select the operation.")
print("a. Add")
print("b. Substract")

choice=input("Please enter your choice(a/b):")
num_1= int(input("Please enter the first number:"))
num_2= int(input("Please enter the second number:"))
if choice=='a':
 print (num_1, " + ", num_2, " = ", add(num_1, num_2))
elif choice=='b':
    print (num_1, " - ", num_2, " = ", substract(num_1, num_2))
else:
          print ("invalid input")




    