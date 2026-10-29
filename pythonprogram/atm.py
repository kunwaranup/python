print("welcome to the atm")
balance=10000
pin=1234

print("insert the atm card")
user_pin=int(input("enter your pin"))
if user_pin==pin:
    print("press 1 for balance check")
    print("press 2 for cash withdraw")
    print("press 3 for deposite")
    print("press 4 for exit")

    user_press=int(input("enter the press  value"))
    if user_press==1:
        print(f"your balance is {balance}")

    elif user_press==2:
        withdraw=int(input("enter the withdraw amount"))

        if withdraw<=balance:
            balance=balance-withdraw
            print("withdraw is sucessful")
            print(f"your withdraw amount is {withdraw}")
            print(f"your remaning balance is {balance}")

    elif user_press==3:
        deposite=int(input("input enter the deposite amount"))
        balance=balance+deposite
        print(f"you have deposite{deposite}and your new balance is{balance}")

    else:
        print("exit from atm")
        



else:
    print("pin is invalid")
     