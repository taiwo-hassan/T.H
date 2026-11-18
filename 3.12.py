3.12
number=int(input("enter a 5 digit numbers :   "))
count=1
upside=0
porse= number
while count<= 5 :
   
    digit = number % 10 
    print(digit)
    number//=10
    
    upside= (upside*10)+ digit
    
    count+=1
print(upside)
if upside== porse :
        print("the number is a pallindrome")

else:
     print("it is not a pallindrome")



