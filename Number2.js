prompt=require("prompt-sync")();
let sum=0, count=1,counter=0;

while(counter!=-1){
number=Number(prompt("enter number to calculate average "));
 sum+=number;

 let average= sum/count;
 console.log(average);
   count++;
counter=prompt("enter -1 to quit");
}

