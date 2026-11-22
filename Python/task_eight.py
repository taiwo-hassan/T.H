

sum=0
count=1
while (count<=10) :
    number=int(input("enter any  10 valid score between 0-100  :  "))

    if (0<=number and number<= 100) :
        sum+=number
        count+=1
    else :
        print("invalid, try again")
        
  
print(f"Sum = {sum}")




