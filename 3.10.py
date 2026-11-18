.10
principal=1000
years =1
annual_rate=7/100
while years <=30 :
    amount_earned=principal*(1+annual_rate)**years
    print(f'amount earned in year {years} is {amount_earned : .2F}')
    years+=1
    print()
