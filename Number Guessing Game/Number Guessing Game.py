import random


def number_game():


    num= random.randint(1,100)
    
    attempts=0
    
    while True:

        try:
            n= int(input("Enter an integer from 1 to 100: "))
            attempts+=1
            

            if num==n:
                print("Congrats! You successfully guessed the number. Total attempts=", attempts)
                break

            elif n>100 or n<1:
                print("Please enter a valid integer from 1 to 100")

            elif num>n:
                print("Enter a larger number")

            elif num<n:
                print("Enter a smaller number")

        except:
            print("Please enter a valid integer from 1 to 100")





while True:

    number_game()

    while True:
        again= input("Do you want to play again? (Yes/No): ").strip().lower()
        

        if again=='yes':
            break

        if again=='no':
            print("Goodbye. Thanks for playing.")
            exit()

        else:
            print("Enter Yes/No")


