
count=1
sum=0
while count<=10 :
    number=int(input("enter numbers to get sum  : "))
    if count%2==0:
        sum +=number
    count+=1
print("your total sum is",sum)
