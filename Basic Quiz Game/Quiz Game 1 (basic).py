def quiz_game():

    count=0

    q1= "Who created Python? \n A)Jack Dorsey \n B) Guido Van Rossum \n C) Steve Jobs \n D) Dennis Ritchie"
    print(q1)

    while True: 
        ans1= input("Enter the solution (A/B/C/D): ").strip().lower()

        if ans1=='b':
            count+=1
            print("You are correct!")
            break

        elif ans1 in 'acd':
            print("You are wrong. The correct answer is B) Guido Van Rossum")
            break
        
        else:
            print("Please enter a valid answer (A/B/C/D)")



    q2= 'What is the output of len("Python")? \n A) 6  B) 7  C) 5  D) Error'
    print(q2)

    while True:

        ans2= input("Enter the solution (A/B/C/D): ").strip().lower()

        if ans2=='a':
            count+=1
            print("You are correct!")
            break

        elif ans2 in 'bcd':
            print("You are wrong. The correct answer is A) 6")
            break
        
        else:
            print("Please enter a valid answer (A/B/C/D)")


    q3= 'Which of the following is used to define a function in Python? \n A) func \n B)function \n C) def \n D) define'
    print(q3)

    while True:
        ans3= input("Enter the solution (A/B/C/D): ").strip().lower()

        if ans3=='c':
            count+=1
            print("You are correct!")
            break

        elif ans3 in 'abd':
            print("You are wrong. The correct answer is C) def")
            break
        
        else:
            print("Please enter a valid answer (A/B/C/D)")


    q4= 'Which data type is the result of input() by default in Python? \n A) str \n B)int \n C) bool \n D) float'
    print(q4)

    while True:
        ans4= input("Enter the solution (A/B/C/D): ").strip().lower()

        if ans4=='a':
            count+=1
            print("You are correct!")
            break

        elif ans4 in 'bcd':
            print("You are wrong. The correct answer is A) str")
            break
        
        else:
            print("Please enter a valid answer (A/B/C/D)")

    q5= 'What Symbol is used to comment a single line in Python? \n A) // \n B) <!-- \n C) # \n D) /* */'
    print(q5)

    while True:
        ans5= input("Enter the solution (A/B/C/D): ").strip().lower()

        if ans5=='c':
            count+=1
            print("You are correct!")
            break

        elif ans5 in 'abd':
            print("You are wrong. The correct answer is C) #")
            break
        
        else:
            print("Please enter a valid answer (A/B/C/D)")

    
    


    def grade():
        
        if count==5:
            return "Perfect"
        
        elif count==4:
            return "Great Job"

        elif count==3:
            return "Good, but could improve"

        elif count<=2:
            return "That was horrible. Try again"

    
    print(f'You have scored {count}/5. {grade()}')


#Again

while True:

    quiz_game()
    
    while True:

        again=input("Do you want to play again? (Yes/No): ").strip().lower()


        if again=='yes':
            break

        elif again=='no':
            print("Goodbye")
            exit()

        else:
            print("Please enter a valid value. (Yes/No)")


