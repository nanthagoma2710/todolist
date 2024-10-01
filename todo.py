import pymysql

# Database connection settings
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "todolist"

def connect_db():
    """Establish a connection to the database"""
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

def create_table():
    """Create the todo table in the database"""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task VARCHAR(255)
        )
    """)
    db.commit()
    cursor.close()
    db.close()

def display_menu():
    """Display the main menu"""
    print("\nTo-Do List Menu:")
    print("1. Add task(s)")
    print("2. Delete task(s)")
    print("3. View tasks")
    print("4. Total tasks")
    print("5. Exit")

def add_tasks():
    """Add one or more tasks to the database"""
    db = connect_db()
    cursor = db.cursor()
    task_count = int(input("How many tasks would you like to add (up to 5)? "))
    if task_count < 1 or task_count > 5:
        print("You can add between 1 to 5 tasks at a time.")
    else:
        for _ in range(task_count):
            task = input("Enter the task: ")
            cursor.execute("INSERT INTO todo (task) VALUES (%s)", (task,))
            db.commit()
            print(f"Task '{task}' added.")
    cursor.close()
    db.close()

def delete_tasks():
    """Delete one or more tasks from the database"""
    db = connect_db()
    cursor = db.cursor()
    task_numbers = input("Enter the task numbers to delete (separated by spaces): ")
    task_numbers = list(map(int, task_numbers.split()))
    
    for task_number in task_numbers:
        cursor.execute("SELECT id FROM todo WHERE id = %s", (task_number,))
        if cursor.fetchone() is None:
            print(f"Task with ID '{task_number}' not found.")
        else:
            cursor.execute("DELETE FROM todo WHERE id = %s", (task_number,))
            db.commit()
            print(f"Task with ID '{task_number}' deleted.")
    cursor.close()
    db.close()

def view_tasks(): 
    """Display all tasks in the database"""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, task FROM todo")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for task in tasks:
            print(f"{task['id']}. {task['task']}")
    cursor.close()
    db.close()

def total_tasks():
    """Display the total number of tasks in the database"""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) AS total FROM todo")
    result = cursor.fetchone()
    if result:
        print(f"Total tasks: {result['total']}")
    else:
        print("No tasks in the database.")
    cursor.close()
    db.close()

def main():
    create_table() 
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_tasks()
        elif choice == "2":
            delete_tasks()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            total_tasks()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()