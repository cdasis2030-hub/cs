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
        return
    
    for i in range(len(tasks)):
        stat = "Done" if status[i] else "Not done"
        print(f"{i+1}. {tasks[i]} | {subjects[i]} | {deadlines[i]} | {stat}")
    print()

def mark_done():
    print("\n--- MARK A TASK AS DONE ---")
    view_tasks()
    if len(tasks) == 0:
        return
    
    num = int(input("Task number to mark as done: "))
    if 1 <= num <= len(tasks):
        status[num-1] = True
        print("Task marked as done!\n")
    else:
        print("Invalid number!\n")

def menu():
    while True:
        print("===== STUDY TRACKER =====")
        print("1 - Add Task")
        print("2 - View Tasks")
        print("3 - Mark Task as Done")
        print("4 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid. Try again.\n")

# Run the menu
menu()
