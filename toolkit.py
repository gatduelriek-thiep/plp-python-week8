import random
# Print the title of your project
print("Welcome to your Toolkit Game engineer by Gatduel")
# This is a game title
tasks = []
while True:
    print("\n --Toolkit Menu--")
    print("1. Play a number guessing game")
    print("2. Manage To-Do list")
    print("3. Use Simple Calculator")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        print("\n Welcome to the Number Guessing Game!")
        secret_number = random.randint(1, 10)
        while True:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == secret_number:
                print("Correct! You guessed the number!")
                break
            else:
                print("Wrong! Try again.")
    
    # To-Do List Manager
    
    elif choice == "2":
        print("\n To-Do List Manager")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")

        todo_choice = input("Choose an option (1-3): ")
        
        if todo_choice == "1":
            if not tasks:
                print("📭 No tasks yet.")
            else:
                print("📋 Your tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif todo_choice == "2":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            print(f" Task '{new_task}' added.")

        elif todo_choice == "3":
            if not tasks:
                print(" No tasks to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                remove_index = int(input("Enter the number of the task to remove: "))
                if 1 <= remove_index <= len(tasks):
                    removed = tasks.pop(remove_index - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print(" Invalid task number.")
 # Simple Calculator
    elif choice == "3":
        print("\n Simple Calculator")
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print(f"Result: {num1 + num2}")
        elif operator == "-":
            print(f"Result: {num1 - num2}")
        elif operator == "*":
            print(f"Result: {num1 * num2}")
        elif operator == "/":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print(" Cannot divide by zero!")
        else:
            print("Invalid operator.")

    # Quit
    elif choice == "4":
        print(" Goodbye! Thanks for using the toolkit.")
        break

    # Invalid input
    else:
        print(f"{choice} is not on the menu. Please try again.")
