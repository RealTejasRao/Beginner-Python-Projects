import colorama
from colorama import Fore, Back,Style
colorama.init(autoreset=True)


def todo():

    
    tasks= {}
    while True: 
        
        act= input("Select an action to perform (Add/View/Delete/Complete/Exit): ").lower().strip()

        if act not in ['add', 'view', 'delete', 'complete', 'exit']:

            print("Enter a valid action (Add/View/Delete/Complete/Exit) ")


        if act=='add':
            add= input("Enter the task you want to add: ").lower().strip()
            tasks[str(add)] = f'{Fore.RED}{Style.BRIGHT} Incomplete'


        elif act=='view':
            print("THIS IS YOUR TO-DO LIST: ")
            for i,(a,b) in enumerate(tasks.items(), start=1):
                print(f'{i}. {a} -{b}')

        #THIS CAN ALSO BE USED BUT THE USER NEEDS TO WRITE THE FULL TASK NAME (KEY) TO REMOVE THE TASK
        # elif act== 'delete':
        #     task= input("Enter the task you want to remove: ").lower().strip()
        #     tasks.pop(str(task))
        #     print(f'The updated to do list is: ')
        #     print(tasks)

        elif act== 'delete':

            while True:
                try:

                    task= int(input("Write the serial number of the task you want to remove: ").strip())

                    if task>len(tasks) or task==0:
                        print("The value you entered exceeds the total tasks in the To-Do List. Enter the serial number of the task you want to remove again.")

                    elif 0<task<=len(tasks):
                        break

                except ValueError:

                    print('Please enter a valid integer')

            grp1= list(tasks)[task-1]

            del tasks[grp1]

            print("The updated list is: ")
            for i,(a,b) in enumerate(tasks.items(),start=1):
                print(f'{i}. {a} -{b}')

        elif act== 'complete':

            while True:
                try:
                    comp= int(input("Enter the serial number of the task you want to mark as complete: ").strip())

                    if comp>len(tasks) or comp==0:
                        print('The value you entered exceeds the total tasks in the To-Do List. Enter the serial number of the task you want to remove again.')

                    elif 0<comp<=len(tasks):
                        break

                except ValueError:
                    print("Enter a valid integer.")

            grp2= list(tasks)[comp-1]

            tasks[grp2]= f'{Fore.GREEN}{Style.BRIGHT} Complete'

            print("Task marked as completed!")


        elif act== 'exit':
            print("Goodbye. See you again!")
            break

todo()
