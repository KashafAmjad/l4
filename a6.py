word=input("Enter any string:")
char=input("Enter any character")
i=0
count=0
while(i < len(word)):
     if(word[i]==char):
          count = count + 1
     i=i+1

print("above character has occured: ",count,"times")
