function weight (number) {
let sum=0
while(number>=1) {
let binary= number%2
 sum+=binary ;
 Math.floor(number);
 Math.floor(number/=2);}
return sum
}


console.log(weight (41))
