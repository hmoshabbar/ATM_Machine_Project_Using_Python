# Nested loops Program for a bank ATM:
import time
print "......................Welcome To SBI ATM....................."
restart=("Y")
chances=3
Account_balance=5000.00
while (chances>=0):
    PIN=int(input("Enter Your 4 Digit PIN:"))
    if PIN==(1234):
    #if PIN==(1234) or (1457):
        #if PIN==(1234):
            #print "Welcome To Moshabbar Hussain"
        #elif PIN==(1457):
            #print "Welcome To Irshad"
        print "You Entered PIN Number is correct please Wait"
        time.sleep(5)
        while restart not in ("N","n","NO","no"): # means restart is not in here making tuple
            print " "
            print "...Choose Your Option..."
            print "1)  BALANCE INQUERY"
            print "2)  CASH WIDTHDRAW"
            print "3)  MONEY TRANSFER"
            print "4)  MONEY DIPOSIT"
            print " "
            option=int(input("Enter Your option:"))
            if option==1:
                time.sleep(2)
                print " Your Account Balance is : ",Account_balance
                restart=raw_input("Would you like to go back:")
                if restart in ("NO","N","no","n"):
                    print "Thank You"
                    break

            elif option==2:
                option2=("Y")
                Widthdraw=float(input("Enter Your Widthraw Amount:"))
                if Widthdraw in [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000]:
                    balance=Account_balance-Widthdraw
                    print "Please wait your transaction is processing....."
                    time.sleep(2)
                    print " Please Collect Your Cash"
                    print " Your Account Balance is :",balance
                    restart=raw_input("Would you like to go back:")
                    if restart in ("NO","N","no","n"):
                        print "Thank You"
                        break
                elif  Widthdraw in [50,150,350,450,550,650,750,850,950,1050,2050,3050,4050,5050]:
                    print "Amount Is not Valid Please Enter Valid Amount"
                    Widthdraw=float(input("Enter Your Widthraw Amount again:"))
                    if Widthdraw in [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000]:
                        balance=Account_balance-Widthdraw
                        print "Please wait your transaction is processing....."
                        time.sleep(2)
                        print " Please Collect Your Cash"
                        print " Your Account Balance is :",balance
                        restart=raw_input("Would you like to go back:")
                        if restart in ("NO","N","no","n"):
                            print "Thank You"
                            break
                        
                        restart="Y"


            elif option==3:
                option3=("Y")
                Transfer=float(input("How Much you want To Transfer:"))
                balance=Account_balance-Transfer
                print "Please Wait Your Transaction is processing "
                time.sleep(2)
                print " Your Account Balance is :",balance
                if restart in ("NO","N","no","n"):
                    print "Thank You"
                    break
            elif option==4:
                Diposit=float(input("How much amount you want to Diposit :"))
                balance=Account_balance+Diposit
                print "please Wait you transctaion is processing....."
                time.sleep(2)
                print " Your Account Balance is :",balance
                if restart in ("NO","N","no","n"):
                    print "Thank You"
                    break

            else:
                print "Please Enter  a vaid pin Number"
                restart=("Y")
    elif PIN !=("1234"):
        print "Your Pin is incorrect"
        chances=chances-1
        if chances==0:
            print "oops ! no more tries"
            print "Blocked Your Account please Contact your Bank"
            
            break
                
                

                     
                
                
