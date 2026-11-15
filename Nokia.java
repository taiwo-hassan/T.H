import java.util.Scanner ;
public class Nokia {
public static void main(String[] args) {

Scanner phone = new Scanner(System.in);
System.out.println("Menu");
int menu=0;
if( menu < 1 ){
System.out.println("  \n  1. Phone Book \n 2.  Messages \n 3. Chats \n 4.Call register \n 5. Tones \n 6. Settings \n 7. Call Divert \n 8. Music \n 9. Games \n 10. Calculator \n 11. Reminders \n 12. Clocks \n 13. Profiles \n 14. Services \n 15. SIM sevices \n Enter from the above options  " ) ;
int number = phone.nextInt();

if (number >=1 || number <15) {
switch (number) {
case 1 :
System.out.println("Phone Book");
System.out.println("\n  1. Search \n 2.  Sevice No.s \n 3. Add name \n 3a. Erase\n 3b. Edit  \n 3c. Copy \n 3d. Assign tone  \n 3e. Send b'card \n 4.Memory in use \n 5. Type of view \n 6. Memory status \n 7. Speed Dials  \n 8. Voice tags \n Enter from the above options");

int phoneNumber = phone.nextInt();
switch(phoneNumber) {
case 1 : System.out.println("Search: Enter 1 for  saved numbers and 2 for names");
        String search = phone.next();
        System.out.println(search);

              break;
case 2 : System.out.println("Services Nos \n service provider number : ");
int voiceMail = 1111;
int spn=311;
int sos=911;
int emergency=112;
System.out.printf("voicemail = %d%nspn = %d%nsos = %d%n ",voiceMail, spn,sos,emergency);
          break;

case 3 : System.out.println("Add name");

String name = phone.next();
 String savedNumber= name;
System.out.println(name);
System.out.println("enter area code or country code");
String areaCode= phone.next();
char add = '+';
String code= add+ areaCode;
System.out.println("enter phone number");
String phoneNum= phone.next();
String phoneNumber1= code+ phoneNum;

System.out.println("phone number is "+  phoneNumber1);

   System.out.println("Enter 1 to Erase number \n 2. Edit number \n 3.Copy \n 4. Assign tone\n 5. Send b'card");
   int other= phone.nextInt();
   if (other ==1 ) {
String erase = " ";
phoneNumber1= erase ;
System.out.println("deleted");
}
    if (other ==3) {
String copied = " 0 ";
copied = phoneNumber1 ;
System.out.println("number copied"+ copied);
}

 if (other ==2) {System.out.println("Edit\n Enter new name");

String newName = phone.next();
newName = name ;

System.out.print("new Name  : "+ newName);

System.out.print("Press 1 to change number");
int  edit = phone.nextInt();
if (edit=='1') {System.out.println("Enter new number");
String newNumber = phone.next();

newNumber=phoneNumber1;
System.out.print("new Number : "+ newNumber); }
}


if (other==4) {System.out.println("Assign tone");
System.out.print("Select tone \n  1. Silent night \n 2. Starry stars \n3. perfect eyes \n4. from device " );

int tone = 0;
if (tone<=3 ){System.out.print("Done "); }
if (tone == 4) {System.out.print("Storage full"); 
}
}


if (other==5) {System.out.println("Send b'card");

{System.out.println("******************");

System.out.printf("Name : %s%nPhone number :%s%n ", name,phoneNumber1); 

System.out.println("*******************"); 
}
}
  break;
  case 4 : System.out.println("Memory in use"); 
  System.out.println("Choose memory to use \n 1. phone storage \n 2. SIM card"); 
  int memory = phone. nextInt();
  if (memory==1) { 
  System.out.println("Phone storage selected");}
  else if  (memory==2){ System.out.println("SIM card selected");}
  else { System.out.println("invalid selction");}

  
  break ;
  
  case 5 : System.out.println("Type of View"); 
  System.out.println("1. Display in vertical\n 2. Display in horizontal"); 
  int display= phone. nextInt();
   if (display==1) { 
  System.out.println("Change in progress...");}
  else if  (display==2){ System.out.println(" Change in progress...");}
  else { System.out.println("invalid selction");}


break;

 case 6: System.out.println("Memory Status "); 
  System.out.println("1. View phone memory Status\n 2. View SIM memory status"); 
int status= phone. nextInt();
 if (status==1) { 
  System.out.println("phone memory Status \n 0/10");}
  
 else if  (status==2){ System.out.println(" SIM memory status\n 0/500");}
  else { System.out.println("invalid selction");}

break ;


case 7 : { System.out.println("Speed dials"); 
{ System.out.println("assign phone number to 2-9") ;}
int speed= phone.nextInt();
if (speed>=2 || speed <= 9) { 
{ System.out.println(speed+ "is assigned to number");}
}
}

break;

case 8 : System.out.println("Voice tags "); 
System.out.println("Voice tag remaining 0/8 ");
       
System.out.println("press 1 to record voice tag \n 2. listen \n 3. change \n 4. delete");
int record_= phone.nextInt();
if (record_==1) {
System.out.println("Recording:- ....~.~.~.~.~.~.~....\n                                       ");}
else if (record_==4) {
System.out.println("Voice tag deleted");}

else if (record_==3) {
System.out.println("Change Voice tag ");
System.out.println("Recording:- ....~.~.~.~.~.~.~....\n                                       ");}

else if (record_==2) {
System.out.println("playing ....~.~.~.~.~.~.-0.5");}    
       }
       
       break; 

case 2 : System.out.println("Messages");
System.out.println("1.write and send Messages\n 2. Read Messages \n 3. view Saved Messsages \n 4. Picture messages \n  5. Messages setting\n Enter from above options ");
int message= phone.nextInt();
switch(message) {
case 1 : System.out.println("write and send Messages");
System.out.println("*****************");
System.out.println("Write message(click options to send)");
String writeMessage=phone.next();
System.out.println("Enter 1 for options or 0 to exit");
int option = phone.nextInt();
if( option==1){
System.out.println(" Options\n ******\n1. Send\n2. Template \n3. insert smilley\n4.Send by set\n5. Save\n 5. Erase\n Enter from above Options " ); } 
int subMenu = phone.nextInt();
switch(subMenu) {
case 1 : System.out.println(" Message sent ");
break;
case 2 : System.out.println(" Template");

       System.out.println("Select from template below");
       
      String temp= "hello how are you " ;
      String temp1= "i am close to home " ;
      String temp2= "Wait a minute\n who are you" ;
      String temp3= "Congratulations Man" ;
      
      System.out.printf(".temp : %s%n . temp1 : %s%n . temp2 :%s%n .temp3 : %s%n ",temp,temp1,temp2,temp3);
       String template = phone.next();
       
      break;
  case 3 : System.out.println("smilley inserted");
  break;
  
  case 4 :  System.out.println("Send by  set");
   System.out.println("Message centre number");
    System.out.println("2. Message sent as : \n E-mail\n Fax or paging");
     System.out.println("Message validity");
     break;
  case 5 :  System.out.println(" message Erased") ;
  break;
   }
    
 case 2 :  System.out.println("read message");
 break;
 case 3 :  System.out.println("Saved messages");
 break;
 case 4 :  System.out.println("Picture messages\n ni message");
 break;
 case 5 :  System.out.println("Message Settings");
 System.out.println("====Group settings=====\n ==========Common settings=======");
 break; 
 
 
 
 
 

}
case 3 : System.out.println("======Chat=======");
break;

case 4 : System.out.println("Call register");
System.out.println("Options \n1=====.Missed Calls=====\n2. ========Received Calls======\n 3.====== Dialled numbers=======\n4.=======Erase recent call list=======\n5.========= Show call durations========\n6.=======Call cost settings=========\n7.========Prepaid credits========== ");
 break;
 
 case 5 : System.out.println("========Tones========");
 

 System.out.println("========Messages alert Tones========");
 System.out.println("========Keypad Tones========");
 System.out.println("========Warning Tones========");
 System.out.println("========Vibrating alert========");
 
  System.out.println("========Vibrating alert========");
   System.out.println("========Screen Saver ========");
    System.out.println("========Ringing Tones========");
 
 System.out.println("Enter 1 to set Ringing volume");
 int volume= phone.nextInt();
 if (volume==1){
 System.out.println("======Volume increased=====");}
 System.out.println("========Incoming call alert========");
 System.out.println("Options\n 1. Off\n2. On");
 int alert=phone.nextInt();
 if (alert==1) {
 System.out.println("======== Call alert off========");}
 else if (alert==2) {System.out.println("========Call alert On========");}
 else 
  System.out.println("Invalid");
   break;
   
 case 6 : System.out.println("Settings");
 System.out.println("=======Call settings===\n1.Automatic redial\n2.speed dialing\n3.call waiting options\n4.Own number sending\n5.Phone line in use\n6.Automatic answer\n7.===Phone settings===\n8.Languages\n9.Cell info display\n10.Welcome note\n11.Network selection\n12.Confirm SIM service actions\n13.====Securty settings====\n14.PIN code request\n15.Call barring service\n16.Fixed dialing\n17.Closed user group\n18.Security level\n19.Change access codes\n20=======Restore factory settings====\n***Enter any of the above numbers to see options***");
 int setting= phone.nextInt();
 switch(setting) {case 2 : System.out.println("=====Speed dialling===\n Enter : 1. on \n2.off");
 int speed=phone.nextInt();
 if (speed==1){System.out.println("==ON==");}
 else if(speed==2){System.out.println("==OFF==");}
 break;
 case 1 :case 3 :case 4:case 5: case 6 : case 7 : case 8 : case 9 : case 10 : case 11 : case 12 : case 13 : case 14 : case 15 : case 16 : case 17 : case 18 : case 19 : 
 case 20 :System.out.print("loading..");
 break;
}
 break;
 case 7 : System.out.println("======Call divert======\n ****Options****\n1. Divert when busy\nSelect :\n 1 to Activate \n2. Cancel");
 int divert= phone.nextInt();
 if (divert==1) {
 System.out.println("Activated");}
 else if (divert==2) {System.out.println("Cancelled");}
 else 
 {System.out.println("Invalid");}
 break;
 
 case 8 : System.out.println("Music");   
 System.out.println("Enter :\n1. Music\n2. Radio\n3.Track list");
 int musicOption=phone.nextInt();
 if(musicOption==1){System.out.println("Turn music:\n1. On\n2.Off");
 int song=phone.nextInt();
 if(song==1) {System.out.println("****Music ON****");}
 else if (song==2) {System.out.println("****Music OFF****");}
 else {System.out.println("****INVALID****");} 
 }
 
 
 else if(musicOption==2){System.out.println("Turn Radio:\n1. On\n2.Off");
 int radio=phone.nextInt();
 if(radio==1) {System.out.println("****Radio ON****");}
 else if (radio==2) {System.out.println("****Radio OFF****");}
 else {System.out.println("****INVALID****");}
 }
 
 
 else if(musicOption==3){System.out.println("Check Track List" );}
 
 else 
 {System.out.println("Invalid"); }
 
  break;
  
  
  case 9 : System.out.println("======Games====");
  System.out.println("Play:\n1. Snake II\n2. Space Impact\n3. Batumi\n4. Pairs II\n5.Bumper\n 6. Game settings\nEnter number to see options"); 
  int game= phone.nextInt();
  switch(game) {
  case 1:case 2 : case 3 : case 4 : case 5 : System.out.println("***play***");
  break;
  case 6 : System.out.println("======Game Settings===="); System.out.println("1. Sounds\n2. light\nvibration(Shakes)");
  break;}
  break;
  
  case 10 : System.out.println("======Calculator====");
  System.out.println("Enter 1 to start calculating");
  int start= phone.nextInt();
  if (start==1) { 
   System.out.println("Enter first number to calclate  ");
 int number1= phone.nextInt();
  System.out.println("Enter second number to calclate");
  int number2= phone.nextInt();
  
  System.out.println("Enter operator");
  char operator = phone.next().charAt(0);
  switch(operator){
  case '+' : int sum = number1 + number2 ;
  System.out.println(sum);
  break;
  case'-' : int subtract = number1 - number2 ;
    System.out.println(subtract);
    break;
    case'*' : int multiply = number1 * number2 ;
           System.out.println(multiply);
           break;
  case'/' : int division = number1 / number2 ;
  System.out.println(division);
  default : 
  System.out.println("invalid");
  break;
  } 
  
  }
  
  case 11: System.out.println("====Reminder====");
  System.out.println("***Add New***\n***View all***");
  break;
  case 12  : System.out.println("====Clock====");
  System.out.println("1.Alarm clock\n2. Clock settings\n3.StopWatch\n4.Date setting\n5. Countdown timer\n6. Auto update of date and time ");
  break;
  case 13 : System.out.println("====Profiles===");
  System.out.println("1. Silent profile\n2. General profile");
  break;
  case 14 :
  System.out.println("===== WAP Services=====");
  System.out.println("1.Home\n2.BookMarks\n3.Settings\n4.Go to Address\n5. exit");
  break;
  case 15 : 
  System.out.println("======SIM services=====");
  System.out.println("Loading...");
  break;
  default :
  System.out.println("invalid");
  break;

}
}
}
}

}


