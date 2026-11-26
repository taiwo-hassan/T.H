function isHappy(number) {
let sum=0;
while(number>=1) { 
let extract=number%10;
number=Math.floor(number/10);
add=extract+extract;
square=extract*extract;
sum+=square;
}
if (add>=10) { 
return "true"}
else if (sum>=10) {
return "false";}
else {
return "invalid";}
}


console.log( isHappy(19) );
