#rock paper seccors
import random
n=int(input("Enter Number of games You want to play : "))
count=0
tie=0
invalid=0
l=["Rock 🪨","Paper 📄", "✂ Scissors"]
for val in range(n):
   user_choice=int(input("Enter a value :0 for rock ,1 for paper ,2 for seccors : "))
   if user_choice<=2 and user_choice>=0:
        print("YOU      :", l[user_choice])
        computer_choice=random.randint(0,2)
        print("COMPUTER :",l[computer_choice])
        if user_choice in range(0,3):
            if user_choice==computer_choice :
                print("Tie")
                tie+=1
            elif computer_choice==0 and user_choice==2:
                print("You Loss")
            elif computer_choice==2 and user_choice==0:
                print("You Win")
                count+=1
            elif user_choice>computer_choice:
                print("You Win")
                count+=1
            elif user_choice<computer_choice:
                print("You Loss")
   else:
        print("Please enter a valid number")
        invalid+=1
print("Number of games Played",n)
print("Number of games You Won  :",count)
print("Number ganes TIED        :",tie)
print("number of invalid number :",invalid)
    
