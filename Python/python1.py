
number=int(input("enter any 3 digit number"))
count=0
sum_=0
compare=number
while(number>=1):
    separate=number%10;
    number/=10
    square=separate*separate
    sum_+=square
    count+=1

if (sum==compare) :
    print("sum of digit is equal to number")

else:
   print("it is not")





