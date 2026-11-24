
sum_=0
count=1
counter=0

while(counter!=-1) :
    number=int(input("enter number to calculate average "))
    sum_+=number
    average= sum_/count
    print(average)
    count+=1
    counter=int(input("enter -1 to quit"))
 
