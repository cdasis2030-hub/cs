# Study Tracker
The Study Tracker is a simple Python-based tool designed to help students organize and manage their academic tasks. It allows users to record tasks, subjects, deadlines, and track completion status in an easy and efficient way. The goal of this project is to give students a lightweight, beginner-friendly system for managing schoolwork without needing complex apps or online accounts.

# Project Overview
This program serves as a basic task manager that runs in the terminal. Students often struggle with keeping track of assignments across different subjects, and traditional planners can be messy or easily forgotten. Study Tracker solves this by offering a simple, structured way to list and monitor tasks using a clean command-line interface.

# Problem Statement
Many students forget deadlines or lose track of tasks because most available tools are either too complicated or require constant internet access. Physical planners can also be easily misplaced. This project addresses that issue by providing a simple offline solution that stores tasks temporarily while the program is running. It’s especially useful for beginners learning Python and organization skills at the same time.

# Project Objectives
The main objectives of Study Tracker are to:

- Provide a clear and simple way to record school tasks.
- Allow students to view, monitor, and manage deadlines.
- Give users the ability to mark tasks as completed.
- Encourage better study habits through organized task tracking.
- Offer a beginner-friendly example of list-based data management in Python.

# Planned Features
- Add new tasks with subject and deadline.
- View all existing tasks in list form.
- Mark tasks as completed.
- Use basic Python lists to store task information.
- Display a clean, readable output in the terminal.
- Ability to delete a task from the list

# Planned Inputs and Outputs
Inputs:
- Task name
- Subject
- Deadline
- Task selection for marking as done

Outputs:
- A formatted list of tasks
- Task status (Done / Not Done)
- Confirmation messages after actions
- Updated task lists after changes

# Logic Plan
User Inputs: The user interacts through terminal prompts (e.g., entering task name, subject, etc.).

Task Storage: All information is stored in four parallel Python lists:
- tasks
- subjects
- deadlines
- status

Processing: Using IF-ELSE logic, user choices control adding tasks, viewing tasks, or marking tasks as completed.

Outputs: The program prints formatted task lists, status updates, and confirmation messages. Users can continue managing tasks through a loop-based menu.

# Example Output
===== STUDY TRACKER =====
- 1 - Add Task
- 2 - View Tasks
- 3 - Mark Task as Done
- 4 - Exit
- User chose: 1

-OUPUT OF INPUT 1:
- --- ADD TASK ---
- Task name: Homework 3
- Subject: Math
- Deadline: Friday
- Task added!

# Contributors
Roa, Asis, Muanag 
