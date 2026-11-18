.9
number=int(input("enter a 5 digit numbers :   "))
count=1


while count<= 5 :
    digit = number % 10 
    print(digit)
    number//=10
   
    
    count+=1

