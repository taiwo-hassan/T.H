prompt=require("prompt-sync")();
digit=prompt("enter any 3 digit number");
let count=0;
let sum=0;
let compare=digit;
while(digit>=1){
let separate=digit%10;
digit/=10;
let square=separate*separate;
sum+=square;
count++;}

if (sum==compare){
console.log("sum of digit is equal to number");
}
else{console.log("it is not"); }







