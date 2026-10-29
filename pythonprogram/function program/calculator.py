print("welcome to calculator")

def add(n1,n2):
    return n1+n2

def mul(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return(n1/n2)

while True:

 user_input=input("enter the operator that you want to perform   ")
 if user_input=="exit":
    print("thanks for using calculator")
    break

 num1=float(input("enter the first number"))
 num2=float(input("enter the second number"))

 if user_input=="add":
    print(f"addition is:{add(num1,num2)}")

 elif user_input=="sub":
    
    print(f"subtraction is:{sub(num1,num2)}")

 elif user_input=="mul":
    
    print(f"multipication is:{mul(num1,num2)}")

 elif user_input=="div":
    if num2==0:
       print("error:cannot be divided")

    else:
   
     print(f"division is:{div(num1,num2)}")
     
else:
   print("invalid choice")

