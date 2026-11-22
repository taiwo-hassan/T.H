
sum_=0
count=1
while (count<=10) :
    number=int(input("enter any  10 valid score between 0-100  :  "))

    if (number>=0) :
        sum_+=number
    else :
        print("invalid")
        
    count+=1
print(f"Sum = {sum_}")



