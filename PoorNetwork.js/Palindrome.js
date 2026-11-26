function IsPalindromeNumber (number) {
let reverse=0
let compare=number;
while(number>=1) {
digit=number%10
number=Math.floor(number/10)
reverse=reverse*10+digit
}
if (compare==reverse) {
return "true"}
else {return "false"}

}






console.log(IsPalindromeNumber(222))
