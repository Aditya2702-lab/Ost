import random
number=random.randint(1,100)
guess=0
count=10
print("***** Guess The Number Game *****")
while(count>0):

    count-=1
    guess+=1
    try:
        a=int(input("Guess the number : "))
        if type(a)==int:

            if(a==number):
                print(f"You guessed the number {number} in {guess} guesses !")
                break
            elif(a>number):
                print("guess lower number!")
            else:
                print("guess higher number! ")
            print(f"You have {count} guesses remaining!")
        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
    except ValueError  :
        print("Invalid input!, Please enter numbers/integers only")
        count+=1

if count==0:
    print("Sorry!, you have exhausted maxixmum no of guesses.")
    print(f"The actual number is '{number}'.")
        
    

