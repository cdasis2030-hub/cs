# Study Tracker
tasks = []      
subjects = []    
deadlines = []   
status = []      

def add_task():
    print("\n--- ADD TASK ---") #header
    t = input("Task name: ") # get the name ! !
    s = input("Subject: ") # get the sub ! !
    d = input("Deadline: ") # get the deadline ! !

    tasks.append(t)
    subjects.append(s)
    deadlines.append(d)
    status.append(False)   # not done yet
    print("Task added!\n")


def view_tasks():
    print("\n--- TASK LIST ---")
    if len(tasks) == 0:
        print("No tasks yet.\n")
    else: 
        for i in range(len(tasks)):
            stat = "Done" if status[i] else "Not done"
            print(f"{i+1}. {tasks[i]} | {subjects[i]} | {deadlines[i]} | {stat}")
        print()
    input("Press Enter to go back to menu...")

def mark_done():
    print("\n--- MARK A TASK AS DONE ---")
    view_tasks()
    if len(tasks) == 0:
        return
    view_tasks()
    try:
        num = int(input("Task number to mark as done: "))
        if 1 <= num <= len(tasks):
            status[num-1] = True
            print("Task marked as done!\n")
        else:
            print("Invalid number!\n")

    except ValueError:
        print("Please enter a valid number!\n")
            
    input("Press Enter to go back to menu...")

def mark_done():
    print("\n--- MARK A TASK AS DONE ---")
    if len(tasks) == 0:
        print("No tasks yet.\n")
        input("Press Enter to go back to menu...")
        return

    view_tasks()
    try:
        num = int(input("Task number to mark as done: "))
        if 1 <= num <= len(tasks):
            status[num-1] = True
            print("Task marked as done!\n")
        else:
            print("Invalid number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

    input("Press Enter to go back to menu...")

def delete_task():
    print("\n--- DELETE TASK ---")
    if len(tasks) == 0:
        print("No tasks to delete.\n")
        input("Press Enter to go back to menu...")
        return

    view_tasks()
    try:
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            subjects.pop(num-1)
            deadlines.pop(num-1)
            status.pop(num-1)
            print("Task deleted!\n")
        else:
            print("Invalid number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

    input("Press Enter to go back to menu...")
    
def menu():
    while True:
        print("===== STUDY TRACKER =====")
        print("1 - Add Task")
        print("2 - View Tasks")
        print("3 - Mark Task as Done")
        print("4 - Delete Task")
        print("5 - Exit")
        
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid. Try again.\n")
            input("Press Enter to continue...")

# Run the menu
menu()
