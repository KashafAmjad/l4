num=5
if num==0:
  print(0)
binery_number=""
while num>0:
        binery_number=str(num % 2)+binery_number
        num=num//2 
print(binery_number)