import json


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def add_tasks(tasks):
    task_id = len(tasks) + 1
    title = input('Enter task title: ')
    description = input('Enter task description: ')
    completed = False
    tasks[task_id] = {'title': title, 'description': description, 'completed': completed}
    print(f'Task {task_id} added.')


def view_tasks(tasks):
    
    if not tasks:
        print('No tasks in the To-Do list.')
    else:
        for task_id, task in tasks.items():
            status = 'Completed' if task['completed'] else 'Not Completed'
            print(f"Task {task_id}: {task['title']} - {status}")


def mark_completed_task(tasks):
    task_id = int(input('Enter the task ID to mark as completed: '))
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        print(f'Task {task_id} marked as completed.')
    else:
        print('Task not found in the To-Do list.')


def delete_task(tasks):
    task_id = input('Enter the task ID to delete: ')
    if task_id in tasks:
        del tasks[task_id]
        print(f'Task {task_id} deleted.')
        save_tasks(tasks)
    else:
        print('Task not found in the To-Do list.')


def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = int(input('Enter your choice (1/2/3/4/5): '))

        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_completed_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            save_tasks(tasks)
            print('To-Do list saved!')
            break
        else:
            print('Invalid choice. Please try again!')


if __name__ == '__main__':
    main()
