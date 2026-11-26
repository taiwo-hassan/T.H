function weight (number) {
let sum=0
while(number>=1) {
let binary= number%2
sum+=binary;
 
number= Math.floor(number/2);}
return Math.floor(sum)
}


console.log(weight (11))
