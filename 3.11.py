3.11
gasoline= int(input("enter the gasoline used or -1 to exit  "))
total_miles=0
total_gasoline=0
while gasoline!= -1 :
    miles_travelled= int(input("enter the miles travelled  "))
    gasoline= int(input("enter the gasoline used or -1 to exit   "))
    total_miles+=miles_travelled
    total_gasoline+= gasoline
    
total_mpg=total_miles/ total_gasoline
print(f"the overall miles/gallon used was {total_mpg}")

