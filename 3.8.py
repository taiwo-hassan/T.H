3.8
digit=0
count=1
product=1
number1=1
number2=0

while count <=4:
    number=int(input("enter your digit : ")) 
    
    
    
    
    if  count== 1:

             number1= number

             number2= number

    if number1 > number :
            number1= number
                


    
    if   number2< number :
            number2= number
                 
        
    
    product*=number
    digit+=number
    
    average=digit/count
    count+=1
    
   
print(f"total sum is {digit},product = {product}, average = {average}, smallest is {number1}, largest is {number2}")






