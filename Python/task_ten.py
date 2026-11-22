counter=0
sum_=0
count=1
while (count<=10) :
    number=int(input("enter any  10 valid score between 0-100  :  "))

    if (number>=0) :
        sum_+=number
        counter+=1
    else :
        print("invalid")
        
    count+=1
average= sum_/counter
print(f"average= {average}")
