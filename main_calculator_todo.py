
#  A calculator program that performs basic arithmetic operations
def add1(x, y):
    return x + y

def subtract1(x, y):
    return x - y
def multiply1(x, y):
    return x * y

def divide1(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
        return x / y   


print("Welcome to the Muhammad Ali Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice=input("Enter your choice (1/2/3/4):")
num=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

if choice == '1':
    result=add1(num, num2)
    print("Result:", result)   


elif choice == '2':
    result=subtract1(num, num2)
    print("Result:", result)

elif choice == '3':
    result=multiply1(num, num2)
    print("Result:", result)

elif choice == '4':
    result=divide1(num, num2)
    print("Result:", result)
else:
    print("Invalid input. Please choose 1, 2, 3, or 4.")


# To do list is used to add and delete tasks
tasks =   []

# def show_menu():
#     print("\nWhat do you want to do?")
#     print("1. Add a task")
#     print("2. Show all tasks")
#     print("3. Delete a task")
#     print("4. Exit")
    

def add_task():
    task = input("Write your task: ")
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks found.")

    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def delete_task():
    show_tasks()
    try:
        number = int(input("Enter task number to delete: "))
        if number >= 1 and number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")
    except:
       print("Please enter a valid number.")

while True:
    print("\nWhat do you want to do?")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Exit")
    choice = input("Choose 1, 2, 3 or 4: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break

    else:   
        print("Please choose a correct option.")
        































