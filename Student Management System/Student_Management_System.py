import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import threading
import playsound
from playsound import playsound
import random
import time
import string

class Student:

    def __init__(self):

        print(f"{Style.BRIGHT}This is the Admin Portal. You are a new user. Please sign up.")

        while True:

            while True:

                adminname1= input("Enter Your Full Name: ").strip().lower()


                if all(i.isalpha() or i.isspace() for i in adminname1) and adminname1!="":
                    if len(adminname1)<3:
                        print(f"{Style.BRIGHT}{Fore.RED}Name must contain a minimum of 3 characters. Try again.")

                    elif len(adminname1)>=3:
                        break
                else:
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon= True).start()
                    print(f'{Style.BRIGHT}{Fore.RED}A name can contain only alphabets/Name cannot be empty.')

                    

            adminname2= input('Confirm Your Full Name: ').strip().lower()

            if adminname1!=adminname2:
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                print(f"{Style.BRIGHT}{Fore.RED}Names Did Not Match. TRY AGAIN")

            elif adminname1==adminname2:
                break

        grp1, grp2, grp3, grp4= string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits

        while True:

            while True:

                valid= True

                adpass1= input("Create a New Password: ").strip()

                if not any(i in grp1  for i in adpass1):
                    print(f"{Style.BRIGHT}{Fore.RED}Password must contain a lowecase letter. ")
                    valid= False

                if not any(i in grp2 for i in adpass1):
                    print(f"{Style.BRIGHT}{Fore.RED}Password must contain a uppercase letter.")           
                    valid= False

                if not any(i in grp3 for i in adpass1):
                    print(f"{Style.BRIGHT}{Fore.RED}Password must contain a special character.")
                    valid= False

                if not any(i in grp4 for i in adpass1):
                    print(f"{Style.BRIGHT}{Fore.RED}Password must contain a number..")
                    valid= False

                if valid:
                    break

            adpass2= input('Confirm Password: ').strip()


            if adpass1!=adpass2:
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                print(f"{Style.BRIGHT}{Fore.RED}Passwords Did Not Match. TRY AGAIN")

            elif adpass1==adpass2:
                break

        threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
        print(f"{Fore.GREEN}{Style.BRIGHT}Welcome {Fore.BLUE}{Style.BRIGHT}{adminname1.capitalize()}. {Fore.GREEN}{Style.BRIGHT}You have succesfully created an account. You have been automatically logged in.")

        wholedict={}
        self.grp4=grp4
        self.wholedict=wholedict

    def portal(self):

        while True:
            act= input(f'{Style.BRIGHT}This is the Student Management System. Please select an action to perform.(Add/Delete/Search/Update/List/Topper/Average/Exit/Help): ').lower().strip()

            grp6= ['add', 'delete', 'search', 'update', 'list', 'topper', 'average', 'exit', 'help']

            if act not in grp6:
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                print(f'{Style.BRIGHT}{Fore.RED}Invalid input. Please select a valid action to perform.(Add/Delete/Search/Update/List/Topper/Average/Exit/Help)')

            elif act=='add':
                self.add()
                break
            elif act=='list':
                self.list()
                break

            elif act=='delete':
                self.delete()
                break
            
            elif act=='search':
                self.search()
                break

            elif act== 'update':
                self.update()
                break

            elif act=='topper':
                self.topper()
                break

            elif act=='average':
                self.average()
                break
        
            elif act=='exit':
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye, See you later!")
                exit()

            elif act=='help':
                self.help()
                break

    def add(self):

        while True:

            print(f'{Style.BRIGHT}To add a student to the Student Management database, Please fill the details below.')


            adname1= input("Enter Full Name of the Student: ").strip().lower()

            if all(i.isalpha() or i.isspace() for i in adname1) and adname1!="":

                if len(adname1)<3:
                    print(f"{Style.BRIGHT}{Fore.RED}Name must contain a minimum of 3 characters. Try again.")

                elif len(adname1)>=3:
                    break

        adname2= " ".join(i.capitalize() for i in adname1.split())
        
        while True:

            try:

                adage= int(input("Enter age of student: ").strip())


                if adage<=0:
                    print(f"{Style.BRIGHT}{Fore.RED}Please enter a valid age.")

                elif adage>0:
                    break

            
            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}Please a valid number greater than 0.")
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

        grp5= ['male', 'female', 'unspecified']

        while True: 

            adgender= input("Enter Gender of Student (Male/Female/Unspecified): ").lower().strip()

            if adgender not in grp5:
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                print(f"{Style.BRIGHT}{Fore.RED}Invalid input. Please enter a valid input from the following (Male/Female/Unspecified)")

            else:
                break


        while True:

                try:

                    admarks1= int(input("Enter marks in Physics (0 to 100): ").strip())
                    
                    if 0<=admarks1<=100:
                        break
                    
                    elif admarks1<0:
                        print("Please enter a positive integer greater than 0.")

                    elif admarks1>100:
                        print("Please enter a number between 0 and 100")

                    

                except ValueError:
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                    print("Please a valid integer.")
            
        while True:

                try:

                    admarks2= int(input("Enter marks in Chemistry(0 to 100): ").strip())
                    
                    if 0<=admarks2<=100:
                        break
                    
                    elif admarks2<0:
                        print("Please enter a positive integer greater than 0.")

                    elif admarks2>100:
                        print("Please enter a number between 0 and 100")

                except ValueError:
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                    print("Please a valid integer.")

        while True:

                try:

                    admarks3= int(input("Enter marks in Maths (0 to 100): ").strip())
                    
                    if 0<=admarks3<=100:
                        break
                    
                    elif admarks3<0:
                        print("Please enter a positive integer greater than 0.")

                    elif admarks3>100:
                        print("Please enter a number between 0 and 100")

                except ValueError:
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                    print("Please enter a valid integer.")

    
        adavg= round((admarks1+admarks2+admarks3)/3)

        print(f"{Style.BRIGHT}{Fore.GREEN}All details have been filled.")
        time.sleep(1)
        adid= "".join(random.choices(self.grp4, k=6))
        
        print(f"{Style.BRIGHT}{Fore.YELLOW}Generating a unique Student ID. Please wait...")
        time.sleep(4)
        print(f"Student ID for {Style.BRIGHT}{Fore.BLUE}{adname2}{Style.RESET_ALL} is {Style.BRIGHT}{Fore.BLUE}{adid}.")


        studict= {

            "Student ID" : adid,
            "Name" : adname2,
            "Age" : adage,
            "Gender" : adgender,
            "Physics" : admarks1,
            "Chemistry" : admarks2,
            "Maths" : admarks3,
            'Average Marks' : adavg
        
        }
        
        for (key,value) in studict.items():
            print(f'{key} : {value}')
        
        while True:
            conf= input("These are the details you entered. Are you sure you want to add this student to the database? (Yes/No): ").lower().strip()

            if conf=='no':
                print(f"{Style.BRIGHT}{Fore.RED}Okay, you are being redirected to the Student Managament Dashboard. Please wait...")
                time.sleep(3)
                self.portal()
                break
            
            elif conf=='yes':

                self.wholedict[adid]= studict

                print(f"{Style.BRIGHT}Adding {Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}{adname2}{Style.RESET_ALL}{Style.BRIGHT} to the Student Database. Please wait...")
                time.sleep(5)
                threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
                print(f"{Fore.BLUE}{Style.BRIGHT}{adname2}{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} was succesfully added.")

                for idx1 ,(key, value) in enumerate(self.wholedict.items(), start=1):
                    print(f'{Style.BRIGHT}{Fore.CYAN}{idx1}.Details for {key} :')

                    if isinstance(value, dict):
                        for idx2, (key2,value2) in enumerate(value.items(), start=1):
                            print(f"{idx2}. {key2} : {value2}")

                    else:
                        print(f" {value}")

                break

            else:
                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                print(f'{Style.BRIGHT}{Fore.RED}Invalid Input. Enter (Yes/No)')


        time.sleep(3)
        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()

    def delete(self):

        if self.wholedict=={}:
            print(f"{Fore.RED}{Style.BRIGHT}No Students in the Database. Please add some to use the delete function.")
            print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
            time.sleep(4)
            self.portal()

        
        while True:

                try:

                    rem= (input("To remove a student from the databse, please enter the unique 6 digit Student ID: : ").strip())
                    
                    if len(rem)>6 or len(rem)<6:
                        print("Invalid input. A Student ID must be a 6 digit number.")
                        break
                    
                    elif len(rem)==6:
                        break

                except ValueError:
                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                    print("Please enter a valid number.")

        
        
        remname= ""
        wholedict2= self.wholedict.copy()
        found= False
        
        for keys, values in wholedict2.items():
            if keys==rem:
                if isinstance(values, dict):
                    for keys2, values2 in values.items():
                        if keys2=='Name':
                            remname= values2
                            print(f"{Style.BRIGHT}Removing {Fore.BLUE}{Style.BRIGHT}{remname}{Style.RESET_ALL}{Style.BRIGHT} from the database.Please wait...")
                            time.sleep(4)
                            found=True
                del self.wholedict[keys]
                break
                
        if found:
            
            threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
            print(f"{Fore.GREEN}{Style.BRIGHT}Successfully removed {Fore.BLUE}{Style.BRIGHT}{remname}{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}, ID= {Fore.BLUE}{Style.BRIGHT}{rem}{Style.RESET_ALL} {Fore.GREEN}{Style.BRIGHT}from the databse.")

        else:
            print(f'{Fore.RED}{Style.BRIGHT}No Student with ID {Fore.BLUE}{Style.BRIGHT}{rem}{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}. Try again.')

            self.delete()
        
        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()

    def search(self):

        if self.wholedict=={}:
            print(f"{Fore.RED}{Style.BRIGHT}No Students in the Database. Please add some to use the search function.")
            print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
            time.sleep(4)
            self.portal()

        while True:
            stu= input('Enter the Student ID to search for a student: ').strip()
            
            for keys,values in self.wholedict.items():
                if stu==keys:
                    print(self.wholedict.get(keys))
                    self.portal()
                    break

                else:
                    print(f"{Style.BRIGHT}{Fore.RED}Invalid Student ID. No Student Found.")
                    print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
                    time.sleep(4)
                    self.portal()

    def update(self):

        if self.wholedict=={}:
            print(f"{Fore.RED}{Style.BRIGHT}No Students in the Database. Please add some to use the update function.")
            print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
            time.sleep(4)
            self.portal()

        grp7= ["Physics", "Chemistry", "Maths"]
        updinfo= input("Enter the Student ID to update Student Info: ").strip()

        found= False
        for keys,values in self.wholedict.items():

            if updinfo==keys:
                print(f"{keys} : {values}" )
                found=True
            
                if isinstance(values,dict):

                    for keys2,values2 in values.items():

                        updinfo2= input("Enter the value that you want to change. (Ex= Name, Age etc.): ").strip().lower()

                        if updinfo2.capitalize()=='Name':

                            updinfo3= input(f"Enter new value of {updinfo2}: ").strip()
                            if all(i.isalpha() or i.isspace() for i in updinfo3) and updinfo3!="":

                                values[updinfo2]=updinfo3
                                threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
                                print(f"{Style.BRIGHT}{Fore.GREEN}Information updated succesfully.")
                                break

                            else:
                                print("A Name can only contain alphabets.")
                        
                        elif updinfo2.capitalize()=='Gender':

                            grp5= ['male', 'female', 'unspecified']
                            if updinfo2 in grp5:
                                updinfo3= input(f"Enter new value of {updinfo2}: ").strip()
                                values[updinfo2]=updinfo3
                                threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
                                print(f"{Style.BRIGHT}{Fore.GREEN}Information updated succesfully.")
                                break

                            else:
                                threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                                print(f"{Style.BRIGHT}{Fore.RED}Invalid input. Valid Values= Male/Female/Unspecified")
                                
                                
                        elif updinfo2.capitalize()=='Age':
                            
                            while True:

                                try:

                                    updinfo3= int(input(f"Enter new value of {updinfo2}: ").strip())


                                    if updinfo3<=0:
                                        print(f"{Style.BRIGHT}{Fore.RED}Please enter a valid age.")

                                    elif updinfo3>0:
                                        break

                                
                                except ValueError:
                                    print(f"{Style.BRIGHT}{Fore.RED}Please a valid number greater than 0.")
                                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()

                            values[updinfo2]=updinfo3
                            threading.Thread(target=playsound, args=("Success.wav",), daemon=True).start()
                            print(f"{Style.BRIGHT}{Fore.GREEN}Information updated succesfully.")
                            break

                        
                        elif updinfo2.capitalize() in grp7:

                            while True:

                                try:

                                    updinfo3= int(input(f"Enter new value of {updinfo2}: ").strip())
                                    
                                    if 0<=updinfo3<=100:
                                        break
                                    
                                    elif updinfo3<0:
                                        print("Please enter a positive integer greater than 0.")

                                    elif updinfo3>100:
                                        print("Please enter a number between 0 and 100")

                                except ValueError:
                                    threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                                    print("Please enter a valid integer.")

    
                            values['Average Marks']= round((values['Physics']+values['Chemistry']+values['Maths'])/3)

                        else:

                            threading.Thread(target=playsound, args=("Error.mp3",), daemon=True).start()
                            print(f"{Style.BRIGHT}{Fore.RED}No such Information Field Found. Valid Inputs= (Name/Gender/Age/Physics/Chemistry/Maths)")

        if not found:
            print("Invalid student ID. Try again")
            return self.update()
            
        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()

    def list(self):

        if self.wholedict=={}:
            print(f"{Fore.CYAN}{Style.BRIGHT}Seems empty in here :/ No students in the database")
            print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
            time.sleep(4)
            self.portal()

        for key,value in self.wholedict.items():
            print(f'{Style.BRIGHT}{Fore.BLUE}Details for {key}: ')
            if isinstance(value, dict):
                for idx, (key2, value2) in enumerate(value.items(), start=1):
                    print(f"{idx}.{key2} : {value2}")

            else:
                print(f" {value}")

        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()
            
    def topper(self):

        if self.wholedict=={}:
            print(f"{Fore.RED}{Style.BRIGHT}No Students in the Database. Please add some to use the topper function.")
            print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
            time.sleep(4)
            self.portal()

        grp8= []

        for key, value in self.wholedict.items():
            print(f"Average marks for {key}: ")
            if isinstance(value,dict):
                print(value.get('Average Marks'))
                grp8.append(value.get('Average Marks'))

        topmarks= max(grp8)

        for key,value in self.wholedict.items():
            if isinstance(value, dict):
                if value.get("Average Marks")==topmarks:
                    print(f"{Fore.GREEN}{Style.BRIGHT}Topper is {Fore.BLUE}{Style.BRIGHT}{value.get('Name')}{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}, Student ID- {Fore.BLUE}{Style.BRIGHT}{key}{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} with Average Marks {Fore.BLUE}{Style.BRIGHT}{topmarks}")
        
        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()
        
    def average(self):

        if self.wholedict=={}:
            print(f"{Fore.RED}{Style.BRIGHT}No Students in the Database. Please add some to use the delete function.")
            print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
            time.sleep(4)
            self.portal()

        grp9= []
        j=0
        for key,value in self.wholedict.items():
            if isinstance(value, dict):
                grp9.append(value.get('Average Marks'))
        

        for i in grp9:
            j+=i
        classavg= round(j/len(grp9))
        print(f"{Fore.GREEN}{Style.BRIGHT}Class average is {Fore.BLUE}{Style.BRIGHT}{classavg}.")


        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()
        
    def help(self):

        print(f'1. {Style.BRIGHT}{Fore.CYAN}Add{Style.RESET_ALL}= Add a student to the Database')

        print(f'2. {Style.BRIGHT}{Fore.CYAN}Delete{Style.RESET_ALL}= Delete a student from the Database')

        print(f'3. {Style.BRIGHT}{Fore.CYAN}Search{Style.RESET_ALL}= Search for a specific student in the database.')

        print(f'4. {Style.BRIGHT}{Fore.CYAN}Update{Style.RESET_ALL}= Change the details of a student in the databse.')

        print(f'5. {Style.BRIGHT}{Fore.CYAN}List{Style.RESET_ALL}= Print all the contents of the Database')

        print(f'6. {Style.BRIGHT}{Fore.CYAN}Topper{Style.RESET_ALL}= Find the Student Topper(Highest average marks)')

        print(f'7. {Style.BRIGHT}{Fore.CYAN}Average{Style.RESET_ALL}= Find the class average.')

        print(f'{Style.BRIGHT}{Fore.YELLOW}You are being redirected to the Student Management Dashboard by default. Please wait...')
        time.sleep(4)
        self.portal()
        
if __name__ == "__main__":
    u1 = Student()
    u1.portal()





