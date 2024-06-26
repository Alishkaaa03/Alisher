class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({'name': task_name, 'completed': False})

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task['name'] != task_name]

    def update_task(self, task_name, new_name):
        for task in self.tasks:
            if task['name'] == task_name:
                task['name'] = new_name

def main():
    todo_list = ToDoList()

    def display_tasks():
        for idx, task in enumerate(todo_list.tasks):
            print(f"{idx + 1}. [{ 'x' if task['completed'] else ' ' }] {task['name']}")

    def add_task():
        task_name = input("Введите название задачи: ")
        todo_list.add_task(task_name)

    def delete_task():
        task_name = input("Введите название задачи для удаления: ")
        todo_list.delete_task(task_name)

    def update_task():
        old_name = input("Введите название задачи, которую нужно обновить: ")
        new_name = input("Введите новое название задачи: ")
        todo_list.update_task(old_name, new_name)

    options = {
