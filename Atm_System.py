import time as t
Present_amount= 2000
a = str(input("Pls enter your name: "))
# <<<<<<<<<< Code for current Time >>>>>>>>>>>>>
samay=t.strftime('%H:%M:%S')
time=int(t.strftime('%H'))
time1=int(t.strftime('%H'))
print("Time:",samay)
if time<12:
 print("Good Morning ",a,"!")
elif time>12 and time<18:
   print("Good Afternoon",a,'!')
elif time>18 and time<21:
   print("Good Evening",a,'!')
elif time>21 and time<24:
   print("Hello",a,'!')
# <<<<<<<<<<< Code For Atm Machine >>>>>>>>>>>>>>
message = """ 
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL."""
print(message)
task = int(input("Pls enter your option : "))
if task >=1 and task <=3:
    print("Welcome to our Virtual bank")
    if task ==1:
        print("Sir here is Your Current Balance: INR",Present_amount)
        if time1>21 and time1<24:
          print('Good Night',a,"And Take Care !")
    elif task ==2:
        print("Enter Your Amount")
        amount=int(input())
        if amount <500:
         print("Sir you Need to deposit More than: 500")
        else:
         print("Thank You !! Sir Your Amoumt has been Deposited")
         print("Sir here is Your Current balanace",Present_amount + amount)
         if time>21 and time<24:
           print('Good Night',a,"And Take Care !")
    elif task ==3:
        print("Enter Your Amount")
        withdrawl=int(input())
        if withdrawl < Present_amount:
           print("Thank you Sir!","Here is Your current balance", Present_amount - withdrawl)
        else:
           print("Insufficiant Balance","Transction Fail!")
           if time>21 and time<24:
            print('Good Night',a,"And Take Care !")
else:
    print("Pls enter the no 1 to 3 !")
