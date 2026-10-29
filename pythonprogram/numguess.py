print("enter to the number guessing game")
import random
computer_choice=random.randint(1,100)
print("computer has choice the number, choose the number")


attemt=0
while attemt<6:

 user_choice=int(input("enter the user choice between 1-100 "))
 attemt=attemt+1
 print("your attempt is ",attemt)

 if user_choice>computer_choice:
   print("guess lower number")

 elif user_choice<computer_choice:
   print("guess higher number")

 else:
   print("your choice is correct you win the game")
   break


print("you lose the game")
