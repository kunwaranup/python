print("Welcome to the Rock, Paper, Scissors game!")
import random
list1=["rock", "paper", "scissors"]
computer_choice=random.choice(list1)
print(computer_choice)
user_choice=input("Enter your choice (rock, paper, scissors): ").lower()

if(user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
    print("user wins")

elif(user_choice=="scissors" and computer_choice=="rock") or (user_choice=="rock" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="scissors"):
    print("computer wins")
else:
    print("it's a tie")