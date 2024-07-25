import time as t
present_amount = 2000
name = input("Please enter your name: ")

# Get current time
current_time = t.strftime('%H:%M:%S')
hour = int(t.strftime('%H'))

# Print greeting based on time
if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
elif hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Hello"

print("Time:", current_time)
print(f"{greeting}, {name}!")

# ATM Machine Logic
message = """
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL."""
print(message)
task = int(input("Please enter your option: "))

if task >= 1 and task <= 3:
    print("Welcome to our Virtual bank")
    if task == 1:
        print("Sir here is Your Current Balance: INR", present_amount)
    elif task == 2:
        amount = int(input("Enter Your Amount: "))
        if amount < 500:
            print("Sir you Need to deposit More than: 500")
        else:
            print("Thank You !! Sir Your Amount has been Deposited")
            present_amount += amount
            print("Sir here is Your Current balance", present_amount)
    elif task == 3:
        withdrawl = int(input("Enter Your Amount: "))
        if withdrawl < present_amount:
            print("Thank you Sir!", "Here is Your current balance", present_amount - withdrawl)
            present_amount -= withdrawl
        else:
            print("Insufficient Balance", "Transaction Fail!")

    if hour > 21:
        print('Good Night', name, "And Take Care !")
else:
    print("Please enter a number between 1 and 3!")