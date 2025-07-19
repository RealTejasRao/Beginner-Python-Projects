import colorama
from colorama import Fore, Back,Style
colorama.init(autoreset=True)
import string
import random
import time
import playsound
from playsound import playsound
import threading

class Account:

    def __init__(self):
        

        print(f'{Style.BRIGHT}Please create a bank account. Enter a Username and Password.')
        user= input("Please Enter a Username: ").strip()
        grp1, grp2, grp3, grp4= string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits

        while True:

            valid=True
            password= input("Please choose a password: ").strip()
            

            if not any(i in grp1 for i in password):
                print(f"{Fore.RED}{Style.BRIGHT}Password must contain at least one small letter. Try again.")
                valid= False

            if not any(i in grp2 for i in password):
                print(f"{Fore.RED}{Style.BRIGHT}Password must contain at least one capital letter. Try again.")
                valid= False

            if not any(i in grp3 for i in password):
                print(f"{Fore.RED}{Style.BRIGHT}Password must contain at least one special character. Try again.")
                valid= False

            if not any(i in grp4 for i in password):
                print(f"{Fore.RED}{Style.BRIGHT}Password must contain at least one number. Try again.")
                valid= False

            if valid:

                print(f'{Fore.GREEN}You have successfully signed up. Your username is {Fore.BLUE}{Style.BRIGHT}{user}{Style.RESET_ALL}{Fore.GREEN} and your password is {Fore.BLUE}{Style.BRIGHT}{password}.{Style.RESET_ALL}{Fore.GREEN} Please keep them in mind.')
                break
        
    
        grp4= string.digits
        num= random.choices(grp4, k=11)
        num2= "".join(num)
        print("Account number is being generated...")
        time.sleep(8)
        print(f'Your account number is {Fore.BLUE}{Style.BRIGHT}{num2}')
        time.sleep(3)

        self.user=user
        self.num2=num2
        self.password=password

    def login(self):
        
        print(f'{Style.BRIGHT}Please enter your login credentials to login.')

        attempts1=4

        while True:

        
            attempts1-=1

            if attempts1==0:
                print(f"{Fore.RED}{Style.BRIGHT}All attempts failed. Try again later.")
                exit()

            print(f'{Fore.RED}{attempts1} Attempts Left')
            log1= input("Enter your account number: ").strip()
            
            if log1==self.num2:
                break

            else:
                print("Account number invalid. Please try again")

        attempts2=4
        while True:
            
            attempts2-=1
            if attempts2==0:
                print("All attempts failed. Try again later.")
                exit()

            print(f'{Fore.RED}{attempts2} Attempts Left')
            log2= input("Enter account password: ").strip()

            if log2==self.password:
                break

            else:
                print("Password did not match. Try again.")

        def sound1():
            playsound("Success.wav")
            
        print(f"{Fore.GREEN}{Style.BRIGHT}You have successfully logged in. Welcome{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT} {self.user}")
        t1= threading.Thread(target=sound1)
        t1.start()

    
    def transaction(self):
    

        while True:

            try:
                initial= int(input("Enter amount in dollars to deposit into your brand new account: ").strip())

                if initial>0:
                    break

                elif initial<0:
                    print("Invalid input. Enter a positive number.")
            
            except ValueError:

                print("Invalid input. Please enter a positive number.")

            
        
        def sound2():
            playsound("Sound.mp3")

        t2= threading.Thread(target=sound2)
        t2.start()
        print(f"{Fore.GREEN}{Style.BRIGHT}Congratulations! Your account has been credited with $50 as New-User Bonus!")
        time.sleep(6)
        print(f'{Fore.BLUE}{Style.BRIGHT}{self.user}{Style.RESET_ALL} Total account balance is {Fore.BLUE}{Style.BRIGHT}{50+initial}.')

        self.bal= 50+initial

        while True:
            while True:

                act= input("Please select an action to perform (View/Deposit/Transfer/Delete/Exit): ").lower().strip()

                actions= ['view', 'deposit', 'transfer', 'delete', 'exit']

                if act not in actions:
                    print(f'{Fore.RED}{Style.BRIGHT}Please select a valid action (View/Deposit/Transfer/Delete/Exit)')

                else:
                    break

            if act=='view':
                print(f" Hello{Fore.BLUE}{Style.BRIGHT} {self.user}{Style.RESET_ALL}, A/c No. {Fore.BLUE}{Style.BRIGHT}{self.num2} ")
                print(f'Total Balance: {Style.BRIGHT}${self.bal}')
                time.sleep(3)

            elif act=='deposit':

                while True:

                    try:

                        dep= int(input("Enter the amount you want to deposit in your account: "))

                        if dep<=0:
                            print("Amount needs to be greater than 0. Try again.")

                        elif dep>0:
                            break

                    except ValueError:

                        print(f"{Fore.RED}{Style.BRIGHT}Please enter a valid number greater than 0.")


                
                self.bal+= dep

                print(f'{Style.BRIGHT} We are depositing the money in your account. Hold on...')
                time.sleep(4)

                def sound3():
                    playsound("Success.wav")

                t3= threading.Thread(target=sound3)
                t3.start()
                print(f"{Fore.GREEN}{Style.BRIGHT}{dep} dollars were successfully deposited into your account")
                print(f'Total account balance: {Style.BRIGHT}{self.bal}')
                time.sleep(3)


            elif act=='transfer':

                while True:

                    try:

                        cre= int(input("Enter the amount you want to transfer: "))

                        if cre<=0:
                            print("Amount needs to be greater than 0. Try again.")

                        if cre>self.bal:
                            print(f'{Fore.RED}{Style.BRIGHT}The amount you want to transfer cannot be more than your account balance. Try again')

                        elif cre>0:
                            break

                    except ValueError:

                        print(f"{Fore.RED}{Style.BRIGHT}Please enter a valid number greater than 0.")

                    
                self.bal-=cre

                print(f'{Style.BRIGHT} We are transferring the money from your account. Hold on...')
                time.sleep(4)

                def sound4():
                    playsound("Success.wav")

                t4= threading.Thread(target=sound4)
                t4.start()
                print(f"{Fore.RED}{Style.BRIGHT}{cre} dollars were successfully transferred from your account")
                print(f'Total account balance: {Style.BRIGHT}{self.bal}')
                time.sleep(3)
            
            elif act=='delete':

                while True:

                    if self.bal>0:
                        print(f"{Fore.RED}{Style.BRIGHT}Error in deleting account. Account Balance must be Zero.")
                        break

                    if self.bal==0:
                        print(f"{Fore.BLUE}{Style.BRIGHT}{self.user}!{Style.RESET_ALL} A/c No. {Fore.BLUE}{Style.BRIGHT}{self.num2}.")
                        print(f'{Fore.GREEN}{Style.BRIGHT}Your account was deleted successfully. ')
                        print(f"{Fore.RED}We are sorry to see you go!")
                        print(f"{Style.BRIGHT}Thanks for using our services \n We hope to see you again in the future.")
                        exit()
                
            elif act== 'exit':
                print(f'{Style.BRIGHT}Goodbye! See you later.')
                break


u1= Account()
u1.login()
u1.transaction()




