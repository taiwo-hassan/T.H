.16
larger1=0
larger2=0
count = 0
while count<=9 :
    number=int(input("enter your numbers :  "))
    
    if count ==0 :
         larger1== number
         
    if larger1< number :
        larger1= number
    if number == larger1 :
        continue
    if count ==0 :
         larger2 = number
    
    if larger2 <number :
          larger2 = number
    count+=1
    
print(f"the first largest is {larger1},the second largest is {larger2}")





