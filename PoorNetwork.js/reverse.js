function reverse (number) {
let reverse=0
while(number>=1) {
digit=number%10
number=Math.floor(number/10)
reverse=reverse*10+digit;
}
return (Math.floor(reverse));

}






console.log(reverse (123))
