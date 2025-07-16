import random

def game():
    grp= ['rock', 'paper', 'scissors']

    while True:
        try:
            i= int(input("How many rounds do you want to play? (Max 5): ").strip())

            if i>5 or i<1:
                print("Please enter a valid integer from 1 to 5")

            else:
                break

        except ValueError:
            print("Please enter a valid integer from 1 to 5")

    count=0
    win=0
    lose=0

    while True:
        bot= random.choice(grp)

        while True:

            human= input("Choose Rock, Paper or Scissors: ").strip().lower()

            if human not in grp:
                print("Please enter a valid value (Rock/Paper/Scissors)")

            else:
                break

        count+=1

        print(f'I chose {bot}')

        if bot==human:
            print("It is a Tie")

        if bot=='rock' and human=='paper':
            print("You won. Congrats!")
            win+=1
        
        if bot=='rock' and human=='scissors':
            print("You lost.")
            lose+=1
        
        if bot=='paper' and human=='scissors':
            print("You won. Congrats!")
            win+=1
        
        if bot=='paper' and human=='rock':
            print("You lost")
            lose+=1
        
        if bot=='scissors' and human=='paper':
            print("You lost")
            lose+=1
        
        if bot=='scissors' and human=='rock':
            print("You won. Congrats!")
            win+=1

        if count==i:

            print(f'All rounds have ended. You won {win} round(s) and lost {lose} round(s)')

            if win>lose:
                print("You won in the end. Good game.")

            if win<lose:
                print("You lost in the end. Good effort.")
            break


while True:
    game()

    while True:
        again= input('Do you want to play again? (Yes/No):').lower().strip()

        if again=='yes':
            break
        elif again=='no':
            print("Okay. Goodbye!")
            exit()
            
        else:
            print("Please enter Yes/No")
        
    

