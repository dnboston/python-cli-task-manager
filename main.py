from task_manager.task_manager import TaskManager


def show_menu():
    print("\n" + "=" * 20)
    print(" Task Manager ")
    print("=" * 20)
    print("1) Add task")
    print("2) List tasks")
    print("3) Mark task as done")
    print("4) Delete task")
    print("5) Exit")


def main():
    task_manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if not choice:
            print("Please enter a choice.")
            continue

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            task_manager.mark_task_done()
        elif choice == "4":
            task_manager.delete_task()
        elif choice.lower() == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()