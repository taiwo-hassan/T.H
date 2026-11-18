3.14
pie=0
numerator=4
sum =0
for number in range(1,12,2) :
      
       pie = numerator/number  
       if pie %2 == 0:
            sum += numerator/number
       else :
            sum-= numerator/number  

print(sum)

