
try:
    number=int(input("Enter the number:"))
    print("the number enter is",number)

except ValueError as e:
    print("exception:",e)
