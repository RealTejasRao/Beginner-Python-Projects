def calculator():

    while True: 
        try:
            num1= float(input("Enter first number: ").strip())
            break
        except ValueError:
            print("Enter a valid integer")

    while True:

        oper= input('Enter operator: ').strip().lower()

        if oper in ['+','-','*', '/', '**', '%', '//', 'sqrt']:
            break

        else:
            print("Enter a valid operator")
            

    if oper in ['+','-','*', '/', '**', '%', '//']:

        while True:
            try:
                num2= float(input("Enter second number: ").strip())
                break
            except:
                print("Enter a valid integer")

    if oper=='+':
        print(f'The sum is {num1+num2}')

    if oper=='-':
        print(f'The difference is {num1-num2}')

    if oper=='*':
        print(f'The product is {round(num1*num2,2)}')

    try:
        if oper=='/':
            print(f'The quotient is {round(num1/num2,2)}')
    
        if oper=='%':
            print(f'The remainder is {num1%num2}')

        if oper=='//':
            print(f"The GIF is {num1//num2}")

        
    
    except ZeroDivisionError:
        print("You cannot a divide a number by 0")

    if oper=='**':
            print("%s raised to the power %s is %s" %(num1, num2, num1**num2))
                  
    if oper=='sqrt':
            print(f'The square root of {num1} is {num1**0.5} ')


#Again

while True:

    calculator()

    while True:
        again= input("Do you wanna calculate again? (Yes/No): ").lower().strip()
        

        if again=='yes':
            break
        elif again=='no':
            print("Okay. Goodbye!")
            exit()
            
        else:
            print("Please enter Yes/No")

    
    