To-Do List Application (Written By Python)

A simple and practical command-line To-Do List application written in Python.

This project allows users to manage daily tasks with priorities, persistent storage, and task completion tracking.


Features:

Add new tasks with:

Title

Description

Priority (High, Medium, Low)

View all tasks in a clean, readable format

Automatic sorting by priority (High → Low)

Mark tasks as completed

Delete tasks from the list

Persistent storage using a CSV file (tasks.csv)

Simple and user-friendly CLI menu


Technologies Used:

Python 3

Built-in libraries: csv, os, enum

No external dependencies required.


How It Works:

When the program starts, it automatically loads tasks from "tasks.csv" (if it exists, if not, program will build one automatically).

All changes (add, delete, complete) are immediately saved to the CSV file.

Tasks are displayed sorted by priority.

Task status clearly shows whether it is completed or not.