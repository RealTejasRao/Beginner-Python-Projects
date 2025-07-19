import time
import playsound
from playsound import playsound
import keyboard
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import threading

def clock():

    while True:
        act= input("Please select an action to perform (Time/Stopwatch/Timer/Alarm/Exit): ").lower().strip()

        def tme():

            print(f'The Date is {Fore.RED}{Style.BRIGHT}{time.strftime('%d/%m/%Y')}{Style.RESET_ALL} and the Time is {Fore.RED}{Style.BRIGHT}{time.strftime('%H:%M')}')

        def Stopwatch():

            print(f"{Fore.RED} {Style.BRIGHT} Press ENTER to Stop")
            
            i=0
            count=0

            while True:

                time.sleep(0.1)
                i+=0.1
                if i>=1:
                    count+=1
                    i=0
                    print(count)

            
                if keyboard.is_pressed("Enter"):

                    break
            print(f'Stopwatch stopped. Total Time= {count}')
            input()
                    

        def Timer():


            while True:

                try:


                    min= float(input("How many minutes? : ").strip())

                    if min<0:

                        print("Please enter a positive integer greater than 0")

                    else:
                        break
                        

                except ValueError:

                    print("Enter a valid integer")


            for i in range(int(min*60), -1, -1):

                m, s= divmod(i,60)
                print(f'{m:02d}:{s:02d} left')
                time.sleep(1)


            def sound():

                playsound("LongAlarm.mp3")
            print(f'{Fore.GREEN}{Style.BRIGHT}TIMER STOPPED.')


            t1= threading.Thread(target=sound)
            t1.start()
            

        def alarm():

            print(f'The current time is {Fore.RED}{Style.BRIGHT}{time.strftime('%H:%M')}')
            

            res= (input("Set a time to set the Alarm for (HH:MM): ").strip())

            print(f"{Fore.GREEN}{Style.BRIGHT}Alarm set for {res}")

            while True:
                if res==time.strftime("%H:%M"):
                    break

            def sound2():
                playsound("LongAlarm.mp3")
                
            print(f"{Fore.BLUE}TIME TO WAKE UP!!!!{Style.RESET_ALL} It is {res} ")
            

            t1= threading.Thread(target=sound2).start()

        grp= ['time', 'stopwatch', 'timer', 'alarm', 'exit']

        while True:

            if act not in grp:
                print("Enter a valid option (Time/Stopwatch/Timer/Alarm/Exit) ")
                break
            if act=='time':
                tme()
                break

            elif act== 'stopwatch':
                Stopwatch()
                break

            elif act=='timer':
                Timer()
                break

            elif act=='alarm':
                alarm()
                break

            elif act== 'exit':
                print("Goodbye! See you again!")
                exit()

            
clock()


        


