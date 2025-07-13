import json
from colorama import Fore, Style, init
init(autoreset=True)
todolist=[]


def save():
    with open("tasks.json","w") as f:
        json.dump(todolist, f)

def load():
    global todolist
    try:
        with open("tasks.json","r") as f:
            todolist=json.load(f)
    except FileNotFoundError:
        todolist=[]

def add():
    task=input("Enter task: ")
    priority=input("Enter priority (Low/Medium/High): ")
    todolist.append({"Task":task, "Status":"Pending", "Priority":priority})
    save()
    print(Fore.GREEN+"New Task Added Successfully!\n")


def view():
    print(Style.BRIGHT + Fore.CYAN + "Your TO-DO List:")
    if todolist == []:
        print(Fore.YELLOW + "No pending tasks!\n")
    else:
        for i, task in enumerate(todolist, 1):
            print(Fore.BLUE + f"{i}.Task - {task['Task']}\n  Status - {task['Status']}\n  Priority - {task.get('Priority', 'N/A')}\n")
        print("\n")


def done():
    if todolist==[]:
        print(Fore.YELLOW+"List is Empty\n")
    else:
        try:
            key=int(input("Enter task number you want to mark as complete: "))-1
            if 0<=key<len(todolist):
                todolist[key]['Status']='Completed'
                print(Fore.GREEN+f"Task Completed:\n {todolist[key]['Task']}\n")
                save()
            else:
                print(Fore.RED+"Invalid Task Number!\n")
        except ValueError:
            print(Fore.RED+"Please enter valid Task Number\n")



def remove():
    if todolist==[]:
        print(Fore.YELLOW+"List is Empty\n")
    else:
        try:
            key=int(input("Enter task number you want to remove: "))-1
            if 0<=key<len(todolist):    
                confirm=input(Fore.RED+f"Are you sure you want to remove '{todolist[key]['Task']}'? (y/n): ")
                if confirm.lower()=="y":
                    removedtask=todolist.pop(key)
                    print(Fore.GREEN+f"Task Removed:\n {removedtask['Task']} - {removedtask['Status']}\n")
                    save()
                else:
                    print(Fore.GREEN+"Task not removed\n")
            else:
                print(Fore.RED+"Invalid Task Number!\n")
        except ValueError:
            print(Fore.RED+"Please enter valid Task Number\n")

    
def menu():
    load()
    while(True):
        print(Style.BRIGHT+Fore.MAGENTA+"Welcome to To Do List Application")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Exit")
        ch=input("Enter your choice: ")
        if ch=="1":
            add()
        elif ch=="2":
            view()
        elif ch=="3":
            done()
        elif ch=="4":
            remove()
        elif ch=="5":
            print(Fore.YELLOW+"Exiting The Application")
            exit()
        else:
            print(Fore.RED+"Invalid option. Try again!!\n")
menu()
