import csv
import os
from enum import Enum


class Priority(Enum):
    #for example:
    #Priority.HIGH.value == 3
    #Priority.HIGH.name == "HIGH"
    HIGH = 3
    MEDIUM = 2
    LOW = 1


class Task:
    def __init__(self, title, description, priority, completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed

    def to_list(self):
        return [
            self.title,
            self.description,
            self.priority.name,
            self.completed
        ]


class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_from_csv()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_csv()
        print("Work Has Been Added!")
        print("-" * 30)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_csv()
            print("Woek Has Been Removed!")
            print("-" * 30)
        else:
            print("Invalid Number Was Entered!")
            print("-" * 30)

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_to_csv()
            print("Woek Has Been Marked That It Was Done!")
            print("-" * 30)
        else:
            print("Invalid Number Was Entered!")
            print("-" * 30)

    def show_tasks(self):
        if not self.tasks:
            print("List Is Empty!")
            print("-" * 30)
            return

        self.sort_by_priority()

        for i, task in enumerate(self.tasks):
            if task.completed == True:
                status = "Was Done!"
            else :
                status = "Wasn't Done!"
                
            print(f"{i + 1}. {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Priority: {task.priority.name}")
            print(f"   Status: {status}")
            print("-" * 30)

    def sort_by_priority(self):
         def priority_value(task):
             return task.priority.value

         self.tasks.sort(key=priority_value, reverse=True)


    def save_to_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Description", "Priority", "Completed"])
            for task in self.tasks:
                writer.writerow(task.to_list())

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title, desc, priority, completed = row
                task = Task(
                    title,
                    desc,
                    Priority[priority],
                    completed == "True"
                )
                self.tasks.append(task)




def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add")
    print("2. Delete")
    print("3. Show List")
    print("4. Mark Work As Completed")
    print("5. Exit")
    print("-" * 30)


def get_priority():
    print("Choose The Priority Of This Action:")
    print("1. High")
    print("2. Mid")
    print("3. Low")
    choice = input("Choose : ")

    if choice == "1":
        return Priority.HIGH
    elif choice == "2":
        return Priority.MEDIUM
    else:
        return Priority.LOW


def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Your Choice : ")

        if choice == "1":
            title = input("Title : ")
            desc = input("Description : ")
            priority = get_priority()
            todo.add_task(Task(title, desc, priority))

        elif choice == "2":
            todo.show_tasks()
            index = int(input("Work Number : ")) - 1
            todo.remove_task(index)

        elif choice == "3":
            todo.show_tasks()

        elif choice == "4":
            todo.show_tasks()
            index = int(input("Work Number : ")) - 1
            todo.mark_completed(index)

        elif choice == "5":
            print("Exited The Program...")
            break

        else:
            print("Invalid Input!")


if __name__ == "__main__":
    main()
