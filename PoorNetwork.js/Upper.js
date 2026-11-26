function countPrimes(number)   { 
let count=2;
let digit=1;
while(count<=number)  { 
if (number%count!=0 && count%2!=0) {   
digit++;
}
count++;}
return digit;
}


console.log(countPrimes(5) )

