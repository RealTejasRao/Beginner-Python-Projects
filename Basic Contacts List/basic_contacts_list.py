import os
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)
import playsound
from playsound import playsound
import time
import threading

class Contact:


    def __init__(self):

        grp= ['add', 'view', 'delete', 'delall', 'exit', 'help', 'edit']

        while True:

            print(f"{Style.BRIGHT}{Fore.CYAN}Please select an action to perform. (Add/View/Edit/Delete/DelAll/Exit/Help): ", end="")
            act= input().lower().strip()

            if act not in grp:
                print(f"{Style.BRIGHT}{Fore.RED}Please enter a valid input from the following. (Add/View/Edit/Delete/DelAll/Exit/Help) ")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            else:
                break

        if act=='add':
            self.add()

        elif act=='view':
            self.view()

        elif act=='delete':
            self.delete()

        elif act=='delall':
            self.delall()

        elif act=='exit':
            print(f'{Style.BRIGHT}GOODBYE!')
            exit()

        elif act=='edit':
            self.edit()

        elif act=='help':
            self.help()

    def add(self):
        while True:
            name= input("Enter the name : ").strip()

            if name=='':
                print(f"{Style.BRIGHT}{Fore.RED}Name cannot be empty. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            elif len(name)<3:
                print(f"{Style.BRIGHT}{Fore.RED}Name should contain atleast 3 characters. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            elif len(name)>20:
                print(f"{Style.BRIGHT}{Fore.RED}Name cannot contain more than 20 characters. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            else:
                break

        while True:
            num= input("Enter the phone number: ").strip()

            if any(i.isalpha() for i in num):
                print(f"{Style.BRIGHT}{Fore.RED}Number cannot contain alphabets.")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            elif num=='':
                print(f"{Style.BRIGHT}{Fore.RED}Number cannot be empty. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()


            elif len(num)>15:
                print(f"{Style.BRIGHT}{Fore.RED}Number cannot contain more than 15 characters. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            elif len(num)<8:
                print(f"{Style.BRIGHT}{Fore.RED}Number must contain a minimum of 8 characters. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            else:
                break

        with open('contact_list', 'a+') as f:

            f.write(f'{name} : {num}\n')


        print(f"{Style.BRIGHT}{Fore.GREEN}Contact has been added succesfully")
        threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
        print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
        time.sleep(3)
        self.__init__()

    def view(self):

        with open("contact_list", 'a+') as f:
            f.seek(0)
            lines=f.readlines()
            if not lines:
                print(f"{Style.BRIGHT}{Fore.RED}Contact List is Empty")
            else:
                for i, line in enumerate(lines, start=1):
                    print(f"{i}. {line}")

        print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
        time.sleep(3)
        self.__init__()

    
    def delete(self):
        
        rem= input("Enter the phone number you want to remove from the list: ").strip()
        with open('contact_list', 'r') as f:
            lines= f.readlines()

            with open("contact_list", 'w+') as f:
                found=False
                for line in lines:
                    if rem not in line:
                        f.write(line)

                    else:
                        found=True
                
                if found:
                    print(f"{Style.BRIGHT}{Fore.GREEN}Contact removed successfully.")
                    threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()

                else:
                    print(f"{Style.BRIGHT}{Fore.RED}Invalid number. No contact found.")
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
        
        print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
        time.sleep(3)
        self.__init__()

    
    def delall(self):

        while True:
        
            print(f'{Style.BRIGHT}{Fore.RED}ARE YOU SURE YOU WANT TO DELETE THE WHOLE CONTACT LIST? (YES/NO): ', end="")
            conf= input().lower().strip()

            grp2= ['yes','no']

            if conf not in grp2:
                print(f"{Style.BRIGHT}{Fore.RED}Please enter a valid input. (YES/NO)")

            else:
                break

        if conf == 'yes':
            try:
                os.remove('contact_list')
                print(f"{Fore.GREEN}{Style.BRIGHT}Entire Contact List was deleted successfully.")
                threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
            except FileNotFoundError:
                print(f"{Style.BRIGHT}{Fore.RED}Contact list file not found.")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
        else:
            print(f"{Style.BRIGHT}{Fore.YELLOW}Deletion cancelled.")

        print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
        time.sleep(3)
        self.__init__()

    def edit(self):

        while True:

            change= input("To edit the details of a contact, please enter the phone number of the person: ").strip()

            if any(i.isalpha() for i in change):
                    print(f"{Style.BRIGHT}{Fore.RED}Number cannot contain alphabets.")
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            elif change=='':
                print(f"{Style.BRIGHT}{Fore.RED}Number cannot be empty. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()


            elif len(change)>15:
                print(f"{Style.BRIGHT}{Fore.RED}Number cannot contain more than 15 characters. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            elif len(change)<8:
                print(f"{Style.BRIGHT}{Fore.RED}Number must contain a minimum of 8 characters. Try again")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

            else:
                break

    
        with open("contact_list", 'r') as f:
            lines= f.readlines()
            if not any(change in line for line in lines):
                    print(f"{Style.BRIGHT}{Fore.RED}Number not found.")
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                    print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
                    time.sleep(3)
                    self.__init__()

            
            
            else:
                while True:
                    new_name= input("Enter the New Name : ").strip()

                    if new_name=='':
                        print(f"{Style.BRIGHT}{Fore.RED}Name cannot be empty. Try again")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                    elif len(new_name)<3:
                        print(f"{Style.BRIGHT}{Fore.RED}Name should contain atleast 3 characters. Try again")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                    elif len(new_name)>20:
                        print(f"{Style.BRIGHT}{Fore.RED}Name cannot contain more than 20 characters. Try again")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                    else:
                        break

                while True:
                    new_num= input("Enter new phone number: ").strip()

                    if any(i.isalpha() for i in new_num):
                        print(f"{Style.BRIGHT}{Fore.RED}Number cannot contain alphabets.")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                    elif new_num=='':
                        print(f"{Style.BRIGHT}{Fore.RED}Number cannot be empty. Try again")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()


                    elif len(new_num)>15:
                        print(f"{Style.BRIGHT}{Fore.RED}Number cannot contain more than 15 characters. Try again")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                    elif len(new_num)<8:
                        print(f"{Style.BRIGHT}{Fore.RED}Number must contain a minimum of 8 characters. Try again")
                        threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                    else:
                        break


        with open("contact_list", 'w+') as f:

            for line in lines:
                if change not in line:
                    f.write(line)

                else:
                    f.write(f"{new_name} : {new_num}\n")

        print(f"{Style.BRIGHT}{Fore.GREEN}Contact edited successfully.")

        print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
        time.sleep(3)
        self.__init__()


    def help(self):

        print(f"{Style.BRIGHT}{Fore.CYAN}Options:")
        print(f"  Add    - Add a new contact")
        print(f"  View   - View all contacts")
        print(f"  Delete - Remove a contact by phone number")
        print(f"  DelAll - Delete all contacts")
        print(f"  Exit   - Exit the program")
        print(f"  Help   - Show this help message")
        
        print(f"{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Home Page. Please wait...")
        time.sleep(3)
        self.__init__()


c1= Contact()



