print("select your ride:")
print("1.bike")
print("2.car")
choice=int(input("enter your choice:"))
if choice==1:
    print("you selected bike")
    print("1.scooty")
    print("1.motorcycle")
    choice2=int(input("enter your choice 2:"))  
    if choice2==1:
        print("you have selected scooty.you have paid 50$ per hours")
    else:
       print("you have selected motorcycle.you have paid 60$ per hours") 
elif(choice==2) :
    print("what type of car?")
    print("1.sedan")
    print("2.XUV")
    choice2=int(input("enter your choice 3:"))  
    if choice2==1:
     print("you have selected sedan.you have paid 100$ per hours")
    else:
      print("you have selected XUV.you have paid 120$ per hours")   
else: 
  print("wrong choice!")     



