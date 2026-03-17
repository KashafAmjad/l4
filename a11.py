try:
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    result=num1 / num2
    print("result is",result)

except ZeroDivisionError:
    print("Division by zero is error!!")

except SyntaxError:
    print("wrong input")

else:
    print("no exception")

finally:
    print("This will excecute no matter what")
