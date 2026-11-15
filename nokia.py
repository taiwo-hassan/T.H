



print("==========Menu=========")
menu=0;
if( menu < 1 ):
        print(''' \n  1. Phone Book \n 2.  Messages \n 3. Chats \n 4.Call register \n 5. Tones \n 6. Settings \n 7. Call Divert \n 8. Music \n 9. Games \n 10. Calculator \n 11. 
        Reminders \n 12. Clocks \n 13. Profiles \n 14. Services \n 15. SIM sevices  ''' ) 


number = int(input("Enter from the above options :  "))

if (number >=1 or number < 15) :
    match (number) :
        case 1 :
            print("Phone Book");
            print('''\n  1. Search \n 2.  Sevice No.s \n 3. Add name \n 3a. Erase\n 3b. Edit  \n 3c. Copy \n 3d. Assign tone  \n 3e. Send b'card \n 4.Memory in use \n 5.  
            Type of view \n 6. Memory status \n 7. Speed Dials  \n 8. Voice tags ''')
            phone_number = int(input("Enter from the above options  : "))
            match(phone_number) :
                case 1 :search = int(input ("Search: Enter 1 for  saved numbers and 2 for names :   "))
                            
                  
                case 2 : 
                        print("Services Nos \n service provider number : ")
                        voiceMail = 1111
                        spn=311
                        sos=911
                        emergency=112
                        print(f"voicemail ={voiceMail}\n spn = {spn}\n sos= {sos}\n Emergency ={ emergency}")
                    


                case 3 : 
                        name=input("Add name")
                        savedNumber= name
                        print(name)
                        areaCode=input("enter area code or country code")
                        
                        add = '+'
                        code= add+ areaCode
                        phoneNum=input("enter phone number")
                
                        phoneNumber1= code + phoneNum

                        print("phone number is ", phoneNumber1)

                        other=int(input("Enter 1 to Erase number \n 2. Edit number \n 3.Copy \n 4. Assign tone\n 5. Send b'card"))

                        if (other ==1 ) :
                                erase = " "
                                phoneNumber1= erase 
                                print("deleted")

                        if (other ==3) :
                             copied = " 0 "
                             copied = phoneNumber1 
                             print("number copied",copied)


                        if (other ==2) :
                                        newName=input("Edit\n Enter new name")

                                        newName = name
                                        print("new Name  : ",newName)

                                        edit =int(input("Press 1 to change number"))

                                        if (edit=='1') :
                                                     newNumber = ("Enter new number")
                                                     newNumber=phoneNumber1
                                                     
                                                     print("new Number : ",newNumber)

                        if (other==4) : 
                                                print("Assign tone")
                                                print("Select tone \n  1. Silent night \n 2. Starry stars \n3. perfect eyes \n4. from device " )

                                                tone = 0
                                                
                                                if (tone<=3 ) :
                                                     print("Done ")
                                                if (tone == 4) : 
                                                      print("Storage full")

                        if (other==5) :
                                    print("Send b'card")
                                    
                                    print("******************")

                                    print(f"Name :  {name}\nPhone number :{phone_number} ")

                                    print("*******************")



                case 4 : 
                    print("Memory in use")
                    memory =int(input("Choose memory to use \n 1. phone storage \n 2. SIM card"))
                    if (memory==1) :
                        print("Phone storage selected")
                    elif (memory==2):
                        print("SIM card selected")
                    else :
                        print("invalid selction")


                case 5 :    
                    print("Type of View")
                    display=int(input("1. Display in vertical\n 2. Display in horizontal"))

                    if (display==1) : 
                        println("Change in progress...")
                    elif (display==2) :
                            print(" Change in progress...")
                    else :
                        print("invalid selction")

                case 6: 
                    print("Memory Status ")
                    status=int(input("1. View phone memory Status\n 2. View SIM memory status"))

                    if (status==1) :
                            print("phone memory Status \n 0/10")
                    elif  (status==2):
                             print(" SIM memory status\n 0/500")
                    else :
                            print("invalid selction")

                case 7 :
                    print("Speed dials")
                    speed=int(input("assign phone number to 2-9") )

                    if (speed>=2 or speed <= 9) :
                        print(speed, "is assigned to number")

                case 8 : 
                    print("Voice tags ")
                    print("Voice tag remaining 0/8 ")
                    record_= int(input("press 1 to record voice tag \n 2. listen \n 3. change \n 4. delete"))
                    if (record_==1) :
                        print("Recording:- ....~.~.~.~.~.~.~....\n                                       ")
                    elif (record_==4) :
                        print("Voice tag deleted")
                    elif (record_==3) :
                        print("Change Voice tag ")
                        print("Recording:- ....~.~.~.~.~.~.~....\n                                       ")
                    elif (record_==2) :
                            println("playing ....~.~.~.~.~.~.-0.5") 

        case 2 :
            print("Messages")
            message= int(input("1.write and send Messages\n 2. Read Messages \n 3. view Saved Messsages \n 4. Picture messages \n  5. Messages setting\n Enter from above options "))
            match(message) :
                case 1 :
                    print("write and send Messages")
                    print("*****************")
                    writeMessage=input("Write message(click options to send")
                    option =int(input("Enter 1 for options or 0 to exit"))
                    if( option==1) : 
                        print(" Options\n ******\n1. Send\n2. Template \n3. insert smilley\n4.Send by set\n5. Save\n 5. Erase\n Enter from above Options " )
                        sub_menu = int(input("Enter from above Options"))
                        match(sub_menu) :
                            case 1 : print(" Message sent ")
                            case 2 : 
                                print(" Template")
                                print("Select from template below")
                                temp= "hello how are you " 
                                temp1= "i am close to home " 
                                temp2= "Wait a minute\n who are you" 
                                temp3= "Congratulations Man" 
                                template=input(f"temp : {temp}\n temp1 : {temp1}\ntemp2 :{temp2}\n temp3 :{temp3} :  ")


                            case 3 : print("smilley inserted")
                            case 4 :   
                                print("Send by  set")
                                print("Message centre number")
                                print("2. Message sent as : \n E-mail\n Fax or paging")
                                print("Message validity")
                            case 5 : print(" message Erased") 
                case 2 :  print("read message")
                case 3 :  print("Saved messages")
                case 4 :  print("Picture messages\n  message")
                case 5 :  
                          print("Message Settings")
                          print("====Group settings=====\n ==========Common settings=======")

        case 3 : print("======Chat=======")
        case 4 :
                 print("Call register")
                 print('''Options \n1=====.Missed Calls=====\n2. ========Received Calls======\n 3.====== Dialled numbers=======\n4.=======Erase recent call list=======\n5.========= 
                 Show call durations========\n6.=======Call cost settings=========\n7.========Prepaid credits========== ''')
        case 5 : 
            print("========Tones========")
            print("========Messages alert Tones========")
            print("========Keypad Tones========")
            print("========Warning Tones========")
            print("========Vibrating alert========")
            print("========Vibrating alert========")
            print("========Screen Saver ========")
            print("========Ringing Tones========")
            volume= int(input("Enter 1 to set Ringing volume"))
            if (volume==1) :
                print("======Volume increased=====")
            print("========Incoming call alert========")
            alert=int(input("Options\n 1. Off\n2. On"))
            if (alert==1) :
                    print("======== Call alert off========")
            elif(alert==2) :
                        print("========Call alert On========")
            else :
                        print("Invalid")

        case 6 : 
                 print("Settings")
                 print('''=======Call settings===\n1.Automatic redial\n2.speed dialing\n3.call waiting options\n4.Own number sending\n5.Phone line in use\n6.Automatic    
                 answer\n7.===Phone settings===\n8.Languages\n9.Cell info display\n10.Welcome note\n11.Network selection\n12.Confirm SIM service actions\n13.====Securty 
                 Settings====\n14.PIN code request\n15.Call barring service\n16.Fixed dialing\n17.Closed user group\n18.Security level\n19.Change access codes\n20=======Restore 
                 factory settings====''');
                 setting= int(input("***Enter any of the above numbers to see options***"))
                 match(setting) :
                        case 2 : 
                                 speed=int(input("=====Speed dialling===\n Enter : 1. on \n2.off"))
                                 if (speed==1) :
                                        print("==ON==")
                                 elif(speed==2):
                                        print("==OFF==")
                        case 1 |3 | 4|5| 6 | 7 |  8 | 9 | 10 |  11 | 12 |  13| 14 |  15 | 16 | 17 | 18 | 19| 20 :print("loading..")

        case 7 : 
             divert=int(input("======Call divert======\n ****Options****\n1. Divert when busy\nSelect :\n 1 to Activate \n2. Cancel"))
             if (divert==1) :
                    print("Activated")
             elif (divert==2) :
                    print("Cancelled")
             else :
                print("Invalid")

        case 8 : 
                print("Music")  
                musicOption=int(input("Enter :\n1. Music\n2. Radio\n3.Track list"))
                if(musicOption==1):
                        song=int(input("Turn music:\n1. On\n2.Off"))    

                        if(song==1) :
                             print("****Music ON****")
                        elif (song==2) :
                             print("****Music OFF****")
                        else :
                                print("invalid")
                elif(musicOption==2):
                         radio=int(input("Turn Radio:\n1. On\n2.Off"))
                         if(radio==1) :
                                print("****Radio ON****")
                         elif (radio==2) :
                                print("****Radio OFF****")
                         else :
                             print("****INVALID****")
                elif (musicOption==3) :
                        print("Check Track List" )
                else :
                    print("Invalid")
        case 9 :   
                        print("======Games====")
                        game= int(input("Play:\n1. Snake II\n2. Space Impact\n3. Batumi\n4. Pairs II\n5.Bumper\n 6. Game settings"))
                        match(game) :
                             case 1|2|3|4|5:print("***play***")
                             case 6 :
                                    print("======Game Settings===="); System.out.println("1. Sounds\n2. light\nvibration(Shakes)")

        case 10 : 
             print("======Calculator====")
             start= int(input("Enter 1 to start calculating"))
             if (start==1) :
                number1=int(input("Enter first number to calclate  "))
                number2=int(input("Enter second number to calclate"))
                operator =input("Enter operator")
                match(operator):
                    case '+' : 
                            sum_ = number1 + number2 
                            print(sum_)
                    case'-' :
                            subtract = number1 - number2 
                            print(subtract)
                    case'*' :
                             multiply = number1 * number2 
                             print(multiply)
                    case'/' : 
                            division = number1 / number2 
                            print(division)
                    case _: 
                            print("invalid")

        case 11: 
                print("====Reminder====")
                print("***Add New***\n***View all***")
        case 12  : 
                print("====Clock====")
                print("1.Alarm clock\n2. Clock settings\n3.StopWatch\n4.Date setting\n5. Countdown timer\n6. Auto update of date and time ")
        case 13 :
                print("====Profiles===")
                print("1. Silent profile\n2. General profile")
        case 14 :
            print("===== WAP Services=====")
            print("1.Home\n2.BookMarks\n3.Settings\n4.Go to Address\n5. exit")
        case 15 : 
                print("======SIM services=====")
                print("Loading...")
        case _ :
            print("invalid")

