import random

# Generating random number from 1 to 100
computer_input=random.randint(1,100)

# fixing the maximum attempts 
max_attempts=7

print("Welcome to Number Guessing Game :)")
print(f'You have a maximum attenpts :{max_attempts}')

# for Multiple attempts
for attempts in range(1,max_attempts+1):
    try:
        guess=int(input("Enter Your Guessing Number :"))
        if 1>guess or guess>100:
            print("Your Guess is Too High (or) Too Low")
            continue
        
        if guess==computer_input:
            print(f"Congratulation You Won !!!\n Your Number is {guess}")
            break
        elif guess>computer_input:
            print("Your Guess is too High..")
        else:
            print("Your Guess is Too Low..")
        
    except ValueError:
        print("Please Enter the Valid Number")
else:
    print("Your Attempts May Be Finished\n Better Luck Next Time")
