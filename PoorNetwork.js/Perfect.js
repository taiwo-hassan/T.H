function checkPerfectNumber(number) {  
let count=1;
let sum=0;
while(count< number)  {
if (number%count==0) {
sum+=count;}
return sum;
count++,

}




console.log(checkPerfectNumber(28))
