prompt=require("prompt-sync");
 word =prompt("enter a word");
 letter=" ";
length= word.length();
console.log(length);
 count=0;
while (length>=1){
 alphabet=word.charAt(count);
letter=alphabet+letter;
length--;
count++;}
console.log(letter);}



