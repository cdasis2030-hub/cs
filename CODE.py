# =============================
#       STUDY TRACKER
# =============================

tasks = []
subjects = []
deadlines = []
status = []

# -----------------------------
# Add Task
# -----------------------------
def add_task():
    print("\n--- ADD TASK ---")
    t = input("Task name: ").strip()
    s = input("Subject: ").strip()
    d = input("Deadline: ").strip()

    if t == "" or s == "" or d == "":
        print("All fields are required!\n")
    else:
        tasks.append(t)
        subjects.append(s)
        deadlines.append(d)
        status.append(False)
        print("Task added!\n")

    input("Press Enter to go back to menu...")

# -----------------------------
# View Tasks
# -----------------------------
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

# -----------------------------
# Mark Task as Done
# -----------------------------
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

# -----------------------------
# Delete Task
# -----------------------------
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

# -----------------------------
# Main Menu
# -----------------------------
def menu():
    while True:
        print("\n===== STUDY TRACKER =====")
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
            print("Invalid choice. Try again.\n")
            input("Press Enter to continue...")

# -----------------------------
# Run Program
# -----------------------------
menu()

