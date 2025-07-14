todolist=[]

def add():
    task=input("Enter task: ")
    priority=input("Enter priority (Low/Medium/High): ")
    todolist.append({"Task":task, "Status":"Pending", "Priority":priority})
    print("New Task Added Successfully!\n")

def view():
    print("Your TO-DO List:")
    if todolist == []:
        print("No pending tasks!\n")
    else:
        for i, task in enumerate(todolist, 1):
            print(f"{i}.Task - {task['Task']}\n  Status - {task['Status']}\n  Priority - {task.get('Priority', 'N/A')}\n")
        print("\n")


def done():
    if todolist==[]:
        print("List is Empty\n")
    else:
        try:
            key=int(input("Enter task number you want to mark as complete: "))-1
            if 0<=key<len(todolist):
                todolist[key]['Status']='Completed'
                print(f"Task Completed:\n {todolist[key]['Task']}\n")
            else:
                print(+"Invalid Task Number!\n")
        except ValueError:
            print("Please enter valid Task Number\n")



def remove():
    if todolist==[]:
        print("List is Empty\n")
    else:
        try:
            key=int(input("Enter task number you want to remove: "))-1
            if 0<=key<len(todolist):    
                confirm=input(f"Are you sure you want to remove '{todolist[key]['Task']}'? (y/n): ")
                if confirm.lower()=="y":
                    removedtask=todolist.pop(key)
                    print(f"Task Removed:\n {removedtask['Task']} - {removedtask['Status']}\n")
                else:
                    print("Task not removed\n")
            else:
                print("Invalid Task Number!\n")
        except ValueError:
            print("Please enter valid Task Number\n")


def clear():
    confirm=input("Are you sure you want to clear all tasks? (y/n): ")
    if confirm.lower() == "y":
        todolist.clear()
        print("All tasks cleared successfully!\n")
    else:
        print(F"Tasks not cleared\n") 


def menu():
    while(True):
        print("Welcome to To Do List Application")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Clear All Tasks")
        print("6. Exit")
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
            clear()
        elif ch=="6":
            print("Exiting The Application")
            exit()
        else:
            print("Invalid option. Try again!!\n")
menu()
