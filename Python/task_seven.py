counter=0
count=1
sum=0
while count<=10 :
    number=int(input("enter numbers to get sum  : "))
    if number%2==0:
        sum +=number
        counter+=1
    
    count+=1
average= sum/counter  
print(f"your total sum is {sum} \n average = {average}")
