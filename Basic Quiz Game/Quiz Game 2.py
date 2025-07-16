def quiz(ques,options, correct):


    print(ques)
    print(options)
    
    ans= input('Answer: ').lower().strip()
    if ans==correct:
        print('you are correct')
        return 1

    else:
        print(f'you are wrong. correct ans is {correct}')
        return 0
    
    
def grade(score):
        
    if score==5:
        return "Perfect"
    
    elif score==4:
        return "Great Job"

    elif score==3:
        return "Good, but could improve"

    elif score<=2:
        return "That was horrible. Try again"
    
while True:

    score=0

    score+=quiz('Who created python?', 'A)Jack Dorsey \n B) Guido Van Rossum \n C) Steve Jobs \n D) Dennis Ritchie', 'b')
    score+=quiz('What is the output of len("Python")?', ' A) 6 \n B) 7 \n C) 5 \n D) Error', 'a')
    score+=quiz('Which of the following is used to define a function in Python?', 'A) func \n B)function \n C) def \n D) define','c')
    score+=quiz('Which data type is the result of input() by default in Python?', 'A) str \n B)int \n C) bool \n D) float', 'a')
    score+=quiz('What Symbol is used to comment a single line in Python?' ,'A) // \n B) <!-- \n C) # \n D) /* */', 'c')

    
    print(f'You have scored {score}/5. {grade(score)}')
    while True:

        again=input("Do you want to play again? (Yes/No): ").strip().lower()


        if again=='yes':
            break

        elif again=='no':
            print("Goodbye")
            exit()

        else:
            print("Please enter a valid value. (Yes/No)")

